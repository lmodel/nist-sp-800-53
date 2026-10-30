"""nist-sp-800-53.

Electronic (LinkML) Version of NIST SP 800-53 Rev 5 Controls and SP 800-53A Rev 5 Assessment Procedures
"""

try:
    from nist_sp_800_53._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
