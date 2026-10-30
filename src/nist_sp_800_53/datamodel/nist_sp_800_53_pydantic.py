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


metamodel_version = "1.12.0"
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


linkml_meta = LinkMLMeta({'annotations': {'cprt_framework_version': {'tag': 'cprt_framework_version',
                                                'value': 'SP_800_53_5_2_0'},
                     'oscal_content_commit': {'tag': 'oscal_content_commit',
                                              'value': 'f0de6d8d8c059d374f15e0ae07508d82e370fc1d'},
                     'oscal_content_tag': {'tag': 'oscal_content_tag',
                                           'value': 'v1.6.0'},
                     'publication_date': {'tag': 'publication_date',
                                          'value': '2025-08'}},
     'comments': ['The version is the release of Revision 5 that the catalog '
                  'carries, 5.2.0 of August 2025, and publication_date is that '
                  "release's date; Revision 5 itself was published in September "
                  "2020 and updated in December 2020. source is the publication's "
                  "digital object identifier. NIST's Cybersecurity and Privacy "
                  'Reference Tool names the same release SP_800_53_5_2_0, and the '
                  'catalog and the four baseline profiles NIST publishes for it in '
                  'usnistgov/oscal-content are copied to '
                  'src/nist_sp_800_53/schema/oscal-content/ at the tag and commit '
                  'in the annotations. scripts/check_upstream_release.py reads the '
                  'same pins and reports when NIST publishes a newer edition or '
                  "changes a copied file. The release tags are the schema's own "
                  'versions.',
                  'SP 800-53, SP 800-53A and SP 800-53B are works of the United '
                  'States Government and are not subject to copyright in the '
                  "United States. The descriptions here are this project's own "
                  "words; NIST's text of each control, parameter, objective and "
                  'method stays in the catalog copy.',
                  "NIST's catalog renders each family as an OSCAL group, each "
                  'control and control enhancement as an OSCAL control, each '
                  'statement, discussion, assessment objective and assessment '
                  'method as a part, each organization-defined parameter as a '
                  'parameter, each reference as a back-matter resource, and each '
                  'baseline as a profile. The broad_mappings name those '
                  'lmodel/oscal classes.'],
     'default_prefix': 'nist_sp_800_53',
     'default_range': 'string',
     'description': 'A LinkML model of the security and privacy controls that NIST '
                    'Special Publication 800-53, Revision 5, defines at Release '
                    '5.2.0: its twenty control families, their controls and '
                    'control enhancements, each with its statement, discussion, '
                    'organization-defined parameters, related controls and '
                    'references; the assessment objectives and methods that SP '
                    '800-53A gives each control; and the four control baselines of '
                    'SP 800-53B.',
     'id': 'https://w3id.org/lmodel/nist-sp-800-53',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'nist_sp_800_53',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_sp_800_53': {'prefix_prefix': 'nist_sp_800_53',
                                     'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-53/'},
                  'oscal': {'prefix_prefix': 'oscal',
                            'prefix_reference': 'https://w3id.org/lmodel/oscal/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/nist-sp-800-53',
                  'https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final',
                  'https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls',
                  'https://doi.org/10.6028/NIST.SP.800-53Ar5',
                  'https://doi.org/10.6028/NIST.SP.800-53B',
                  'https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/SP800-53/rev5'],
     'source': 'https://doi.org/10.6028/NIST.SP.800-53r5',
     'source_file': 'src/nist_sp_800_53/schema/nist_sp_800_53.yaml',
     'title': 'NIST SP 800-53 Security and Privacy Controls, Release 5.2.0',
     'types': {'sp80053_control_identifier': {'base': 'str',
                                              'description': "A control's "
                                                             'identifier: its '
                                                             "family's letters, a "
                                                             'hyphen and the '
                                                             "control's number "
                                                             'within the family, '
                                                             'such as AC-2.',
                                              'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                              'name': 'sp80053_control_identifier',
                                              'pattern': '^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)-[1-9][0-9]*$',
                                              'typeof': 'string',
                                              'uri': 'xsd:string'},
               'sp80053_control_or_enhancement_identifier': {'base': 'str',
                                                             'description': 'The '
                                                                            'identifier '
                                                                            'of a '
                                                                            'control '
                                                                            'or of '
                                                                            'a '
                                                                            'control '
                                                                            'enhancement, '
                                                                            'such '
                                                                            'as '
                                                                            'AC-2 '
                                                                            'or '
                                                                            'AC-2(1), '
                                                                            'where '
                                                                            'the '
                                                                            'publication '
                                                                            'cites '
                                                                            'either.',
                                                             'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                                             'name': 'sp80053_control_or_enhancement_identifier',
                                                             'pattern': '^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)-[1-9][0-9]*(\\([1-9][0-9]*\\))?$',
                                                             'typeof': 'string',
                                                             'uri': 'xsd:string'},
               'sp80053_enhancement_identifier': {'base': 'str',
                                                  'description': 'A control '
                                                                 "enhancement's "
                                                                 'identifier: its '
                                                                 "control's "
                                                                 'identifier and '
                                                                 'the '
                                                                 "enhancement's "
                                                                 'number in '
                                                                 'parentheses, '
                                                                 'such as AC-2(1).',
                                                  'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                                  'name': 'sp80053_enhancement_identifier',
                                                  'pattern': '^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)-[1-9][0-9]*\\([1-9][0-9]*\\)$',
                                                  'typeof': 'string',
                                                  'uri': 'xsd:string'},
               'sp80053_family_identifier': {'base': 'str',
                                             'description': 'The two letters that '
                                                            'name one of the '
                                                            'twenty control '
                                                            'families, such as AC '
                                                            'for Access Control.',
                                             'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                             'name': 'sp80053_family_identifier',
                                             'pattern': '^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)$',
                                             'typeof': 'string',
                                             'uri': 'xsd:string'},
               'sp80053_parameter_identifier': {'base': 'str',
                                                'description': 'The identifier '
                                                               "NIST's catalog "
                                                               'gives an '
                                                               'organization-defined '
                                                               'parameter, in '
                                                               'lower case: the '
                                                               'zero-padded '
                                                               'control '
                                                               'identifier, _odp '
                                                               'and the '
                                                               "parameter's "
                                                               'number, such as '
                                                               'ac-02_odp.01, or, '
                                                               'for a parameter '
                                                               'that aggregates '
                                                               'several, the '
                                                               'control '
                                                               'identifier, _prm_ '
                                                               'and a number, such '
                                                               'as ac-1_prm_1.',
                                                'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                                'name': 'sp80053_parameter_identifier',
                                                'pattern': '^[a-z]{2}-[0-9]{2}(\\.[0-9]{2})?_odp(\\.[0-9]{2})?$|^[a-z]{2}-[1-9][0-9]*(\\.[1-9][0-9]*)?_prm_[1-9][0-9]*$',
                                                'typeof': 'string',
                                                'uri': 'xsd:string'},
               'sp80053_withdrawal_target': {'base': 'str',
                                             'description': 'Where a withdrawn '
                                                            'control or '
                                                            'enhancement was '
                                                            'incorporated, as the '
                                                            'publication names it: '
                                                            'a control or '
                                                            'enhancement, such as '
                                                            'AC-2 or AC-2(1), one '
                                                            "item of a control's "
                                                            'statement, such as '
                                                            'AC-2k, or a whole '
                                                            'family, such as SR.',
                                             'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
                                             'name': 'sp80053_withdrawal_target',
                                             'pattern': '^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)(-[1-9][0-9]*(\\([1-9][0-9]*\\))?([a-z](\\.[1-9][0-9]*)*|\\([a-z]\\)(\\([1-9][0-9]*\\))*)?)?$',
                                             'typeof': 'string',
                                             'uri': 'xsd:string'}}} )

