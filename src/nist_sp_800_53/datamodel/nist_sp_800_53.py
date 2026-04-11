# Auto generated from nist_sp_800_53.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-11T23:51:18
# Schema: NIST-SP-800-53
#
# id: https://w3id.org/lmodel/nist-sp-800-53
# description: Electronic (LinkML) Version of NIST SP 800-53 Rev 5 Controls and SP 800-53A Rev 5 Assessment Procedures
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = "5.2.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_SP_800_53 = CurieNamespace('nist_sp_800_53', 'https://w3id.org/lmodel/nist-sp-800-53/')
DEFAULT_ = NIST_SP_800_53


# Types

# Class references



SP80053Document = Any

@dataclass(repr=False)
class Catalog(YAMLRoot):
    """
    Top-level wrapper that mirrors OSCAL catalog shape
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Catalog"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Catalog"
    class_name: ClassVar[str] = "Catalog"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Catalog

    catalog: Optional[Union[dict, "CatalogBody"]] = None

@dataclass(repr=False)
class ProfileDocument(YAMLRoot):
    """
    Top-level wrapper for OSCAL profile files
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["ProfileDocument"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:ProfileDocument"
    class_name: ClassVar[str] = "ProfileDocument"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.ProfileDocument

    profile: Optional[Union[dict, "ProfileBody"]] = None

CatalogBody = Any

ProfileBody = Any

Metadata = Any

Revision = Any

@dataclass(repr=False)
class Role(YAMLRoot):
    """
    Role definition
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Role"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Role

    id: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


Party = Any

Address = Any

ResponsibleParty = Any

BackMatter = Any

Resource = Any

Citation = Any

ResourceLink = Any

@dataclass(repr=False)
class CatalogElement(YAMLRoot):
    """
    Base class for catalog elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["CatalogElement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:CatalogElement"
    class_name: ClassVar[str] = "CatalogElement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.CatalogElement

    id: Optional[str] = None
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if not isinstance(self.props, list):
            self.props = [self.props] if self.props is not None else []
        self.props = [v if isinstance(v, Property) else Property(**as_dict(v)) for v in self.props]

        if not isinstance(self.links, list):
            self.links = [self.links] if self.links is not None else []
        self.links = [v if isinstance(v, Link) else Link(**as_dict(v)) for v in self.links]

        if not isinstance(self.parts, list):
            self.parts = [self.parts] if self.parts is not None else []
        self.parts = [v if isinstance(v, Part) else Part(**as_dict(v)) for v in self.parts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentifiedElement(CatalogElement):
    """
    A catalog element with required id and optional title/class
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["IdentifiedElement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:IdentifiedElement"
    class_name: ClassVar[str] = "IdentifiedElement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.IdentifiedElement

    title: Optional[str] = None
    class: Optional[Union[str, "CatalogElementClassValue"]] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.class is not None and not isinstance(self.class, CatalogElementClassValue):
            self.class = CatalogElementClassValue(self.class)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlGroup(IdentifiedElement):
    """
    A group of controls (family)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["ControlGroup"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:ControlGroup"
    class_name: ClassVar[str] = "ControlGroup"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.ControlGroup

    groups: Optional[Union[Union[dict, "ControlGroup"], list[Union[dict, "ControlGroup"]]]] = empty_list()
    controls: Optional[Union[Union[dict, "Control"], list[Union[dict, "Control"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.groups, list):
            self.groups = [self.groups] if self.groups is not None else []
        self.groups = [v if isinstance(v, ControlGroup) else ControlGroup(**as_dict(v)) for v in self.groups]

        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, Control) else Control(**as_dict(v)) for v in self.controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Control(IdentifiedElement):
    """
    A security control
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Control"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Control"
    class_name: ClassVar[str] = "Control"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Control

    params: Optional[Union[Union[dict, "Parameter"], list[Union[dict, "Parameter"]]]] = empty_list()
    controls: Optional[Union[Union[dict, "ControlEnhancement"], list[Union[dict, "ControlEnhancement"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.params, list):
            self.params = [self.params] if self.params is not None else []
        self.params = [v if isinstance(v, Parameter) else Parameter(**as_dict(v)) for v in self.params]

        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, ControlEnhancement) else ControlEnhancement(**as_dict(v)) for v in self.controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlEnhancement(IdentifiedElement):
    """
    An enhancement to a control
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["ControlEnhancement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:ControlEnhancement"
    class_name: ClassVar[str] = "ControlEnhancement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.ControlEnhancement

    params: Optional[Union[Union[dict, "Parameter"], list[Union[dict, "Parameter"]]]] = empty_list()
    controls: Optional[Union[Union[dict, "ControlEnhancement"], list[Union[dict, "ControlEnhancement"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.params, list):
            self.params = [self.params] if self.params is not None else []
        self.params = [v if isinstance(v, Parameter) else Parameter(**as_dict(v)) for v in self.params]

        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, ControlEnhancement) else ControlEnhancement(**as_dict(v)) for v in self.controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Parameter(IdentifiedElement):
    """
    A configurable parameter used by a control
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Parameter"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Parameter"
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Parameter

    guidelines: Optional[Union[Union[dict, "Guideline"], list[Union[dict, "Guideline"]]]] = empty_list()
    select: Optional[Union[dict, "Selection"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.guidelines, list):
            self.guidelines = [self.guidelines] if self.guidelines is not None else []
        self.guidelines = [v if isinstance(v, Guideline) else Guideline(**as_dict(v)) for v in self.guidelines]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Guideline(YAMLRoot):
    """
    Additional prose guidance associated with a parameter
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Guideline"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Guideline"
    class_name: ClassVar[str] = "Guideline"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Guideline

    prose: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Property(YAMLRoot):
    """
    A name-value property with optional namespace and class attributes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Property"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Property"
    class_name: ClassVar[str] = "Property"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Property

    name: Optional[str] = None
    value: Optional[str] = None
    ns: Optional[str] = None
    class: Optional[Union[str, "CatalogPropertyClassValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self.class is not None and not isinstance(self.class, CatalogPropertyClassValue):
            self.class = CatalogPropertyClassValue(self.class)

        super().__post_init__(**kwargs)


Selection = Any

@dataclass(repr=False)
class Link(YAMLRoot):
    """
    Relationship link
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Link"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Link"
    class_name: ClassVar[str] = "Link"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Link

    href: Optional[str] = None
    rel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Part(IdentifiedElement):
    """
    Structured narrative part that can contain nested parts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Part"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Part"
    class_name: ClassVar[str] = "Part"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Part

    name: Optional[str] = None
    prose: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        super().__post_init__(**kwargs)


ImportResource = Any

IncludeControlsSelection = Any

MergeRules = Any

# Enumerations
class CatalogElementClassValue(EnumDefinitionImpl):
    """
    Allowed values for element-level class values
    """
    family = PermissibleValue(text="family")

    _defn = EnumDefinition(
        name="CatalogElementClassValue",
        description="Allowed values for element-level class values",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SP800-53",
            PermissibleValue(text="SP800-53"))
        setattr(cls, "SP800-53-enhancement",
            PermissibleValue(text="SP800-53-enhancement"))

class CatalogPropertyClassValue(EnumDefinitionImpl):
    """
    Allowed values for property-level class values
    """
    _defn = EnumDefinition(
        name="CatalogPropertyClassValue",
        description="Allowed values for property-level class values",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "sp800-53",
            PermissibleValue(text="sp800-53"))
        setattr(cls, "sp800-53a",
            PermissibleValue(text="sp800-53a"))
        setattr(cls, "zero-padded",
            PermissibleValue(text="zero-padded"))

# Slots
class slots:
    pass

slots.catalog = Slot(uri=NIST_SP_800_53.catalog, name="catalog", curie=NIST_SP_800_53.curie('catalog'),
                   model_uri=NIST_SP_800_53.catalog, domain=None, range=Optional[Union[dict, CatalogBody]])

slots.profile = Slot(uri=NIST_SP_800_53.profile, name="profile", curie=NIST_SP_800_53.curie('profile'),
                   model_uri=NIST_SP_800_53.profile, domain=None, range=Optional[Union[dict, ProfileBody]])

slots.metadata = Slot(uri=NIST_SP_800_53.metadata, name="metadata", curie=NIST_SP_800_53.curie('metadata'),
                   model_uri=NIST_SP_800_53.metadata, domain=None, range=Optional[Union[dict, Metadata]])

slots.groups = Slot(uri=NIST_SP_800_53.groups, name="groups", curie=NIST_SP_800_53.curie('groups'),
                   model_uri=NIST_SP_800_53.groups, domain=None, range=Optional[Union[Union[dict, ControlGroup], list[Union[dict, ControlGroup]]]])

slots.controls = Slot(uri=NIST_SP_800_53.controls, name="controls", curie=NIST_SP_800_53.curie('controls'),
                   model_uri=NIST_SP_800_53.controls, domain=None, range=Optional[Union[Union[dict, Control], list[Union[dict, Control]]]])

slots.params = Slot(uri=NIST_SP_800_53.params, name="params", curie=NIST_SP_800_53.curie('params'),
                   model_uri=NIST_SP_800_53.params, domain=None, range=Optional[Union[Union[dict, Parameter], list[Union[dict, Parameter]]]])

slots.props = Slot(uri=NIST_SP_800_53.props, name="props", curie=NIST_SP_800_53.curie('props'),
                   model_uri=NIST_SP_800_53.props, domain=None, range=Optional[Union[Union[dict, Property], list[Union[dict, Property]]]])

slots.guidelines = Slot(uri=NIST_SP_800_53.guidelines, name="guidelines", curie=NIST_SP_800_53.curie('guidelines'),
                   model_uri=NIST_SP_800_53.guidelines, domain=None, range=Optional[Union[Union[dict, Guideline], list[Union[dict, Guideline]]]])

slots.links = Slot(uri=NIST_SP_800_53.links, name="links", curie=NIST_SP_800_53.curie('links'),
                   model_uri=NIST_SP_800_53.links, domain=None, range=Optional[Union[Union[dict, Link], list[Union[dict, Link]]]])

slots.parts = Slot(uri=NIST_SP_800_53.parts, name="parts", curie=NIST_SP_800_53.curie('parts'),
                   model_uri=NIST_SP_800_53.parts, domain=None, range=Optional[Union[Union[dict, Part], list[Union[dict, Part]]]])

slots.select = Slot(uri=NIST_SP_800_53.select, name="select", curie=NIST_SP_800_53.curie('select'),
                   model_uri=NIST_SP_800_53.select, domain=None, range=Optional[Union[dict, Selection]])

slots.id = Slot(uri=NIST_SP_800_53.id, name="id", curie=NIST_SP_800_53.curie('id'),
                   model_uri=NIST_SP_800_53.id, domain=None, range=Optional[str])

slots.uuid = Slot(uri=NIST_SP_800_53.uuid, name="uuid", curie=NIST_SP_800_53.curie('uuid'),
                   model_uri=NIST_SP_800_53.uuid, domain=None, range=Optional[str])

slots.title = Slot(uri=NIST_SP_800_53.title, name="title", curie=NIST_SP_800_53.curie('title'),
                   model_uri=NIST_SP_800_53.title, domain=None, range=Optional[str])

slots.version = Slot(uri=NIST_SP_800_53.version, name="version", curie=NIST_SP_800_53.curie('version'),
                   model_uri=NIST_SP_800_53.version, domain=None, range=Optional[str])

slots.last_modified = Slot(uri=NIST_SP_800_53.last_modified, name="last-modified", curie=NIST_SP_800_53.curie('last_modified'),
                   model_uri=NIST_SP_800_53.last_modified, domain=None, range=Optional[str])

slots.oscal_version = Slot(uri=NIST_SP_800_53.oscal_version, name="oscal-version", curie=NIST_SP_800_53.curie('oscal_version'),
                   model_uri=NIST_SP_800_53.oscal_version, domain=None, range=Optional[str])

slots._class = Slot(uri=NIST_SP_800_53.class, name="_class", curie=NIST_SP_800_53.curie('class'),
                   model_uri=NIST_SP_800_53._class, domain=None, range=Optional[str])

slots.label = Slot(uri=NIST_SP_800_53.label, name="label", curie=NIST_SP_800_53.curie('label'),
                   model_uri=NIST_SP_800_53.label, domain=None, range=Optional[str])

slots.name = Slot(uri=NIST_SP_800_53.name, name="name", curie=NIST_SP_800_53.curie('name'),
                   model_uri=NIST_SP_800_53.name, domain=None, range=Optional[str])

slots.value = Slot(uri=NIST_SP_800_53.value, name="value", curie=NIST_SP_800_53.curie('value'),
                   model_uri=NIST_SP_800_53.value, domain=None, range=Optional[str])

slots.ns = Slot(uri=NIST_SP_800_53.ns, name="ns", curie=NIST_SP_800_53.curie('ns'),
                   model_uri=NIST_SP_800_53.ns, domain=None, range=Optional[str])

slots.prose = Slot(uri=NIST_SP_800_53.prose, name="prose", curie=NIST_SP_800_53.curie('prose'),
                   model_uri=NIST_SP_800_53.prose, domain=None, range=Optional[str])

slots.remarks = Slot(uri=NIST_SP_800_53.remarks, name="remarks", curie=NIST_SP_800_53.curie('remarks'),
                   model_uri=NIST_SP_800_53.remarks, domain=None, range=Optional[str])

slots.revisions = Slot(uri=NIST_SP_800_53.revisions, name="revisions", curie=NIST_SP_800_53.curie('revisions'),
                   model_uri=NIST_SP_800_53.revisions, domain=None, range=Optional[Union[Union[dict, Revision], list[Union[dict, Revision]]]])

slots.roles = Slot(uri=NIST_SP_800_53.roles, name="roles", curie=NIST_SP_800_53.curie('roles'),
                   model_uri=NIST_SP_800_53.roles, domain=None, range=Optional[Union[Union[dict, Role], list[Union[dict, Role]]]])

slots.parties = Slot(uri=NIST_SP_800_53.parties, name="parties", curie=NIST_SP_800_53.curie('parties'),
                   model_uri=NIST_SP_800_53.parties, domain=None, range=Optional[Union[Union[dict, Party], list[Union[dict, Party]]]])

slots.responsible_parties = Slot(uri=NIST_SP_800_53.responsible_parties, name="responsible-parties", curie=NIST_SP_800_53.curie('responsible_parties'),
                   model_uri=NIST_SP_800_53.responsible_parties, domain=None, range=Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]])

slots.role_id = Slot(uri=NIST_SP_800_53.role_id, name="role-id", curie=NIST_SP_800_53.curie('role_id'),
                   model_uri=NIST_SP_800_53.role_id, domain=None, range=Optional[str])

slots.party_uuids = Slot(uri=NIST_SP_800_53.party_uuids, name="party-uuids", curie=NIST_SP_800_53.curie('party_uuids'),
                   model_uri=NIST_SP_800_53.party_uuids, domain=None, range=Optional[Union[str, list[str]]])

slots.type = Slot(uri=NIST_SP_800_53.type, name="type", curie=NIST_SP_800_53.curie('type'),
                   model_uri=NIST_SP_800_53.type, domain=None, range=Optional[str])

slots.short_name = Slot(uri=NIST_SP_800_53.short_name, name="short-name", curie=NIST_SP_800_53.curie('short_name'),
                   model_uri=NIST_SP_800_53.short_name, domain=None, range=Optional[str])

slots.email_addresses = Slot(uri=NIST_SP_800_53.email_addresses, name="email-addresses", curie=NIST_SP_800_53.curie('email_addresses'),
                   model_uri=NIST_SP_800_53.email_addresses, domain=None, range=Optional[Union[str, list[str]]])

slots.addresses = Slot(uri=NIST_SP_800_53.addresses, name="addresses", curie=NIST_SP_800_53.curie('addresses'),
                   model_uri=NIST_SP_800_53.addresses, domain=None, range=Optional[Union[Union[dict, Address], list[Union[dict, Address]]]])

slots.addr_lines = Slot(uri=NIST_SP_800_53.addr_lines, name="addr-lines", curie=NIST_SP_800_53.curie('addr_lines'),
                   model_uri=NIST_SP_800_53.addr_lines, domain=None, range=Optional[Union[str, list[str]]])

slots.city = Slot(uri=NIST_SP_800_53.city, name="city", curie=NIST_SP_800_53.curie('city'),
                   model_uri=NIST_SP_800_53.city, domain=None, range=Optional[str])

slots.state = Slot(uri=NIST_SP_800_53.state, name="state", curie=NIST_SP_800_53.curie('state'),
                   model_uri=NIST_SP_800_53.state, domain=None, range=Optional[str])

slots.postal_code = Slot(uri=NIST_SP_800_53.postal_code, name="postal-code", curie=NIST_SP_800_53.curie('postal_code'),
                   model_uri=NIST_SP_800_53.postal_code, domain=None, range=Optional[str])

slots.imports = Slot(uri=NIST_SP_800_53.imports, name="imports", curie=NIST_SP_800_53.curie('imports'),
                   model_uri=NIST_SP_800_53.imports, domain=None, range=Optional[Union[Union[dict, ImportResource], list[Union[dict, ImportResource]]]])

slots.merge = Slot(uri=NIST_SP_800_53.merge, name="merge", curie=NIST_SP_800_53.curie('merge'),
                   model_uri=NIST_SP_800_53.merge, domain=None, range=Optional[Union[dict, MergeRules]])

slots.back_matter = Slot(uri=NIST_SP_800_53.back_matter, name="back-matter", curie=NIST_SP_800_53.curie('back_matter'),
                   model_uri=NIST_SP_800_53.back_matter, domain=None, range=Optional[Union[dict, BackMatter]])

slots.resources = Slot(uri=NIST_SP_800_53.resources, name="resources", curie=NIST_SP_800_53.curie('resources'),
                   model_uri=NIST_SP_800_53.resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.citation = Slot(uri=NIST_SP_800_53.citation, name="citation", curie=NIST_SP_800_53.curie('citation'),
                   model_uri=NIST_SP_800_53.citation, domain=None, range=Optional[Union[dict, Citation]])

slots.text = Slot(uri=NIST_SP_800_53.text, name="text", curie=NIST_SP_800_53.curie('text'),
                   model_uri=NIST_SP_800_53.text, domain=None, range=Optional[str])

slots.description = Slot(uri=NIST_SP_800_53.description, name="description", curie=NIST_SP_800_53.curie('description'),
                   model_uri=NIST_SP_800_53.description, domain=None, range=Optional[str])

slots.rlinks = Slot(uri=NIST_SP_800_53.rlinks, name="rlinks", curie=NIST_SP_800_53.curie('rlinks'),
                   model_uri=NIST_SP_800_53.rlinks, domain=None, range=Optional[Union[Union[dict, ResourceLink], list[Union[dict, ResourceLink]]]])

slots.media_type = Slot(uri=NIST_SP_800_53.media_type, name="media-type", curie=NIST_SP_800_53.curie('media_type'),
                   model_uri=NIST_SP_800_53.media_type, domain=None, range=Optional[str])

slots.href = Slot(uri=NIST_SP_800_53.href, name="href", curie=NIST_SP_800_53.curie('href'),
                   model_uri=NIST_SP_800_53.href, domain=None, range=Optional[str])

slots.rel = Slot(uri=NIST_SP_800_53.rel, name="rel", curie=NIST_SP_800_53.curie('rel'),
                   model_uri=NIST_SP_800_53.rel, domain=None, range=Optional[str])

slots.include_controls = Slot(uri=NIST_SP_800_53.include_controls, name="include-controls", curie=NIST_SP_800_53.curie('include_controls'),
                   model_uri=NIST_SP_800_53.include_controls, domain=None, range=Optional[Union[Union[dict, IncludeControlsSelection], list[Union[dict, IncludeControlsSelection]]]])

slots.with_ids = Slot(uri=NIST_SP_800_53.with_ids, name="with-ids", curie=NIST_SP_800_53.curie('with_ids'),
                   model_uri=NIST_SP_800_53.with_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.as_is = Slot(uri=NIST_SP_800_53.as_is, name="as-is", curie=NIST_SP_800_53.curie('as_is'),
                   model_uri=NIST_SP_800_53.as_is, domain=None, range=Optional[Union[bool, Bool]])

slots.how_many = Slot(uri=NIST_SP_800_53.how_many, name="how-many", curie=NIST_SP_800_53.curie('how_many'),
                   model_uri=NIST_SP_800_53.how_many, domain=None, range=Optional[str])

slots.choice = Slot(uri=NIST_SP_800_53.choice, name="choice", curie=NIST_SP_800_53.curie('choice'),
                   model_uri=NIST_SP_800_53.choice, domain=None, range=Optional[Union[str, list[str]]])

slots.IdentifiedElement__class = Slot(uri=NIST_SP_800_53.class, name="IdentifiedElement__class", curie=NIST_SP_800_53.curie('class'),
                   model_uri=NIST_SP_800_53.IdentifiedElement__class, domain=IdentifiedElement, range=Optional[Union[str, "CatalogElementClassValue"]])

slots.Control_controls = Slot(uri=NIST_SP_800_53.controls, name="Control_controls", curie=NIST_SP_800_53.curie('controls'),
                   model_uri=NIST_SP_800_53.Control_controls, domain=Control, range=Optional[Union[Union[dict, "ControlEnhancement"], list[Union[dict, "ControlEnhancement"]]]])

slots.ControlEnhancement_controls = Slot(uri=NIST_SP_800_53.controls, name="ControlEnhancement_controls", curie=NIST_SP_800_53.curie('controls'),
                   model_uri=NIST_SP_800_53.ControlEnhancement_controls, domain=ControlEnhancement, range=Optional[Union[Union[dict, "ControlEnhancement"], list[Union[dict, "ControlEnhancement"]]]])

slots.Property__class = Slot(uri=NIST_SP_800_53.class, name="Property__class", curie=NIST_SP_800_53.curie('class'),
                   model_uri=NIST_SP_800_53.Property__class, domain=Property, range=Optional[Union[str, "CatalogPropertyClassValue"]])
