from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "5.2.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'nist_sp_800_53',
     'default_range': 'string',
     'description': 'Electronic (LinkML) Version of NIST SP 800-53 Rev 5 Controls '
                    'and SP 800-53A Rev 5 Assessment Procedures ',
     'id': 'https://w3id.org/lmodel/nist-sp-800-53',
     'imports': ['linkml:types'],
     'name': 'NIST-SP-800-53',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_sp_800_53': {'prefix_prefix': 'nist_sp_800_53',
                                     'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-53/'},
                  'oscal_catalog': {'prefix_prefix': 'oscal_catalog',
                                    'prefix_reference': 'https://w3id.org/lmodel/oscal_catalog/'},
                  'oscal_profile': {'prefix_prefix': 'oscal_profile',
                                    'prefix_reference': 'https://w3id.org/lmodel/oscal_profile/'}},
     'source': 'https://doi.org/10.6028/NIST.SP.800-53r5',
     'source_file': 'src/nist_sp_800_53/schema/nist_sp_800_53.yaml',
     'subsets': {'nist_sp_800_53r4_catalog': {'description': 'NIST SP 800-53 Rev 4 '
                                                             'backward-compatibility '
                                                             'subset for catalog '
                                                             'elements present in '
                                                             'OSCAL 1.2.x '
                                                             'representations but '
                                                             'removed in Rev 5 '
                                                             '(e.g. depends-on '
                                                             'parameter '
                                                             'dependency)',
                                              'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                              'name': 'nist_sp_800_53r4_catalog'},
                 'nist_sp_800_53r5_catalog': {'description': 'NIST SP 800-53 Rev 5 '
                                                             'catalog subset for '
                                                             'controls and '
                                                             'assessment '
                                                             'procedures',
                                              'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                              'name': 'nist_sp_800_53r5_catalog'},
                 'nist_sp_800_53r5_cprt': {'description': 'NIST CPRT '
                                                          '(Cybersecurity and '
                                                          'Privacy Reference Tool) '
                                                          'export subset covering '
                                                          'SP 800-53, SP 800-53A, '
                                                          'and SP 800-53B element '
                                                          'and relationship data',
                                           'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                           'name': 'nist_sp_800_53r5_cprt'},
                 'nist_sp_800_53r5_profile': {'description': 'NIST SP 800-53 Rev 5 '
                                                             'profile subset for '
                                                             'baselines and '
                                                             'overlays',
                                              'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                              'name': 'nist_sp_800_53r5_profile'}}} )

class CatalogElementClassValue(str, Enum):
    """
    Allowed values for element-level class values
    """
    family = "family"
    SP800_53 = "SP800-53"
    SP800_53_enhancement = "SP800-53-enhancement"
    assessment_objective = "assessment-objective"


class CatalogPropertyClassValue(str, Enum):
    """
    Allowed values for property-level class values
    """
    sp800_53 = "sp800-53"
    sp800_53a = "sp800-53a"
    zero_padded = "zero-padded"


class CPRTElementTypeValue(str, Enum):
    """
    Allowed element_type values in NIST CPRT export data
    """
    family = "family"
    """
    SP 800-53 control family (e.g. AC, AU)
    """
    control = "control"
    """
    Top-level security or privacy control (e.g. AC-1)
    """
    control_enhancement = "control_enhancement"
    """
    Control enhancement (e.g. AC-1(1))
    """
    control_statement = "control_statement"
    """
    Normative control statement text
    """
    discussion = "discussion"
    """
    Non-normative discussion text for a control
    """
    odp = "odp"
    """
    Organization-Defined Parameter
    """
    odp_type = "odp_type"
    """
    ODP category (e.g. assignment, selection)
    """
    odp_statement = "odp_statement"
    """
    Full ODP statement text
    """
    examine = "examine"
    """
    SP 800-53A Examine assessment objective
    """
    interview = "interview"
    """
    SP 800-53A Interview assessment objective
    """
    test = "test"
    """
    SP 800-53A Test assessment objective
    """
    determination = "determination"
    """
    Assessment determination criterion
    """
    withdraw_reason = "withdraw_reason"
    """
    Reason a control was withdrawn from SP 800-53
    """
    reference = "reference"
    """
    Informational reference to an external publication
    """
    security_baseline = "security_baseline"
    """
    Security baseline designation (LOW / MODERATE / HIGH / NOT SELECTED)
    """
    privacy_baseline = "privacy_baseline"
    """
    Privacy baseline designation (P-HIGH / NOT SELECTED)
    """
    sort = "sort"
    """
    Sort-order key for display purposes
    """
    control_name_sort = "control_name_sort"
    """
    Sort-order key for control name ordering
    """


class CPRTRelationshipTypeValue(str, Enum):
    """
    Relationship type identifiers used in NIST CPRT export data
    """
    projection = "projection"
    """
    Represents a relationship between two elements
    """
    related = "related"
    """
    Denotes where a control is related to another control
    """
    incorporated_into = "incorporated_into"
    """
    Denotes where a withdrawn control was incorporated into another
    """
    moved_to = "moved_to"
    """
    Denotes where a withdrawn control was moved to
    """



class Catalog(ConfiguredBaseModel):
    """
    Top-level wrapper that mirrors OSCAL catalog shape
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['oscal_catalog:CatalogDocument'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    catalog: Optional[Any] = Field(default=None, description="""Root catalog payload""", json_schema_extra = { "linkml_meta": {'domain_of': ['SP80053Document', 'Catalog'],
         'exact_mappings': ['oscal_catalog:catalog'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class ProfileDocument(ConfiguredBaseModel):
    """
    Top-level wrapper for OSCAL profile files
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['oscal_profile:ProfileDocument'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_profile']})

    profile: Optional[Any] = Field(default=None, description="""Root profile payload""", json_schema_extra = { "linkml_meta": {'domain_of': ['SP80053Document', 'ProfileDocument'],
         'exact_mappings': ['oscal_profile:profile'],
         'in_subset': ['nist_sp_800_53r5_profile']} })


class Role(ConfiguredBaseModel):
    """
    Role definition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['oscal_catalog:Role'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:id'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'exact_mappings': ['oscal_catalog:title'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })


class CatalogElement(ConfiguredBaseModel):
    """
    Base class for catalog elements
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:id'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:props'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:links'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:parts'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class IdentifiedElement(CatalogElement):
    """
    A catalog element with required id and optional title/class
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog'],
         'slot_usage': {'_class': {'name': '_class',
                                   'range': 'CatalogElementClassValue'}}})

    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'exact_mappings': ['oscal_catalog:title'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'exact_mappings': ['oscal_catalog:_class'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'ProfileSetParameter'],
         'exact_mappings': ['oscal_catalog:label'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:id'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:props'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:links'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:parts'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class ControlGroup(IdentifiedElement):
    """
    A group of controls (family)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['oscal_catalog:Group'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    groups: Optional[list[ControlGroup]] = Field(default=None, description="""List of control groups in the catalog""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogBody', 'ControlGroup'],
         'exact_mappings': ['oscal_catalog:groups'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    controls: Optional[list[Control]] = Field(default=None, description="""List of controls in a group""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlGroup', 'Control', 'ControlEnhancement'],
         'exact_mappings': ['oscal_catalog:controls'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'exact_mappings': ['oscal_catalog:title'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'exact_mappings': ['oscal_catalog:_class'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'ProfileSetParameter'],
         'exact_mappings': ['oscal_catalog:label'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:id'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:props'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:links'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:parts'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class Control(IdentifiedElement):
    """
    A security control
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['oscal_catalog:Control'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog'],
         'slot_usage': {'controls': {'name': 'controls',
                                     'range': 'ControlEnhancement'}}})

    params: Optional[list[Any]] = Field(default=None, description="""List of parameters for a control""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control', 'ControlEnhancement'],
         'exact_mappings': ['oscal_catalog:params'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    controls: Optional[list[ControlEnhancement]] = Field(default=None, description="""List of controls in a group""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlGroup', 'Control', 'ControlEnhancement'],
         'exact_mappings': ['oscal_catalog:controls'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'exact_mappings': ['oscal_catalog:title'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'exact_mappings': ['oscal_catalog:_class'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'ProfileSetParameter'],
         'exact_mappings': ['oscal_catalog:label'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:id'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:props'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:links'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:parts'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class ControlEnhancement(IdentifiedElement):
    """
    An enhancement to a control
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['oscal_catalog:Control'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog'],
         'slot_usage': {'controls': {'name': 'controls',
                                     'range': 'ControlEnhancement'}}})

    params: Optional[list[Any]] = Field(default=None, description="""List of parameters for a control""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control', 'ControlEnhancement'],
         'exact_mappings': ['oscal_catalog:params'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    controls: Optional[list[ControlEnhancement]] = Field(default=None, description="""List of controls in a group""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlGroup', 'Control', 'ControlEnhancement'],
         'exact_mappings': ['oscal_catalog:controls'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'exact_mappings': ['oscal_catalog:title'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'exact_mappings': ['oscal_catalog:_class'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'ProfileSetParameter'],
         'exact_mappings': ['oscal_catalog:label'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:id'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:props'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:links'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:parts'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class Guideline(ConfiguredBaseModel):
    """
    Additional prose guidance associated with a parameter
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['oscal_catalog:ParameterGuideline'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    prose: Optional[str] = Field(default=None, description="""Free-text prose content""", json_schema_extra = { "linkml_meta": {'domain_of': ['Guideline', 'Part'],
         'exact_mappings': ['oscal_catalog:prose'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class Property(ConfiguredBaseModel):
    """
    A name-value property with optional namespace and class attributes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['oscal_catalog:Property'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog'],
         'slot_usage': {'_class': {'name': '_class',
                                   'range': 'CatalogPropertyClassValue'}}})

    name: Optional[str] = Field(default=None, description="""Name of a property, part, or party""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party', 'Property', 'Part'],
         'exact_mappings': ['oscal_catalog:name'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    value: Optional[str] = Field(default=None, description="""Property value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property'],
         'exact_mappings': ['oscal_catalog:value'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    ns: Optional[str] = Field(default=None, description="""Namespace URI for a property""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property'],
         'exact_mappings': ['oscal_catalog:ns'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    class_: Optional[CatalogPropertyClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'exact_mappings': ['oscal_catalog:_class'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class Link(ConfiguredBaseModel):
    """
    Relationship link
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['oscal_catalog:Link'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    href: Optional[str] = Field(default=None, description="""Link or resource reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink', 'Link', 'ImportResource'],
         'exact_mappings': ['oscal_catalog:href'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    rel: Optional[str] = Field(default=None, description="""Relationship type for a link""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link'],
         'exact_mappings': ['oscal_catalog:rel'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class Part(IdentifiedElement):
    """
    Structured narrative part that can contain nested parts
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['oscal_catalog:Part'],
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    name: Optional[str] = Field(default=None, description="""Name of a property, part, or party""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party', 'Property', 'Part'],
         'exact_mappings': ['oscal_catalog:name'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    prose: Optional[str] = Field(default=None, description="""Free-text prose content""", json_schema_extra = { "linkml_meta": {'domain_of': ['Guideline', 'Part'],
         'exact_mappings': ['oscal_catalog:prose'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'exact_mappings': ['oscal_catalog:title'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'exact_mappings': ['oscal_catalog:_class'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'ProfileSetParameter'],
         'exact_mappings': ['oscal_catalog:label'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:id'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:props'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'exact_mappings': ['oscal_catalog:links'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement', 'ProfileAdd'],
         'exact_mappings': ['oscal_catalog:parts'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Catalog.model_rebuild()
ProfileDocument.model_rebuild()
Role.model_rebuild()
CatalogElement.model_rebuild()
IdentifiedElement.model_rebuild()
ControlGroup.model_rebuild()
Control.model_rebuild()
ControlEnhancement.model_rebuild()
Guideline.model_rebuild()
Property.model_rebuild()
Link.model_rebuild()
Part.model_rebuild()
