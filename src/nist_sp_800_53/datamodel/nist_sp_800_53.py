# Auto generated from nist_sp_800_53.yaml by pythongen.py version: 0.0.1
# Schema: nist_sp_800_53
#
# id: https://w3id.org/lmodel/nist-sp-800-53
# description: A LinkML model of the security and privacy controls that NIST Special Publication 800-53, Revision 5, defines at Release 5.2.0: its twenty control families, their controls and control enhancements, each with its statement, discussion, organization-defined parameters, related controls and references; the assessment objectives and methods that SP 800-53A gives each control; and the four control baselines of SP 800-53B.
# license: Apache-2.0

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

from linkml_runtime.linkml_model.types import Boolean, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI

metamodel_version = "1.12.0"
version = "5.2.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_SP_800_53 = CurieNamespace('nist_sp_800_53', 'https://w3id.org/lmodel/nist-sp-800-53/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_SP_800_53


# Types
class Sp80053FamilyIdentifier(String):
    """ The two letters that name one of the twenty control families, such as AC for Access Control. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp80053_family_identifier"
    type_model_uri = NIST_SP_800_53.Sp80053FamilyIdentifier


class Sp80053ControlIdentifier(String):
    """ A control's identifier: its family's letters, a hyphen and the control's number within the family, such as AC-2. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp80053_control_identifier"
    type_model_uri = NIST_SP_800_53.Sp80053ControlIdentifier


class Sp80053EnhancementIdentifier(String):
    """ A control enhancement's identifier: its control's identifier and the enhancement's number in parentheses, such as AC-2(1). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp80053_enhancement_identifier"
    type_model_uri = NIST_SP_800_53.Sp80053EnhancementIdentifier


class Sp80053ControlOrEnhancementIdentifier(String):
    """ The identifier of a control or of a control enhancement, such as AC-2 or AC-2(1), where the publication cites either. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp80053_control_or_enhancement_identifier"
    type_model_uri = NIST_SP_800_53.Sp80053ControlOrEnhancementIdentifier


class Sp80053WithdrawalTarget(String):
    """ Where a withdrawn control or enhancement was incorporated, as the publication names it: a control or enhancement, such as AC-2 or AC-2(1), one item of a control's statement, such as AC-2k, or a whole family, such as SR. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp80053_withdrawal_target"
    type_model_uri = NIST_SP_800_53.Sp80053WithdrawalTarget


class Sp80053ParameterIdentifier(String):
    """ The identifier NIST's catalog gives an organization-defined parameter, in lower case: the zero-padded control identifier, _odp and the parameter's number, such as ac-02_odp.01, or, for a parameter that aggregates several, the control identifier, _prm_ and a number, such as ac-1_prm_1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp80053_parameter_identifier"
    type_model_uri = NIST_SP_800_53.Sp80053ParameterIdentifier


# Class references