class Sp80053ControlStatus(str, Enum):
    """
    The one status the catalog marks: withdrawn. A control or enhancement that Revision 5 keeps carries no status.
    """
    WITHDRAWN = "WITHDRAWN"
    """
    Revision 5 withdrew the control or enhancement; incorporated_into, moved_to or withdrawal_reason says where it went.
    """


class Sp80053ImplementationLevel(str, Enum):
    """
    Who implements a control or enhancement, as NIST's reference data marks it.
    """
    ORGANIZATION = "ORGANIZATION"
    """
    The organization implements it, through its processes and people.
    """
    SYSTEM = "SYSTEM"
    """
    The system implements it, through its mechanisms.
    """


class Sp80053SelectionCardinality(str, Enum):
    """
    How many of a selection's choices the organization picks.
    """
    ONE = "ONE"
    """
    Exactly one choice, which the catalog leaves unwritten.
    """
    ONE_OR_MORE = "ONE_OR_MORE"
    """
    One or more choices, which the publication writes as Selection (one or more).
    """


class Sp80053AssessmentMethodKind(str, Enum):
    """
    The three assessment methods of SP 800-53A, as its catalog writes them.
    """
    EXAMINE = "EXAMINE"
    """
    Review, inspect, observe, study or analyze specifications, mechanisms or activities.
    """
    INTERVIEW = "INTERVIEW"
    """
    Hold discussions with individuals or groups.
    """
    TEST = "TEST"
    """
    Exercise mechanisms or activities under specified conditions.
    """


