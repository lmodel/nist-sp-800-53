"""Checks the upstream watch's reports against a stubbed GitHub API and doi.org.

scripts/check_upstream_release.py reads the network through one function,
`_get`. These tests replace it with a stub that answers as usnistgov/oscal-content
and doi.org would, so they run offline. They check what the script reports
when NIST moves something: a newer release without the pinned folder, a
network failure, a file NIST adds, and a tag that names another commit.
"""

import importlib.util
import io
import json
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
TAG_OBJECT = "8342d2e4798583f5bbbd1a6dc8b45e31ca0393f8"


@pytest.fixture
def watch():
    """A fresh copy of the script, so a stub never leaks into another test."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _not_found(url):
    return urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b"{}"))


def _stub(watch, latest="v1.6.0", folder="same", extra=(), tag_commit=None, doi=None):
    """A `_get` that answers as the API and doi.org do today, changed by the
    arguments: the latest release's tag, what that release holds in the
    pinned folder ("same", "changed" or "gone"), extra file names there, the
    commit the pinned tag names, and an exception doi.org raises."""
    pinned = {
        name: sha
        for name, (source, sha) in watch.PINNED_BLOBS.items()
        if source.startswith(watch.PINNED_PATH + "/")
    }
    left_out = sorted(watch.LEFT_OUT)
    licence_sha = watch.PINNED_BLOBS["LICENSE.md"][1]

    def folder_at(ref):
        names = dict(pinned)
        if ref == latest and folder == "changed":
            names[next(iter(names))] = "0" * 40
        entries = [{"name": n, "sha": s, "type": "file"} for n, s in names.items()]
        entries += [{"name": n, "sha": "1" * 40, "type": "file"} for n in left_out]
        if ref == latest:
            entries += [{"name": n, "sha": "2" * 40, "type": "file"} for n in extra]
        return entries

    def get(url):
        if url.startswith(watch.DOI_API):
            if doi is not None:
                raise doi
            if url.endswith(watch.PINNED_DOI):
                return json.dumps({"responseCode": 1}).encode()
            raise _not_found(url)
        path = url.removeprefix(watch.API)
        if path == f"/git/ref/tags/{watch.PINNED_TAG}":
            return json.dumps({"object": {"type": "tag", "sha": TAG_OBJECT}}).encode()
        if path == f"/git/tags/{TAG_OBJECT}":
            sha = tag_commit or watch.PINNED_COMMIT
            return json.dumps({"object": {"type": "commit", "sha": sha}}).encode()
        if path == "/releases/latest":
            return json.dumps({"tag_name": latest}).encode()
        for ref in {watch.PINNED_COMMIT, latest}:
            if path == f"/contents/{watch.PINNED_PATH}?ref={ref}":
                if ref == latest and folder == "gone":
                    raise _not_found(url)
                return json.dumps(folder_at(ref)).encode()
            if path == f"/contents/LICENSE.md?ref={ref}":
                entry = {"name": "LICENSE.md", "sha": licence_sha, "type": "file"}
                return json.dumps(entry).encode()
            if path == f"/contents/{watch.EDITIONS_PATH}?ref={ref}":
                return json.dumps(
                    [
                        {"name": "README.md", "type": "file"},
                        {"name": "rev4", "type": "dir"},
                        {"name": "rev5", "type": "dir"},
                    ]
                ).encode()
        raise AssertionError(f"unexpected request: {url}")

    return get


def _run(watch, tmp_path, **stub):
    watch._get = _stub(watch, **stub)
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_current_copies_report_nothing_to_do(watch, tmp_path):
    """Today's answers, an annotated tag included, give exit 0."""
    code, report = _run(watch, tmp_path)
    assert code == 0, report
    assert "6 of 6 copied files match" in report
    assert "For information" not in report


def test_a_release_without_the_pinned_folder_is_reported(watch, tmp_path):
    """A newer release that no longer holds the pinned folder is a finding,
    not a crash, and the copies are still checked."""
    code, report = _run(watch, tmp_path, latest="v1.7.0", folder="gone")
    assert code == 1
    assert "v1.7.0 no longer holds `nist.gov/SP800-53/rev5/json/`" in report
    assert "6 of 6 copied files match" in report


def test_a_changed_file_at_a_newer_release_is_reported(watch, tmp_path):
    code, report = _run(watch, tmp_path, latest="v1.7.0", folder="changed")
    assert code == 1
    assert "v1.7.0 changes" in report


def test_a_network_failure_is_reported_and_the_other_check_runs(watch, tmp_path):
    """doi.org failing ends the editions check with a line of the report; the
    catalog check still runs, and the run still fails."""
    code, report = _run(watch, tmp_path, doi=urllib.error.URLError("down"))
    assert code == 1
    assert "**The editions check could not finish: <urlopen error down>.**" in report
    assert "6 of 6 copied files match" in report


def test_a_file_nist_adds_is_reported_for_information(watch, tmp_path):
    """A new file in the pinned folder is listed, and on its own it does not
    fail the run."""
    added = "NIST_SP-800-53_rev5_NEW-baseline_profile.json"
    code, report = _run(watch, tmp_path, latest="v1.7.0", extra=(added,))
    assert code == 0, report
    assert "For information" in report
    assert f"`{added}`" in report


def test_a_moved_tag_is_reported(watch, tmp_path):
    code, report = _run(watch, tmp_path, tag_commit="3" * 40)
    assert code == 1
    assert "no longer names the pinned commit" in report
    assert "`333333333333`" in report
