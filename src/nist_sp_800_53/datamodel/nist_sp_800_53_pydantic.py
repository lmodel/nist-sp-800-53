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


metamodel_version = "1.7.0"
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
     'prefixes': {'catalog': {'prefix_prefix': 'catalog',
                              'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-53/catalog/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_sp_800_53': {'prefix_prefix': 'nist_sp_800_53',
                                     'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-53/'},
                  'profile': {'prefix_prefix': 'profile',
                              'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-53/profile/'}},
     'source': 'https://doi.org/10.6028/NIST.SP.800-53r5',
     'source_file': 'src/nist_sp_800_53/schema/nist_sp_800_53.yaml',
     'subsets': {'nist_sp_800_53r5_catalog': {'description': 'NIST SP 800-53 '
                                                             'Catalog subset for '
                                                             'controls and '
                                                             'assessment '
                                                             'procedures',
                                              'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                              'name': 'nist_sp_800_53r5_catalog'},
                 'nist_sp_800_53r5_profile': {'description': 'NIST SP 800-53 '
                                                             'Profile subset for '
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


class CatalogPropertyClassValue(str, Enum):
    """
    Allowed values for property-level class values
    """
    sp800_53 = "sp800-53"
    sp800_53a = "sp800-53a"
    zero_padded = "zero-padded"



class Catalog(ConfiguredBaseModel):
    """
    Top-level wrapper that mirrors OSCAL catalog shape
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    catalog: Optional[Any] = Field(default=None, description="""Root catalog payload""", json_schema_extra = { "linkml_meta": {'domain_of': ['SP80053Document', 'Catalog'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class ProfileDocument(ConfiguredBaseModel):
    """
    Top-level wrapper for OSCAL profile files
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_profile']})

    profile: Optional[Any] = Field(default=None, description="""Root profile payload""", json_schema_extra = { "linkml_meta": {'domain_of': ['SP80053Document', 'ProfileDocument'],
         'in_subset': ['nist_sp_800_53r5_profile']} })


class Role(ConfiguredBaseModel):
    """
    Role definition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })


class CatalogElement(ConfiguredBaseModel):
    """
    Base class for catalog elements
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })


class IdentifiedElement(CatalogElement):
    """
    A catalog element with required id and optional title/class
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog'],
         'slot_usage': {'class': {'name': 'class',
                                  'range': 'CatalogElementClassValue'}}})

    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })


class ControlGroup(IdentifiedElement):
    """
    A group of controls (family)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    controls: Optional[list[Control]] = Field(default=None, description="""List of controls in a group""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlGroup', 'Control', 'ControlEnhancement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })


class Control(IdentifiedElement):
    """
    A security control
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog'],
         'slot_usage': {'controls': {'name': 'controls',
                                     'range': 'ControlEnhancement'}}})

    params: Optional[list[Parameter]] = Field(default=None, description="""List of parameters for a control""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control', 'ControlEnhancement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    controls: Optional[list[ControlEnhancement]] = Field(default=None, description="""List of controls in a group""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlGroup', 'Control', 'ControlEnhancement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })


class ControlEnhancement(IdentifiedElement):
    """
    An enhancement to a control
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog'],
         'slot_usage': {'controls': {'name': 'controls',
                                     'range': 'ControlEnhancement'}}})

    params: Optional[list[Parameter]] = Field(default=None, description="""List of parameters for a control""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control', 'ControlEnhancement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    controls: Optional[list[ControlEnhancement]] = Field(default=None, description="""List of controls in a group""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlGroup', 'Control', 'ControlEnhancement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })


class Parameter(IdentifiedElement):
    """
    A configurable parameter used by a control
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    guidelines: Optional[list[Guideline]] = Field(default=None, description="""List of guidelines""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    select: Optional[Any] = Field(default=None, description="""Selection parameters for a parameter definition""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })


class Guideline(ConfiguredBaseModel):
    """
    Additional prose guidance associated with a parameter
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    prose: Optional[str] = Field(default=None, description="""Free-text prose content""", json_schema_extra = { "linkml_meta": {'domain_of': ['Guideline', 'Part'], 'in_subset': ['nist_sp_800_53r5_catalog']} })


class Property(ConfiguredBaseModel):
    """
    A name-value property with optional namespace and class attributes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog'],
         'slot_usage': {'class': {'name': 'class',
                                  'range': 'CatalogPropertyClassValue'}}})

    name: Optional[str] = Field(default=None, description="""Name of a property, part, or party""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    value: Optional[str] = Field(default=None, description="""Property value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    ns: Optional[str] = Field(default=None, description="""Namespace URI for a property""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    class_: Optional[CatalogPropertyClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })


class Link(ConfiguredBaseModel):
    """
    Relationship link
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    href: Optional[str] = Field(default=None, description="""Link or resource reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink', 'Link', 'ImportResource'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    rel: Optional[str] = Field(default=None, description="""Relationship type for a link""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link'], 'in_subset': ['nist_sp_800_53r5_catalog']} })


class Part(IdentifiedElement):
    """
    Structured narrative part that can contain nested parts
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'in_subset': ['nist_sp_800_53r5_catalog']})

    name: Optional[str] = Field(default=None, description="""Name of a property, part, or party""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    prose: Optional[str] = Field(default=None, description="""Free-text prose content""", json_schema_extra = { "linkml_meta": {'domain_of': ['Guideline', 'Part'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="class", description="""Classification of a catalog element or property""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog', 'nist_sp_800_53r5_profile']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Revision', 'CatalogElement'],
         'in_subset': ['nist_sp_800_53r5_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts that provide prose and structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_53r5_catalog']} })


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
Parameter.model_rebuild()
Guideline.model_rebuild()
Property.model_rebuild()
Link.model_rebuild()
Part.model_rebuild()