@dataclass(repr=False)
class Sp80053Catalog(YAMLRoot):
    """
    One release of the control catalog as a whole: its families, each holding its controls and their enhancements, the
    baselines that select from them, and the publications the catalog lists.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Catalog"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Catalog"
    class_name: ClassVar[str] = "Sp80053Catalog"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053Catalog

    catalog_release: str = None
    control_families: Union[Union[dict, "Sp80053Family"], list[Union[dict, "Sp80053Family"]]] = None
    control_baselines: Optional[Union[Union[dict, "Sp80053Baseline"], list[Union[dict, "Sp80053Baseline"]]]] = empty_list()
    catalog_references: Optional[Union[Union[dict, "Sp80053Reference"], list[Union[dict, "Sp80053Reference"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.catalog_release):
            self.MissingRequiredField("catalog_release")
        if not isinstance(self.catalog_release, str):
            self.catalog_release = str(self.catalog_release)

        if self._is_empty(self.control_families):
            self.MissingRequiredField("control_families")
        self._normalize_inlined_as_list(slot_name="control_families", slot_type=Sp80053Family, key_name="family_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="control_baselines", slot_type=Sp80053Baseline, key_name="baseline_level", keyed=False)

        self._normalize_inlined_as_list(slot_name="catalog_references", slot_type=Sp80053Reference, key_name="reference_label", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053Family(YAMLRoot):
    """
    One of the twenty families SP 800-53 sorts its controls into, such as Access Control or Supply Chain Risk
    Management.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Family"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Family"
    class_name: ClassVar[str] = "Sp80053Family"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053Family

    family_id: Union[str, Sp80053FamilyIdentifier] = None
    title: str = None
    description: Optional[str] = None
    family_controls: Optional[Union[Union[dict, "Sp80053Control"], list[Union[dict, "Sp80053Control"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.family_id):
            self.MissingRequiredField("family_id")
        if not isinstance(self.family_id, Sp80053FamilyIdentifier):
            self.family_id = Sp80053FamilyIdentifier(self.family_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="family_controls", slot_type=Sp80053Control, key_name="control_identifier", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053Control(YAMLRoot):
    """
    A security or privacy control: a safeguard with an identifier, a statement of what it requires, a discussion,
    parameters the organization defines, related controls, references, the assessment objective and methods SP 800-53A
    gives it, and its enhancements. A control Revision 5 withdrew keeps its identifier and says where it went.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Control"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Control"
    class_name: ClassVar[str] = "Sp80053Control"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053Control

    control_identifier: Union[str, Sp80053ControlIdentifier] = None
    title: str = None
    control_statement: Optional[Union[dict, "Sp80053Statement"]] = None
    control_discussion: Optional[str] = None
    control_parameters: Optional[Union[Union[dict, "Sp80053Parameter"], list[Union[dict, "Sp80053Parameter"]]]] = empty_list()
    related_control_ids: Optional[Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]]] = empty_list()
    control_references: Optional[Union[str, list[str]]] = empty_list()
    assessment_objective: Optional[Union[dict, "Sp80053AssessmentObjective"]] = None
    assessment_methods: Optional[Union[Union[dict, "Sp80053AssessmentMethod"], list[Union[dict, "Sp80053AssessmentMethod"]]]] = empty_list()
    control_status: Optional[Union[str, "Sp80053ControlStatus"]] = None
    incorporated_into: Optional[Union[Union[str, Sp80053WithdrawalTarget], list[Union[str, Sp80053WithdrawalTarget]]]] = empty_list()
    moved_to: Optional[Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]]] = empty_list()
    withdrawal_reason: Optional[str] = None
    implementation_level: Optional[Union[Union[str, "Sp80053ImplementationLevel"], list[Union[str, "Sp80053ImplementationLevel"]]]] = empty_list()
    contributes_to_assurance: Optional[Union[bool, Bool]] = None
    control_enhancements: Optional[Union[Union[dict, "Sp80053ControlEnhancement"], list[Union[dict, "Sp80053ControlEnhancement"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.control_identifier):
            self.MissingRequiredField("control_identifier")
        if not isinstance(self.control_identifier, Sp80053ControlIdentifier):
            self.control_identifier = Sp80053ControlIdentifier(self.control_identifier)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.control_statement is not None and not isinstance(self.control_statement, Sp80053Statement):
            self.control_statement = Sp80053Statement(**as_dict(self.control_statement))

        if self.control_discussion is not None and not isinstance(self.control_discussion, str):
            self.control_discussion = str(self.control_discussion)

        self._normalize_inlined_as_list(slot_name="control_parameters", slot_type=Sp80053Parameter, key_name="parameter_id", keyed=False)

        if not isinstance(self.related_control_ids, list):
            self.related_control_ids = [self.related_control_ids] if self.related_control_ids is not None else []
        self.related_control_ids = [v if isinstance(v, Sp80053ControlOrEnhancementIdentifier) else Sp80053ControlOrEnhancementIdentifier(v) for v in self.related_control_ids]

        if not isinstance(self.control_references, list):
            self.control_references = [self.control_references] if self.control_references is not None else []
        self.control_references = [v if isinstance(v, str) else str(v) for v in self.control_references]

        if self.assessment_objective is not None and not isinstance(self.assessment_objective, Sp80053AssessmentObjective):
            self.assessment_objective = Sp80053AssessmentObjective(**as_dict(self.assessment_objective))

        self._normalize_inlined_as_list(slot_name="assessment_methods", slot_type=Sp80053AssessmentMethod, key_name="assessment_method", keyed=False)

        if self.control_status is not None and not isinstance(self.control_status, Sp80053ControlStatus):
            self.control_status = Sp80053ControlStatus(self.control_status)

        if not isinstance(self.incorporated_into, list):
            self.incorporated_into = [self.incorporated_into] if self.incorporated_into is not None else []
        self.incorporated_into = [v if isinstance(v, Sp80053WithdrawalTarget) else Sp80053WithdrawalTarget(v) for v in self.incorporated_into]

        if not isinstance(self.moved_to, list):
            self.moved_to = [self.moved_to] if self.moved_to is not None else []
        self.moved_to = [v if isinstance(v, Sp80053ControlOrEnhancementIdentifier) else Sp80053ControlOrEnhancementIdentifier(v) for v in self.moved_to]

        if self.withdrawal_reason is not None and not isinstance(self.withdrawal_reason, str):
            self.withdrawal_reason = str(self.withdrawal_reason)

        if not isinstance(self.implementation_level, list):
            self.implementation_level = [self.implementation_level] if self.implementation_level is not None else []
        self.implementation_level = [v if isinstance(v, Sp80053ImplementationLevel) else Sp80053ImplementationLevel(v) for v in self.implementation_level]

        if self.contributes_to_assurance is not None and not isinstance(self.contributes_to_assurance, Bool):
            self.contributes_to_assurance = Bool(self.contributes_to_assurance)

        self._normalize_inlined_as_list(slot_name="control_enhancements", slot_type=Sp80053ControlEnhancement, key_name="enhancement_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053ControlEnhancement(YAMLRoot):
    """
    A control enhancement: added functionality or strength for a control, with an identifier of its own, which the
    publication and other documents cite apart from the control. It carries what a control carries, and names the
    control or enhancement it requires.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["ControlEnhancement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:ControlEnhancement"
    class_name: ClassVar[str] = "Sp80053ControlEnhancement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053ControlEnhancement

    enhancement_id: Union[str, Sp80053EnhancementIdentifier] = None
    title: str = None
    control_statement: Optional[Union[dict, "Sp80053Statement"]] = None
    control_discussion: Optional[str] = None
    control_parameters: Optional[Union[Union[dict, "Sp80053Parameter"], list[Union[dict, "Sp80053Parameter"]]]] = empty_list()
    related_control_ids: Optional[Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]]] = empty_list()
    control_references: Optional[Union[str, list[str]]] = empty_list()
    assessment_objective: Optional[Union[dict, "Sp80053AssessmentObjective"]] = None
    assessment_methods: Optional[Union[Union[dict, "Sp80053AssessmentMethod"], list[Union[dict, "Sp80053AssessmentMethod"]]]] = empty_list()
    control_status: Optional[Union[str, "Sp80053ControlStatus"]] = None
    incorporated_into: Optional[Union[Union[str, Sp80053WithdrawalTarget], list[Union[str, Sp80053WithdrawalTarget]]]] = empty_list()
    moved_to: Optional[Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]]] = empty_list()
    withdrawal_reason: Optional[str] = None
    implementation_level: Optional[Union[Union[str, "Sp80053ImplementationLevel"], list[Union[str, "Sp80053ImplementationLevel"]]]] = empty_list()
    contributes_to_assurance: Optional[Union[bool, Bool]] = None
    required_controls: Optional[Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.enhancement_id):
            self.MissingRequiredField("enhancement_id")
        if not isinstance(self.enhancement_id, Sp80053EnhancementIdentifier):
            self.enhancement_id = Sp80053EnhancementIdentifier(self.enhancement_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.control_statement is not None and not isinstance(self.control_statement, Sp80053Statement):
            self.control_statement = Sp80053Statement(**as_dict(self.control_statement))

        if self.control_discussion is not None and not isinstance(self.control_discussion, str):
            self.control_discussion = str(self.control_discussion)

        self._normalize_inlined_as_list(slot_name="control_parameters", slot_type=Sp80053Parameter, key_name="parameter_id", keyed=False)

        if not isinstance(self.related_control_ids, list):
            self.related_control_ids = [self.related_control_ids] if self.related_control_ids is not None else []
        self.related_control_ids = [v if isinstance(v, Sp80053ControlOrEnhancementIdentifier) else Sp80053ControlOrEnhancementIdentifier(v) for v in self.related_control_ids]

        if not isinstance(self.control_references, list):
            self.control_references = [self.control_references] if self.control_references is not None else []
        self.control_references = [v if isinstance(v, str) else str(v) for v in self.control_references]

        if self.assessment_objective is not None and not isinstance(self.assessment_objective, Sp80053AssessmentObjective):
            self.assessment_objective = Sp80053AssessmentObjective(**as_dict(self.assessment_objective))

        self._normalize_inlined_as_list(slot_name="assessment_methods", slot_type=Sp80053AssessmentMethod, key_name="assessment_method", keyed=False)

        if self.control_status is not None and not isinstance(self.control_status, Sp80053ControlStatus):
            self.control_status = Sp80053ControlStatus(self.control_status)

        if not isinstance(self.incorporated_into, list):
            self.incorporated_into = [self.incorporated_into] if self.incorporated_into is not None else []
        self.incorporated_into = [v if isinstance(v, Sp80053WithdrawalTarget) else Sp80053WithdrawalTarget(v) for v in self.incorporated_into]

        if not isinstance(self.moved_to, list):
            self.moved_to = [self.moved_to] if self.moved_to is not None else []
        self.moved_to = [v if isinstance(v, Sp80053ControlOrEnhancementIdentifier) else Sp80053ControlOrEnhancementIdentifier(v) for v in self.moved_to]

        if self.withdrawal_reason is not None and not isinstance(self.withdrawal_reason, str):
            self.withdrawal_reason = str(self.withdrawal_reason)

        if not isinstance(self.implementation_level, list):
            self.implementation_level = [self.implementation_level] if self.implementation_level is not None else []
        self.implementation_level = [v if isinstance(v, Sp80053ImplementationLevel) else Sp80053ImplementationLevel(v) for v in self.implementation_level]

        if self.contributes_to_assurance is not None and not isinstance(self.contributes_to_assurance, Bool):
            self.contributes_to_assurance = Bool(self.contributes_to_assurance)

        if not isinstance(self.required_controls, list):
            self.required_controls = [self.required_controls] if self.required_controls is not None else []
        self.required_controls = [v if isinstance(v, Sp80053ControlOrEnhancementIdentifier) else Sp80053ControlOrEnhancementIdentifier(v) for v in self.required_controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053Statement(YAMLRoot):
    """
    A control statement: the text of what a control or enhancement requires, and the items it is divided into.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Statement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Statement"
    class_name: ClassVar[str] = "Sp80053Statement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053Statement

    statement_items: Optional[Union[Union[dict, "Sp80053StatementItem"], list[Union[dict, "Sp80053StatementItem"]]]] = empty_list()
    statement_text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="statement_items", slot_type=Sp80053StatementItem, key_name="item_label", keyed=False)

        if self.statement_text is not None and not isinstance(self.statement_text, str):
            self.statement_text = str(self.statement_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053StatementItem(YAMLRoot):
    """
    One lettered or numbered item of a control statement, which may hold items of its own.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["StatementItem"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:StatementItem"
    class_name: ClassVar[str] = "Sp80053StatementItem"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053StatementItem

    item_label: str = None
    item_text: str = None
    statement_items: Optional[Union[Union[dict, "Sp80053StatementItem"], list[Union[dict, "Sp80053StatementItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.item_label):
            self.MissingRequiredField("item_label")
        if not isinstance(self.item_label, str):
            self.item_label = str(self.item_label)

        if self._is_empty(self.item_text):
            self.MissingRequiredField("item_text")
        if not isinstance(self.item_text, str):
            self.item_text = str(self.item_text)

        self._normalize_inlined_as_list(slot_name="statement_items", slot_type=Sp80053StatementItem, key_name="item_label", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053Parameter(YAMLRoot):
    """
    An organization-defined parameter: a value the control statement leaves to the organization, either an assignment
    the organization fills in or a selection from the choices the publication lists. SP 800-53A labels each parameter
    but the ones that aggregate others, and gives most a guideline.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Parameter"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Parameter"
    class_name: ClassVar[str] = "Sp80053Parameter"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053Parameter

    parameter_id: Union[str, Sp80053ParameterIdentifier] = None
    assessment_label: Optional[str] = None
    parameter_label: Optional[str] = None
    parameter_guidelines: Optional[Union[str, list[str]]] = empty_list()
    selection_choices: Optional[Union[str, list[str]]] = empty_list()
    selection_cardinality: Optional[Union[str, "Sp80053SelectionCardinality"]] = None
    aggregated_parameters: Optional[Union[Union[str, Sp80053ParameterIdentifier], list[Union[str, Sp80053ParameterIdentifier]]]] = empty_list()
    alternative_identifiers: Optional[Union[Union[str, Sp80053ParameterIdentifier], list[Union[str, Sp80053ParameterIdentifier]]]] = empty_list()
    alternative_label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.parameter_id):
            self.MissingRequiredField("parameter_id")
        if not isinstance(self.parameter_id, Sp80053ParameterIdentifier):
            self.parameter_id = Sp80053ParameterIdentifier(self.parameter_id)

        if self.assessment_label is not None and not isinstance(self.assessment_label, str):
            self.assessment_label = str(self.assessment_label)

        if self.parameter_label is not None and not isinstance(self.parameter_label, str):
            self.parameter_label = str(self.parameter_label)

        if not isinstance(self.parameter_guidelines, list):
            self.parameter_guidelines = [self.parameter_guidelines] if self.parameter_guidelines is not None else []
        self.parameter_guidelines = [v if isinstance(v, str) else str(v) for v in self.parameter_guidelines]

        if not isinstance(self.selection_choices, list):
            self.selection_choices = [self.selection_choices] if self.selection_choices is not None else []
        self.selection_choices = [v if isinstance(v, str) else str(v) for v in self.selection_choices]

        if self.selection_cardinality is not None and not isinstance(self.selection_cardinality, Sp80053SelectionCardinality):
            self.selection_cardinality = Sp80053SelectionCardinality(self.selection_cardinality)

        if not isinstance(self.aggregated_parameters, list):
            self.aggregated_parameters = [self.aggregated_parameters] if self.aggregated_parameters is not None else []
        self.aggregated_parameters = [v if isinstance(v, Sp80053ParameterIdentifier) else Sp80053ParameterIdentifier(v) for v in self.aggregated_parameters]

        if not isinstance(self.alternative_identifiers, list):
            self.alternative_identifiers = [self.alternative_identifiers] if self.alternative_identifiers is not None else []
        self.alternative_identifiers = [v if isinstance(v, Sp80053ParameterIdentifier) else Sp80053ParameterIdentifier(v) for v in self.alternative_identifiers]

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053AssessmentObjective(YAMLRoot):
    """
    An assessment objective of SP 800-53A: a determination statement an assessor checks, or a heading that groups the
    determination statements of one item of the control statement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["AssessmentObjective"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:AssessmentObjective"
    class_name: ClassVar[str] = "Sp80053AssessmentObjective"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053AssessmentObjective

    objective_label: str = None
    objective_text: Optional[str] = None
    sub_objectives: Optional[Union[Union[dict, "Sp80053AssessmentObjective"], list[Union[dict, "Sp80053AssessmentObjective"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.objective_label):
            self.MissingRequiredField("objective_label")
        if not isinstance(self.objective_label, str):
            self.objective_label = str(self.objective_label)

        if self.objective_text is not None and not isinstance(self.objective_text, str):
            self.objective_text = str(self.objective_text)

        self._normalize_inlined_as_list(slot_name="sub_objectives", slot_type=Sp80053AssessmentObjective, key_name="objective_label", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053AssessmentMethod(YAMLRoot):
    """
    One assessment method SP 800-53A gives a control or enhancement, with the objects an assessor selects from:
    documents and records to examine, people to interview, or mechanisms and activities to test.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["AssessmentMethod"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:AssessmentMethod"
    class_name: ClassVar[str] = "Sp80053AssessmentMethod"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053AssessmentMethod

    assessment_method: Union[str, "Sp80053AssessmentMethodKind"] = None
    assessment_objects: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assessment_method):
            self.MissingRequiredField("assessment_method")
        if not isinstance(self.assessment_method, Sp80053AssessmentMethodKind):
            self.assessment_method = Sp80053AssessmentMethodKind(self.assessment_method)

        if self._is_empty(self.assessment_objects):
            self.MissingRequiredField("assessment_objects")
        if not isinstance(self.assessment_objects, list):
            self.assessment_objects = [self.assessment_objects] if self.assessment_objects is not None else []
        self.assessment_objects = [v if isinstance(v, str) else str(v) for v in self.assessment_objects]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053Reference(YAMLRoot):
    """
    A publication the catalog's references list, as they list it: its label, its citation and its address.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Reference"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Reference"
    class_name: ClassVar[str] = "Sp80053Reference"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053Reference

    reference_label: str = None
    reference_citation: Optional[str] = None
    reference_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reference_label):
            self.MissingRequiredField("reference_label")
        if not isinstance(self.reference_label, str):
            self.reference_label = str(self.reference_label)

        if self.reference_citation is not None and not isinstance(self.reference_citation, str):
            self.reference_citation = str(self.reference_citation)

        if self.reference_url is not None and not isinstance(self.reference_url, URI):
            self.reference_url = URI(self.reference_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp80053Baseline(YAMLRoot):
    """
    One of the four control baselines SP 800-53B defines: the controls and enhancements selected for systems at the
    low, moderate or high impact level, or for privacy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_53["Baseline"]
    class_class_curie: ClassVar[str] = "nist_sp_800_53:Baseline"
    class_name: ClassVar[str] = "Sp80053Baseline"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_53.Sp80053Baseline

    baseline_level: Union[str, "Sp80053BaselineLevel"] = None
    title: str = None
    baseline_controls: Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.baseline_level):
            self.MissingRequiredField("baseline_level")
        if not isinstance(self.baseline_level, Sp80053BaselineLevel):
            self.baseline_level = Sp80053BaselineLevel(self.baseline_level)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.baseline_controls):
            self.MissingRequiredField("baseline_controls")
        if not isinstance(self.baseline_controls, list):
            self.baseline_controls = [self.baseline_controls] if self.baseline_controls is not None else []
        self.baseline_controls = [v if isinstance(v, Sp80053ControlOrEnhancementIdentifier) else Sp80053ControlOrEnhancementIdentifier(v) for v in self.baseline_controls]

        super().__post_init__(**kwargs)


# Enumerations
class Sp80053ControlStatus(EnumDefinitionImpl):
    """
    The one status the catalog marks: withdrawn. A control or enhancement that Revision 5 keeps carries no status.
    """
    WITHDRAWN = PermissibleValue(
        text="WITHDRAWN",
        description="""Revision 5 withdrew the control or enhancement; incorporated_into, moved_to or withdrawal_reason says where it went.""")

    _defn = EnumDefinition(
        name="Sp80053ControlStatus",
        description="""The one status the catalog marks: withdrawn. A control or enhancement that Revision 5 keeps carries no status.""",
    )

class Sp80053ImplementationLevel(EnumDefinitionImpl):
    """
    Who implements a control or enhancement, as NIST's reference data marks it.
    """
    ORGANIZATION = PermissibleValue(
        text="ORGANIZATION",
        description="The organization implements it, through its processes and people.")
    SYSTEM = PermissibleValue(
        text="SYSTEM",
        description="The system implements it, through its mechanisms.")

    _defn = EnumDefinition(
        name="Sp80053ImplementationLevel",
        description="Who implements a control or enhancement, as NIST's reference data marks it.",
    )

class Sp80053SelectionCardinality(EnumDefinitionImpl):
    """
    How many of a selection's choices the organization picks.
    """
    ONE = PermissibleValue(
        text="ONE",
        description="Exactly one choice, which the catalog leaves unwritten.")
    ONE_OR_MORE = PermissibleValue(
        text="ONE_OR_MORE",
        description="One or more choices, which the publication writes as Selection (one or more).")

    _defn = EnumDefinition(
        name="Sp80053SelectionCardinality",
        description="How many of a selection's choices the organization picks.",
    )

class Sp80053AssessmentMethodKind(EnumDefinitionImpl):
    """
    The three assessment methods of SP 800-53A, as its catalog writes them.
    """
    EXAMINE = PermissibleValue(
        text="EXAMINE",
        description="Review, inspect, observe, study or analyze specifications, mechanisms or activities.")
    INTERVIEW = PermissibleValue(
        text="INTERVIEW",
        description="Hold discussions with individuals or groups.")
    TEST = PermissibleValue(
        text="TEST",
        description="Exercise mechanisms or activities under specified conditions.")

    _defn = EnumDefinition(
        name="Sp80053AssessmentMethodKind",
        description="The three assessment methods of SP 800-53A, as its catalog writes them.",
    )

class Sp80053BaselineLevel(EnumDefinitionImpl):
    """
    The four control baselines SP 800-53B defines.
    """
    LOW = PermissibleValue(
        text="LOW",
        description="The baseline for a low-impact system.")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="The baseline for a moderate-impact system.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="The baseline for a high-impact system.")
    PRIVACY = PermissibleValue(
        text="PRIVACY",
        description="The privacy baseline, which applies regardless of impact level.")

    _defn = EnumDefinition(
        name="Sp80053BaselineLevel",
        description="The four control baselines SP 800-53B defines.",
    )

# Slots
class slots:
    pass

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_SP_800_53.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_SP_800_53.description, domain=None, range=Optional[str])

slots.family_id = Slot(uri=NIST_SP_800_53.family_id, name="family_id", curie=NIST_SP_800_53.curie('family_id'),
                   model_uri=NIST_SP_800_53.family_id, domain=None, range=Union[str, Sp80053FamilyIdentifier])

slots.control_identifier = Slot(uri=NIST_SP_800_53.control_identifier, name="control_identifier", curie=NIST_SP_800_53.curie('control_identifier'),
                   model_uri=NIST_SP_800_53.control_identifier, domain=None, range=Union[str, Sp80053ControlIdentifier])

slots.enhancement_id = Slot(uri=NIST_SP_800_53.enhancement_id, name="enhancement_id", curie=NIST_SP_800_53.curie('enhancement_id'),
                   model_uri=NIST_SP_800_53.enhancement_id, domain=None, range=Union[str, Sp80053EnhancementIdentifier])

slots.baseline_level = Slot(uri=NIST_SP_800_53.baseline_level, name="baseline_level", curie=NIST_SP_800_53.curie('baseline_level'),
                   model_uri=NIST_SP_800_53.baseline_level, domain=None, range=Union[str, "Sp80053BaselineLevel"])

slots.control_statement = Slot(uri=NIST_SP_800_53.control_statement, name="control_statement", curie=NIST_SP_800_53.curie('control_statement'),
                   model_uri=NIST_SP_800_53.control_statement, domain=None, range=Optional[Union[dict, Sp80053Statement]])

slots.control_discussion = Slot(uri=NIST_SP_800_53.control_discussion, name="control_discussion", curie=NIST_SP_800_53.curie('control_discussion'),
                   model_uri=NIST_SP_800_53.control_discussion, domain=None, range=Optional[str])

slots.control_parameters = Slot(uri=NIST_SP_800_53.control_parameters, name="control_parameters", curie=NIST_SP_800_53.curie('control_parameters'),
                   model_uri=NIST_SP_800_53.control_parameters, domain=None, range=Optional[Union[Union[dict, Sp80053Parameter], list[Union[dict, Sp80053Parameter]]]])

slots.related_control_ids = Slot(uri=NIST_SP_800_53.related_control_ids, name="related_control_ids", curie=NIST_SP_800_53.curie('related_control_ids'),
                   model_uri=NIST_SP_800_53.related_control_ids, domain=None, range=Optional[Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]]])

slots.control_references = Slot(uri=NIST_SP_800_53.control_references, name="control_references", curie=NIST_SP_800_53.curie('control_references'),
                   model_uri=NIST_SP_800_53.control_references, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^\s*\S'))

slots.assessment_objective = Slot(uri=NIST_SP_800_53.assessment_objective, name="assessment_objective", curie=NIST_SP_800_53.curie('assessment_objective'),
                   model_uri=NIST_SP_800_53.assessment_objective, domain=None, range=Optional[Union[dict, Sp80053AssessmentObjective]])

slots.assessment_methods = Slot(uri=NIST_SP_800_53.assessment_methods, name="assessment_methods", curie=NIST_SP_800_53.curie('assessment_methods'),
                   model_uri=NIST_SP_800_53.assessment_methods, domain=None, range=Optional[Union[Union[dict, Sp80053AssessmentMethod], list[Union[dict, Sp80053AssessmentMethod]]]])

slots.control_status = Slot(uri=NIST_SP_800_53.control_status, name="control_status", curie=NIST_SP_800_53.curie('control_status'),
                   model_uri=NIST_SP_800_53.control_status, domain=None, range=Optional[Union[str, "Sp80053ControlStatus"]])

slots.incorporated_into = Slot(uri=NIST_SP_800_53.incorporated_into, name="incorporated_into", curie=NIST_SP_800_53.curie('incorporated_into'),
                   model_uri=NIST_SP_800_53.incorporated_into, domain=None, range=Optional[Union[Union[str, Sp80053WithdrawalTarget], list[Union[str, Sp80053WithdrawalTarget]]]])

slots.moved_to = Slot(uri=NIST_SP_800_53.moved_to, name="moved_to", curie=NIST_SP_800_53.curie('moved_to'),
                   model_uri=NIST_SP_800_53.moved_to, domain=None, range=Optional[Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]]])

slots.withdrawal_reason = Slot(uri=NIST_SP_800_53.withdrawal_reason, name="withdrawal_reason", curie=NIST_SP_800_53.curie('withdrawal_reason'),
                   model_uri=NIST_SP_800_53.withdrawal_reason, domain=None, range=Optional[str])

slots.implementation_level = Slot(uri=NIST_SP_800_53.implementation_level, name="implementation_level", curie=NIST_SP_800_53.curie('implementation_level'),
                   model_uri=NIST_SP_800_53.implementation_level, domain=None, range=Optional[Union[Union[str, "Sp80053ImplementationLevel"], list[Union[str, "Sp80053ImplementationLevel"]]]])

slots.contributes_to_assurance = Slot(uri=NIST_SP_800_53.contributes_to_assurance, name="contributes_to_assurance", curie=NIST_SP_800_53.curie('contributes_to_assurance'),
                   model_uri=NIST_SP_800_53.contributes_to_assurance, domain=None, range=Optional[Union[bool, Bool]])

slots.statement_items = Slot(uri=NIST_SP_800_53.statement_items, name="statement_items", curie=NIST_SP_800_53.curie('statement_items'),
                   model_uri=NIST_SP_800_53.statement_items, domain=None, range=Optional[Union[Union[dict, Sp80053StatementItem], list[Union[dict, Sp80053StatementItem]]]])

slots.sp80053Catalog__catalog_release = Slot(uri=NIST_SP_800_53.catalog_release, name="sp80053Catalog__catalog_release", curie=NIST_SP_800_53.curie('catalog_release'),
                   model_uri=NIST_SP_800_53.sp80053Catalog__catalog_release, domain=None, range=str,
                   pattern=re.compile(r'^[0-9]+\.[0-9]+\.[0-9]+$'))

slots.sp80053Catalog__control_families = Slot(uri=NIST_SP_800_53.control_families, name="sp80053Catalog__control_families", curie=NIST_SP_800_53.curie('control_families'),
                   model_uri=NIST_SP_800_53.sp80053Catalog__control_families, domain=None, range=Union[Union[dict, Sp80053Family], list[Union[dict, Sp80053Family]]])

slots.sp80053Catalog__control_baselines = Slot(uri=NIST_SP_800_53.control_baselines, name="sp80053Catalog__control_baselines", curie=NIST_SP_800_53.curie('control_baselines'),
                   model_uri=NIST_SP_800_53.sp80053Catalog__control_baselines, domain=None, range=Optional[Union[Union[dict, Sp80053Baseline], list[Union[dict, Sp80053Baseline]]]])

slots.sp80053Catalog__catalog_references = Slot(uri=NIST_SP_800_53.catalog_references, name="sp80053Catalog__catalog_references", curie=NIST_SP_800_53.curie('catalog_references'),
                   model_uri=NIST_SP_800_53.sp80053Catalog__catalog_references, domain=None, range=Optional[Union[Union[dict, Sp80053Reference], list[Union[dict, Sp80053Reference]]]])

slots.sp80053Family__family_controls = Slot(uri=NIST_SP_800_53.family_controls, name="sp80053Family__family_controls", curie=NIST_SP_800_53.curie('family_controls'),
                   model_uri=NIST_SP_800_53.sp80053Family__family_controls, domain=None, range=Optional[Union[Union[dict, Sp80053Control], list[Union[dict, Sp80053Control]]]])

slots.sp80053Control__control_enhancements = Slot(uri=NIST_SP_800_53.control_enhancements, name="sp80053Control__control_enhancements", curie=NIST_SP_800_53.curie('control_enhancements'),
                   model_uri=NIST_SP_800_53.sp80053Control__control_enhancements, domain=None, range=Optional[Union[Union[dict, Sp80053ControlEnhancement], list[Union[dict, Sp80053ControlEnhancement]]]])

slots.sp80053ControlEnhancement__required_controls = Slot(uri=NIST_SP_800_53.required_controls, name="sp80053ControlEnhancement__required_controls", curie=NIST_SP_800_53.curie('required_controls'),
                   model_uri=NIST_SP_800_53.sp80053ControlEnhancement__required_controls, domain=None, range=Optional[Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]]])

slots.sp80053Statement__statement_text = Slot(uri=NIST_SP_800_53.statement_text, name="sp80053Statement__statement_text", curie=NIST_SP_800_53.curie('statement_text'),
                   model_uri=NIST_SP_800_53.sp80053Statement__statement_text, domain=None, range=Optional[str])

slots.sp80053StatementItem__item_label = Slot(uri=NIST_SP_800_53.item_label, name="sp80053StatementItem__item_label", curie=NIST_SP_800_53.curie('item_label'),
                   model_uri=NIST_SP_800_53.sp80053StatementItem__item_label, domain=None, range=str,
                   pattern=re.compile(r'^(([a-z]|[1-9][0-9]*)\.|\(([a-z]|[1-9][0-9]*)\))$'))

slots.sp80053StatementItem__item_text = Slot(uri=NIST_SP_800_53.item_text, name="sp80053StatementItem__item_text", curie=NIST_SP_800_53.curie('item_text'),
                   model_uri=NIST_SP_800_53.sp80053StatementItem__item_text, domain=None, range=str)

slots.sp80053Parameter__parameter_id = Slot(uri=NIST_SP_800_53.parameter_id, name="sp80053Parameter__parameter_id", curie=NIST_SP_800_53.curie('parameter_id'),
                   model_uri=NIST_SP_800_53.sp80053Parameter__parameter_id, domain=None, range=Union[str, Sp80053ParameterIdentifier])

slots.sp80053Parameter__assessment_label = Slot(uri=NIST_SP_800_53.assessment_label, name="sp80053Parameter__assessment_label", curie=NIST_SP_800_53.curie('assessment_label'),
                   model_uri=NIST_SP_800_53.sp80053Parameter__assessment_label, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)-[0-9]{2}(\([0-9]{2}\)|\.[0-9]{2})?_ODP(\[[0-9]{2}\])?$'))

slots.sp80053Parameter__parameter_label = Slot(uri=NIST_SP_800_53.parameter_label, name="sp80053Parameter__parameter_label", curie=NIST_SP_800_53.curie('parameter_label'),
                   model_uri=NIST_SP_800_53.sp80053Parameter__parameter_label, domain=None, range=Optional[str])

slots.sp80053Parameter__parameter_guidelines = Slot(uri=NIST_SP_800_53.parameter_guidelines, name="sp80053Parameter__parameter_guidelines", curie=NIST_SP_800_53.curie('parameter_guidelines'),
                   model_uri=NIST_SP_800_53.sp80053Parameter__parameter_guidelines, domain=None, range=Optional[Union[str, list[str]]])

slots.sp80053Parameter__selection_choices = Slot(uri=NIST_SP_800_53.selection_choices, name="sp80053Parameter__selection_choices", curie=NIST_SP_800_53.curie('selection_choices'),
                   model_uri=NIST_SP_800_53.sp80053Parameter__selection_choices, domain=None, range=Optional[Union[str, list[str]]])

slots.sp80053Parameter__selection_cardinality = Slot(uri=NIST_SP_800_53.selection_cardinality, name="sp80053Parameter__selection_cardinality", curie=NIST_SP_800_53.curie('selection_cardinality'),
                   model_uri=NIST_SP_800_53.sp80053Parameter__selection_cardinality, domain=None, range=Optional[Union[str, "Sp80053SelectionCardinality"]])

slots.sp80053Parameter__aggregated_parameters = Slot(uri=NIST_SP_800_53.aggregated_parameters, name="sp80053Parameter__aggregated_parameters", curie=NIST_SP_800_53.curie('aggregated_parameters'),
                   model_uri=NIST_SP_800_53.sp80053Parameter__aggregated_parameters, domain=None, range=Optional[Union[Union[str, Sp80053ParameterIdentifier], list[Union[str, Sp80053ParameterIdentifier]]]])

slots.sp80053Parameter__alternative_identifiers = Slot(uri=NIST_SP_800_53.alternative_identifiers, name="sp80053Parameter__alternative_identifiers", curie=NIST_SP_800_53.curie('alternative_identifiers'),
                   model_uri=NIST_SP_800_53.sp80053Parameter__alternative_identifiers, domain=None, range=Optional[Union[Union[str, Sp80053ParameterIdentifier], list[Union[str, Sp80053ParameterIdentifier]]]])

slots.sp80053Parameter__alternative_label = Slot(uri=NIST_SP_800_53.alternative_label, name="sp80053Parameter__alternative_label", curie=NIST_SP_800_53.curie('alternative_label'),
                   model_uri=NIST_SP_800_53.sp80053Parameter__alternative_label, domain=None, range=Optional[str])

slots.sp80053AssessmentObjective__objective_label = Slot(uri=NIST_SP_800_53.objective_label, name="sp80053AssessmentObjective__objective_label", curie=NIST_SP_800_53.curie('objective_label'),
                   model_uri=NIST_SP_800_53.sp80053AssessmentObjective__objective_label, domain=None, range=str,
                   pattern=re.compile(r'^(AC|AT|AU|CA|CM|CP|IA|IR|MA|MP|PE|PL|PM|PS|PT|RA|SA|SC|SI|SR)-[0-9]{2}(\([0-9]{2}\))?([a-z]\.([0-9]{2})?)?(\([a-z]\)(\([0-9]{2}\))?)?(\[[0-9]{2}\])*$'))

slots.sp80053AssessmentObjective__objective_text = Slot(uri=NIST_SP_800_53.objective_text, name="sp80053AssessmentObjective__objective_text", curie=NIST_SP_800_53.curie('objective_text'),
                   model_uri=NIST_SP_800_53.sp80053AssessmentObjective__objective_text, domain=None, range=Optional[str])

slots.sp80053AssessmentObjective__sub_objectives = Slot(uri=NIST_SP_800_53.sub_objectives, name="sp80053AssessmentObjective__sub_objectives", curie=NIST_SP_800_53.curie('sub_objectives'),
                   model_uri=NIST_SP_800_53.sp80053AssessmentObjective__sub_objectives, domain=None, range=Optional[Union[Union[dict, Sp80053AssessmentObjective], list[Union[dict, Sp80053AssessmentObjective]]]])

slots.sp80053AssessmentMethod__assessment_method = Slot(uri=NIST_SP_800_53.assessment_method, name="sp80053AssessmentMethod__assessment_method", curie=NIST_SP_800_53.curie('assessment_method'),
                   model_uri=NIST_SP_800_53.sp80053AssessmentMethod__assessment_method, domain=None, range=Union[str, "Sp80053AssessmentMethodKind"])

slots.sp80053AssessmentMethod__assessment_objects = Slot(uri=NIST_SP_800_53.assessment_objects, name="sp80053AssessmentMethod__assessment_objects", curie=NIST_SP_800_53.curie('assessment_objects'),
                   model_uri=NIST_SP_800_53.sp80053AssessmentMethod__assessment_objects, domain=None, range=Union[str, list[str]],
                   pattern=re.compile(r'^\s*\S'))

slots.sp80053Reference__reference_label = Slot(uri=NIST_SP_800_53.reference_label, name="sp80053Reference__reference_label", curie=NIST_SP_800_53.curie('reference_label'),
                   model_uri=NIST_SP_800_53.sp80053Reference__reference_label, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.sp80053Reference__reference_citation = Slot(uri=NIST_SP_800_53.reference_citation, name="sp80053Reference__reference_citation", curie=NIST_SP_800_53.curie('reference_citation'),
                   model_uri=NIST_SP_800_53.sp80053Reference__reference_citation, domain=None, range=Optional[str])

slots.sp80053Reference__reference_url = Slot(uri=NIST_SP_800_53.reference_url, name="sp80053Reference__reference_url", curie=NIST_SP_800_53.curie('reference_url'),
                   model_uri=NIST_SP_800_53.sp80053Reference__reference_url, domain=None, range=Optional[Union[str, URI]])

slots.sp80053Baseline__baseline_controls = Slot(uri=NIST_SP_800_53.baseline_controls, name="sp80053Baseline__baseline_controls", curie=NIST_SP_800_53.curie('baseline_controls'),
                   model_uri=NIST_SP_800_53.sp80053Baseline__baseline_controls, domain=None, range=Union[Union[str, Sp80053ControlOrEnhancementIdentifier], list[Union[str, Sp80053ControlOrEnhancementIdentifier]]])

slots.Sp80053Family_title = Slot(uri=SCHEMA.name, name="Sp80053Family_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_SP_800_53.Sp80053Family_title, domain=Sp80053Family, range=str)

slots.Sp80053Control_title = Slot(uri=SCHEMA.name, name="Sp80053Control_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_SP_800_53.Sp80053Control_title, domain=Sp80053Control, range=str)

slots.Sp80053ControlEnhancement_title = Slot(uri=SCHEMA.name, name="Sp80053ControlEnhancement_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_SP_800_53.Sp80053ControlEnhancement_title, domain=Sp80053ControlEnhancement, range=str)

slots.Sp80053Baseline_title = Slot(uri=SCHEMA.name, name="Sp80053Baseline_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_SP_800_53.Sp80053Baseline_title, domain=Sp80053Baseline, range=str)