class Sp80053BaselineLevel(str, Enum):
    """
    The four control baselines SP 800-53B defines.
    """
    LOW = "LOW"
    """
    The baseline for a low-impact system.
    """
    MODERATE = "MODERATE"
    """
    The baseline for a moderate-impact system.
    """
    HIGH = "HIGH"
    """
    The baseline for a high-impact system.
    """
    PRIVACY = "PRIVACY"
    """
    The privacy baseline, which applies regardless of impact level.
    """



class Sp80053Catalog(ConfiguredBaseModel):
    """
    One release of the control catalog as a whole: its families, each holding its controls and their enhancements, the baselines that select from them, and the publications the catalog lists.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Catalog'],
         'class_uri': 'nist_sp_800_53:Catalog',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final'],
         'tree_root': True})

    catalog_release: str = Field(default=..., description="""The release of Revision 5 the catalog carries, as NIST numbers it, such as 5.2.0.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Catalog']} })
    control_families: list[Sp80053Family] = Field(default=..., description="""The twenty control families, in the order SP 800-53 gives them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Catalog']} })
    control_baselines: Optional[list[Sp80053Baseline]] = Field(default=None, description="""The control baselines of SP 800-53B that select from the catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Catalog']} })
    catalog_references: Optional[list[Sp80053Reference]] = Field(default=None, description="""The publications the catalog's references list, most of which a control cites.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Catalog']} })

    @field_validator('catalog_release')
    def pattern_catalog_release(cls, v):
        pattern=re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid catalog_release format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid catalog_release format: {v}"
            raise ValueError(err_msg)
        return v


class Sp80053Family(ConfiguredBaseModel):
    """
    One of the twenty families SP 800-53 sorts its controls into, such as Access Control or Supply Chain Risk Management.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Group'],
         'class_uri': 'nist_sp_800_53:Family',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://csrc.nist.gov/projects/risk-management/sp800-53-controls'],
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    family_id: str = Field(default=..., description="""The family's two letters, such as AC for Access Control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Family']} })
    title: str = Field(default=..., description="""The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['Sp80053Family',
                       'Sp80053Control',
                       'Sp80053ControlEnhancement',
                       'Sp80053Baseline'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the family is about, in the words of whoever records it. SP 800-53 gives the Program Management family an overview of its own, and the other families none.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['Sp80053Family'],
         'slot_uri': 'schema:description'} })
    family_controls: Optional[list[Sp80053Control]] = Field(default=None, description="""The controls of the family. A knowledge bundle relates a control to its family with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Family']} })


class Sp80053Control(ConfiguredBaseModel):
    """
    A security or privacy control: a safeguard with an identifier, a statement of what it requires, a discussion, parameters the organization defines, related controls, references, the assessment objective and methods SP 800-53A gives it, and its enhancements. A control Revision 5 withdrew keeps its identifier and says where it went.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'nist_sp_800_53:Control',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://csrc.nist.gov/projects/risk-management/sp800-53-controls'],
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    control_identifier: str = Field(default=..., description="""The control's identifier, such as AC-2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control']} })
    title: str = Field(default=..., description="""The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['Sp80053Family',
                       'Sp80053Control',
                       'Sp80053ControlEnhancement',
                       'Sp80053Baseline'],
         'slot_uri': 'schema:name'} })
    control_statement: Optional[Sp80053Statement] = Field(default=None, description="""The control statement: what the control or enhancement requires, as one text, a lettered or numbered list of items, or both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    control_discussion: Optional[str] = Field(default=None, description="""The discussion that follows the statement: context and guidance that help apply the control, which the publication does not require.""", json_schema_extra = { "linkml_meta": {'comments': ['Where the catalog links a control or a statement item inside '
                      "the text, a derivation keeps the link's text, which is the "
                      'identifier as the publication prints it, and where it links a '
                      "reference, the reference's label in brackets."],
         'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    control_parameters: Optional[list[Sp80053Parameter]] = Field(default=None, description="""The organization-defined parameters the statement leaves to the organization, in the order the catalog gives them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    related_control_ids: Optional[list[str]] = Field(default=None, description="""The controls and enhancements the publication lists as related, by identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    control_references: Optional[list[str]] = Field(default=None, description="""The publications the control or enhancement cites, by the labels the catalog's references carry, such as SP 800-12 or OMB A-130.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    assessment_objective: Optional[Sp80053AssessmentObjective] = Field(default=None, description="""The assessment objective SP 800-53A gives the control or enhancement: the determination statements an assessor checks, nested as the statement's items are.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    assessment_methods: Optional[list[Sp80053AssessmentMethod]] = Field(default=None, description="""The assessment methods SP 800-53A gives the control or enhancement, each with the objects it is applied to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    control_status: Optional[Sp80053ControlStatus] = Field(default=None, description="""The status the catalog gives a control or enhancement that Revision 5 withdrew. An active one carries none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    incorporated_into: Optional[list[str]] = Field(default=None, description="""For a withdrawn control or enhancement, what it was incorporated into, as the publication states it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    moved_to: Optional[list[str]] = Field(default=None, description="""For a withdrawn control or enhancement, the control or enhancement it moved to, as the publication states it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    withdrawal_reason: Optional[str] = Field(default=None, description="""For a withdrawn control or enhancement that the publication neither moved nor incorporated, what it says instead, such as that the enhancement is addressed through tailoring.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    implementation_level: Optional[list[Sp80053ImplementationLevel]] = Field(default=None, description="""Who implements the control or enhancement, as NIST's reference data marks it: the organization, the system, or both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    contributes_to_assurance: Optional[bool] = Field(default=None, description="""True where NIST's reference data marks the control or enhancement as one that contributes to assurance; absent otherwise.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    control_enhancements: Optional[list[Sp80053ControlEnhancement]] = Field(default=None, description="""The control's enhancements. A knowledge bundle relates an enhancement to its control with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control']} })

    @field_validator('control_references')
    def pattern_control_references(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid control_references format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid control_references format: {v}"
            raise ValueError(err_msg)
        return v


class Sp80053ControlEnhancement(ConfiguredBaseModel):
    """
    A control enhancement: added functionality or strength for a control, with an identifier of its own, which the publication and other documents cite apart from the control. It carries what a control carries, and names the control or enhancement it requires.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'nist_sp_800_53:ControlEnhancement',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://csrc.nist.gov/projects/risk-management/sp800-53-controls'],
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    enhancement_id: str = Field(default=..., description="""The enhancement's identifier, such as AC-2(1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053ControlEnhancement']} })
    title: str = Field(default=..., description="""The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['Sp80053Family',
                       'Sp80053Control',
                       'Sp80053ControlEnhancement',
                       'Sp80053Baseline'],
         'slot_uri': 'schema:name'} })
    control_statement: Optional[Sp80053Statement] = Field(default=None, description="""The control statement: what the control or enhancement requires, as one text, a lettered or numbered list of items, or both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    control_discussion: Optional[str] = Field(default=None, description="""The discussion that follows the statement: context and guidance that help apply the control, which the publication does not require.""", json_schema_extra = { "linkml_meta": {'comments': ['Where the catalog links a control or a statement item inside '
                      "the text, a derivation keeps the link's text, which is the "
                      'identifier as the publication prints it, and where it links a '
                      "reference, the reference's label in brackets."],
         'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    control_parameters: Optional[list[Sp80053Parameter]] = Field(default=None, description="""The organization-defined parameters the statement leaves to the organization, in the order the catalog gives them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    related_control_ids: Optional[list[str]] = Field(default=None, description="""The controls and enhancements the publication lists as related, by identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    control_references: Optional[list[str]] = Field(default=None, description="""The publications the control or enhancement cites, by the labels the catalog's references carry, such as SP 800-12 or OMB A-130.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    assessment_objective: Optional[Sp80053AssessmentObjective] = Field(default=None, description="""The assessment objective SP 800-53A gives the control or enhancement: the determination statements an assessor checks, nested as the statement's items are.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    assessment_methods: Optional[list[Sp80053AssessmentMethod]] = Field(default=None, description="""The assessment methods SP 800-53A gives the control or enhancement, each with the objects it is applied to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    control_status: Optional[Sp80053ControlStatus] = Field(default=None, description="""The status the catalog gives a control or enhancement that Revision 5 withdrew. An active one carries none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    incorporated_into: Optional[list[str]] = Field(default=None, description="""For a withdrawn control or enhancement, what it was incorporated into, as the publication states it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    moved_to: Optional[list[str]] = Field(default=None, description="""For a withdrawn control or enhancement, the control or enhancement it moved to, as the publication states it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    withdrawal_reason: Optional[str] = Field(default=None, description="""For a withdrawn control or enhancement that the publication neither moved nor incorporated, what it says instead, such as that the enhancement is addressed through tailoring.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    implementation_level: Optional[list[Sp80053ImplementationLevel]] = Field(default=None, description="""Who implements the control or enhancement, as NIST's reference data marks it: the organization, the system, or both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    contributes_to_assurance: Optional[bool] = Field(default=None, description="""True where NIST's reference data marks the control or enhancement as one that contributes to assurance; absent otherwise.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Control', 'Sp80053ControlEnhancement']} })
    required_controls: Optional[list[str]] = Field(default=None, description="""The controls and enhancements that must be implemented for the enhancement to apply, as NIST's catalog links them: its own control, and for SC-42(2) also SC-42(1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053ControlEnhancement']} })

    @field_validator('control_references')
    def pattern_control_references(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid control_references format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid control_references format: {v}"
            raise ValueError(err_msg)
        return v


class Sp80053Statement(ConfiguredBaseModel):
    """
    A control statement: the text of what a control or enhancement requires, and the items it is divided into.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_sp_800_53:Statement',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://csrc.nist.gov/projects/risk-management/sp800-53-controls']})

    statement_items: Optional[list[Sp80053StatementItem]] = Field(default=None, description="""The lettered or numbered items of the statement, in order, each of which may hold items of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Statement', 'Sp80053StatementItem']} })
    statement_text: Optional[str] = Field(default=None, description="""The statement's own text, before any items. A placeholder of the form {{ insert: param, <identifier> }} marks where an organization-defined parameter is inserted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Statement']} })


class Sp80053StatementItem(ConfiguredBaseModel):
    """
    One lettered or numbered item of a control statement, which may hold items of its own.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_sp_800_53:StatementItem',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://csrc.nist.gov/projects/risk-management/sp800-53-controls']})

    statement_items: Optional[list[Sp80053StatementItem]] = Field(default=None, description="""The lettered or numbered items of the statement, in order, each of which may hold items of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Statement', 'Sp80053StatementItem']} })
    item_label: str = Field(default=..., description="""The item's label as the publication prints it, such as a., 1. or (a).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053StatementItem']} })
    item_text: str = Field(default=..., description="""The item's text, with the same placeholders for parameters as the statement's text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053StatementItem']} })

    @field_validator('item_label')
    def pattern_item_label(cls, v):
        pattern=re.compile(r"^(([a-z]|[1-9][0-9]*)\.|\(([a-z]|[1-9][0-9]*)\))$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid item_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid item_label format: {v}"
            raise ValueError(err_msg)
        return v


class Sp80053Parameter(ConfiguredBaseModel):
    """
    An organization-defined parameter: a value the control statement leaves to the organization, either an assignment the organization fills in or a selection from the choices the publication lists. SP 800-53A labels each parameter but the ones that aggregate others, and gives most a guideline.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Parameter'],
         'class_uri': 'nist_sp_800_53:Parameter',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://doi.org/10.6028/NIST.SP.800-53Ar5']})

    parameter_id: str = Field(default=..., description="""The parameter's identifier in NIST's catalog, such as ac-02_odp.01.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Parameter']} })
    assessment_label: Optional[str] = Field(default=None, description="""The label SP 800-53A gives the parameter, such as AC-02_ODP[01]. A parameter that aggregates several has none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Parameter']} })
    parameter_label: Optional[str] = Field(default=None, description="""For an assignment, what the organization defines, such as personnel or roles.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Parameter']} })
    parameter_guidelines: Optional[list[str]] = Field(default=None, description="""The guidelines that say what a value must settle, such as that the frequency of a review is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Parameter']} })
    selection_choices: Optional[list[str]] = Field(default=None, description="""For a selection, the choices the publication lists, in order.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Parameter']} })
    selection_cardinality: Optional[Sp80053SelectionCardinality] = Field(default=None, description="""For a selection, how many choices the organization picks. The catalog marks one or more, and leaves the slot out when one choice is allowed, which is how OSCAL reads an absent how-many.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Parameter']} })
    aggregated_parameters: Optional[list[str]] = Field(default=None, description="""For a parameter that stands for several, the parameters it aggregates, by identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Parameter']} })
    alternative_identifiers: Optional[list[str]] = Field(default=None, description="""The identifiers an earlier release of the catalog gave the parameter, such as ac-1_prm_2 for ac-01_odp.03.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Parameter']} })
    alternative_label: Optional[str] = Field(default=None, description="""The label SP 800-53 prints where it differs from the one SP 800-53A gives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Parameter']} })

    @field_validator('assessment_label')
    def pattern_assessment_label(cls, v):
        pattern=re.compile(r"^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)-[0-9]{2}(\([0-9]{2}\)|\.[0-9]{2})?_ODP(\[[0-9]{2}\])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid assessment_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid assessment_label format: {v}"
            raise ValueError(err_msg)
        return v


class Sp80053AssessmentObjective(ConfiguredBaseModel):
    """
    An assessment objective of SP 800-53A: a determination statement an assessor checks, or a heading that groups the determination statements of one item of the control statement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_sp_800_53:AssessmentObjective',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://doi.org/10.6028/NIST.SP.800-53Ar5']})

    objective_label: str = Field(default=..., description="""The label SP 800-53A gives the objective, such as AC-02a.[01].""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053AssessmentObjective']} })
    objective_text: Optional[str] = Field(default=None, description="""The determination statement, with the same placeholders for parameters as the control statement. A heading has none.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053AssessmentObjective']} })
    sub_objectives: Optional[list[Sp80053AssessmentObjective]] = Field(default=None, description="""The objectives grouped under this one, in order.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053AssessmentObjective']} })

    @field_validator('objective_label')
    def pattern_objective_label(cls, v):
        pattern=re.compile(r"^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)-[0-9]{2}(\([0-9]{2}\))?([a-z]\.([0-9]{2})?)?(\([a-z]\)(\([0-9]{2}\))?)?(\[[0-9]{2}\])*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid objective_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid objective_label format: {v}"
            raise ValueError(err_msg)
        return v


class Sp80053AssessmentMethod(ConfiguredBaseModel):
    """
    One assessment method SP 800-53A gives a control or enhancement, with the objects an assessor selects from: documents and records to examine, people to interview, or mechanisms and activities to test.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_sp_800_53:AssessmentMethod',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://doi.org/10.6028/NIST.SP.800-53Ar5']})

    assessment_method: Sp80053AssessmentMethodKind = Field(default=..., description="""Which of the three methods this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053AssessmentMethod']} })
    assessment_objects: list[str] = Field(default=..., description="""The objects the method is applied to, in the order the publication lists them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053AssessmentMethod']} })

    @field_validator('assessment_objects')
    def pattern_assessment_objects(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid assessment_objects format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid assessment_objects format: {v}"
            raise ValueError(err_msg)
        return v


class Sp80053Reference(ConfiguredBaseModel):
    """
    A publication the catalog's references list, as they list it: its label, its citation and its address.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Resource'],
         'class_uri': 'nist_sp_800_53:Reference',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final']})

    reference_label: str = Field(default=..., description="""The label the controls cite the publication by, such as SP 800-12.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Reference']} })
    reference_citation: Optional[str] = Field(default=None, description="""The citation, as the catalog prints it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Reference']} })
    reference_url: Optional[str] = Field(default=None, description="""The address the catalog gives for the publication.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Reference']} })

    @field_validator('reference_label')
    def pattern_reference_label(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid reference_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid reference_label format: {v}"
            raise ValueError(err_msg)
        return v


class Sp80053Baseline(ConfiguredBaseModel):
    """
    One of the four control baselines SP 800-53B defines: the controls and enhancements selected for systems at the low, moderate or high impact level, or for privacy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Profile'],
         'class_uri': 'nist_sp_800_53:Baseline',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-53',
         'see_also': ['https://doi.org/10.6028/NIST.SP.800-53B'],
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    baseline_level: Sp80053BaselineLevel = Field(default=..., description="""Which of the four baselines this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Baseline']} })
    title: str = Field(default=..., description="""The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['Sp80053Family',
                       'Sp80053Control',
                       'Sp80053ControlEnhancement',
                       'Sp80053Baseline'],
         'slot_uri': 'schema:name'} })
    baseline_controls: list[str] = Field(default=..., description="""The controls and enhancements the baseline selects, by identifier, in the order the catalog gives them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp80053Baseline']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Sp80053Catalog.model_rebuild()
Sp80053Family.model_rebuild()
Sp80053Control.model_rebuild()
Sp80053ControlEnhancement.model_rebuild()
Sp80053Statement.model_rebuild()
Sp80053StatementItem.model_rebuild()
Sp80053Parameter.model_rebuild()
Sp80053AssessmentObjective.model_rebuild()
Sp80053AssessmentMethod.model_rebuild()
Sp80053Reference.model_rebuild()
Sp80053Baseline.model_rebuild()
