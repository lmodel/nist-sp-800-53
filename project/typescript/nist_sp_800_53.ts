/**
* The one status the catalog marks: withdrawn. A control or enhancement that Revision 5 keeps carries no status.
*/
export enum Sp80053ControlStatus {
    
    /** Revision 5 withdrew the control or enhancement; incorporated_into, moved_to or withdrawal_reason says where it went. */
    WITHDRAWN = "WITHDRAWN",
};
/**
* Who implements a control or enhancement, as NIST's reference data marks it.
*/
export enum Sp80053ImplementationLevel {
    
    /** The organization implements it, through its processes and people. */
    ORGANIZATION = "ORGANIZATION",
    /** The system implements it, through its mechanisms. */
    SYSTEM = "SYSTEM",
};
/**
* How many of a selection's choices the organization picks.
*/
export enum Sp80053SelectionCardinality {
    
    /** Exactly one choice, which the catalog leaves unwritten. */
    ONE = "ONE",
    /** One or more choices, which the publication writes as Selection (one or more). */
    ONE_OR_MORE = "ONE_OR_MORE",
};
/**
* The three assessment methods of SP 800-53A, as its catalog writes them.
*/
export enum Sp80053AssessmentMethodKind {
    
    /** Review, inspect, observe, study or analyze specifications, mechanisms or activities. */
    EXAMINE = "EXAMINE",
    /** Hold discussions with individuals or groups. */
    INTERVIEW = "INTERVIEW",
    /** Exercise mechanisms or activities under specified conditions. */
    TEST = "TEST",
};
/**
* The four control baselines SP 800-53B defines.
*/
export enum Sp80053BaselineLevel {
    
    /** The baseline for a low-impact system. */
    LOW = "LOW",
    /** The baseline for a moderate-impact system. */
    MODERATE = "MODERATE",
    /** The baseline for a high-impact system. */
    HIGH = "HIGH",
    /** The privacy baseline, which applies regardless of impact level. */
    PRIVACY = "PRIVACY",
};


/**
 * One release of the control catalog as a whole: its families, each holding its controls and their enhancements, the baselines that select from them, and the publications the catalog lists.
 */
export interface Sp80053Catalog {
    /** The release of Revision 5 the catalog carries, as NIST numbers it, such as 5.2.0. */
    catalog_release: string,
    /** The twenty control families, in the order SP 800-53 gives them. */
    control_families: Sp80053Family[],
    /** The control baselines of SP 800-53B that select from the catalog. */
    control_baselines?: Sp80053Baseline[],
    /** The publications the catalog's references list, most of which a control cites. */
    catalog_references?: Sp80053Reference[],
}


/**
 * One of the twenty families SP 800-53 sorts its controls into, such as Access Control or Supply Chain Risk Management.
 */
export interface Sp80053Family {
    /** The family's two letters, such as AC for Access Control. */
    family_id: string,
    /** The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline. */
    title: string,
    /** What the family is about, in the words of whoever records it. SP 800-53 gives the Program Management family an overview of its own, and the other families none. */
    description?: string,
    /** The controls of the family. A knowledge bundle relates a control to its family with isPartOf instead. */
    family_controls?: Sp80053Control[],
}


/**
 * A security or privacy control: a safeguard with an identifier, a statement of what it requires, a discussion, parameters the organization defines, related controls, references, the assessment objective and methods SP 800-53A gives it, and its enhancements. A control Revision 5 withdrew keeps its identifier and says where it went.
 */
export interface Sp80053Control {
    /** The control's identifier, such as AC-2. */
    control_identifier: string,
    /** The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline. */
    title: string,
    /** The control statement: what the control or enhancement requires, as one text, a lettered or numbered list of items, or both. */
    control_statement?: Sp80053Statement,
    /** The discussion that follows the statement: context and guidance that help apply the control, which the publication does not require. */
    control_discussion?: string,
    /** The organization-defined parameters the statement leaves to the organization, in the order the catalog gives them. */
    control_parameters?: Sp80053Parameter[],
    /** The controls and enhancements the publication lists as related, by identifier. */
    related_control_ids?: string[],
    /** The publications the control or enhancement cites, by the labels the catalog's references carry, such as SP 800-12 or OMB A-130. */
    control_references?: string[],
    /** The assessment objective SP 800-53A gives the control or enhancement: the determination statements an assessor checks, nested as the statement's items are. */
    assessment_objective?: Sp80053AssessmentObjective,
    /** The assessment methods SP 800-53A gives the control or enhancement, each with the objects it is applied to. */
    assessment_methods?: Sp80053AssessmentMethod[],
    /** The status the catalog gives a control or enhancement that Revision 5 withdrew. An active one carries none. */
    control_status?: string,
    /** For a withdrawn control or enhancement, what it was incorporated into, as the publication states it. */
    incorporated_into?: string[],
    /** For a withdrawn control or enhancement, the control or enhancement it moved to, as the publication states it. */
    moved_to?: string[],
    /** For a withdrawn control or enhancement that the publication neither moved nor incorporated, what it says instead, such as that the enhancement is addressed through tailoring. */
    withdrawal_reason?: string,
    /** Who implements the control or enhancement, as NIST's reference data marks it: the organization, the system, or both. */
    implementation_level?: string,
    /** True where NIST's reference data marks the control or enhancement as one that contributes to assurance; absent otherwise. */
    contributes_to_assurance?: boolean,
    /** The control's enhancements. A knowledge bundle relates an enhancement to its control with isPartOf instead. */
    control_enhancements?: Sp80053ControlEnhancement[],
}


/**
 * A control enhancement: added functionality or strength for a control, with an identifier of its own, which the publication and other documents cite apart from the control. It carries what a control carries, and names the control or enhancement it requires.
 */
export interface Sp80053ControlEnhancement {
    /** The enhancement's identifier, such as AC-2(1). */
    enhancement_id: string,
    /** The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline. */
    title: string,
    /** The control statement: what the control or enhancement requires, as one text, a lettered or numbered list of items, or both. */
    control_statement?: Sp80053Statement,
    /** The discussion that follows the statement: context and guidance that help apply the control, which the publication does not require. */
    control_discussion?: string,
    /** The organization-defined parameters the statement leaves to the organization, in the order the catalog gives them. */
    control_parameters?: Sp80053Parameter[],
    /** The controls and enhancements the publication lists as related, by identifier. */
    related_control_ids?: string[],
    /** The publications the control or enhancement cites, by the labels the catalog's references carry, such as SP 800-12 or OMB A-130. */
    control_references?: string[],
    /** The assessment objective SP 800-53A gives the control or enhancement: the determination statements an assessor checks, nested as the statement's items are. */
    assessment_objective?: Sp80053AssessmentObjective,
    /** The assessment methods SP 800-53A gives the control or enhancement, each with the objects it is applied to. */
    assessment_methods?: Sp80053AssessmentMethod[],
    /** The status the catalog gives a control or enhancement that Revision 5 withdrew. An active one carries none. */
    control_status?: string,
    /** For a withdrawn control or enhancement, what it was incorporated into, as the publication states it. */
    incorporated_into?: string[],
    /** For a withdrawn control or enhancement, the control or enhancement it moved to, as the publication states it. */
    moved_to?: string[],
    /** For a withdrawn control or enhancement that the publication neither moved nor incorporated, what it says instead, such as that the enhancement is addressed through tailoring. */
    withdrawal_reason?: string,
    /** Who implements the control or enhancement, as NIST's reference data marks it: the organization, the system, or both. */
    implementation_level?: string,
    /** True where NIST's reference data marks the control or enhancement as one that contributes to assurance; absent otherwise. */
    contributes_to_assurance?: boolean,
    /** The controls and enhancements that must be implemented for the enhancement to apply, as NIST's catalog links them: its own control, and for SC-42(2) also SC-42(1). */
    required_controls?: string[],
}


/**
 * A control statement: the text of what a control or enhancement requires, and the items it is divided into.
 */
export interface Sp80053Statement {
    /** The lettered or numbered items of the statement, in order, each of which may hold items of its own. */
    statement_items?: Sp80053StatementItem[],
    /** The statement's own text, before any items. A placeholder of the form {{ insert: param, <identifier> }} marks where an organization-defined parameter is inserted. */
    statement_text?: string,
}


/**
 * One lettered or numbered item of a control statement, which may hold items of its own.
 */
export interface Sp80053StatementItem {
    /** The lettered or numbered items of the statement, in order, each of which may hold items of its own. */
    statement_items?: Sp80053StatementItem[],
    /** The item's label as the publication prints it, such as a., 1. or (a). */
    item_label: string,
    /** The item's text, with the same placeholders for parameters as the statement's text. */
    item_text: string,
}


/**
 * An organization-defined parameter: a value the control statement leaves to the organization, either an assignment the organization fills in or a selection from the choices the publication lists. SP 800-53A labels each parameter but the ones that aggregate others, and gives most a guideline.
 */
export interface Sp80053Parameter {
    /** The parameter's identifier in NIST's catalog, such as ac-02_odp.01. */
    parameter_id: string,
    /** The label SP 800-53A gives the parameter, such as AC-02_ODP[01]. A parameter that aggregates several has none. */
    assessment_label?: string,
    /** For an assignment, what the organization defines, such as personnel or roles. */
    parameter_label?: string,
    /** The guidelines that say what a value must settle, such as that the frequency of a review is defined. */
    parameter_guidelines?: string[],
    /** For a selection, the choices the publication lists, in order. */
    selection_choices?: string[],
    /** For a selection, how many choices the organization picks. The catalog marks one or more, and leaves the slot out when one choice is allowed, which is how OSCAL reads an absent how-many. */
    selection_cardinality?: string,
    /** For a parameter that stands for several, the parameters it aggregates, by identifier. */
    aggregated_parameters?: string[],
    /** The identifiers an earlier release of the catalog gave the parameter, such as ac-1_prm_2 for ac-01_odp.03. */
    alternative_identifiers?: string[],
    /** The label SP 800-53 prints where it differs from the one SP 800-53A gives. */
    alternative_label?: string,
}


/**
 * An assessment objective of SP 800-53A: a determination statement an assessor checks, or a heading that groups the determination statements of one item of the control statement.
 */
export interface Sp80053AssessmentObjective {
    /** The label SP 800-53A gives the objective, such as AC-02a.[01]. */
    objective_label: string,
    /** The determination statement, with the same placeholders for parameters as the control statement. A heading has none. */
    objective_text?: string,
    /** The objectives grouped under this one, in order. */
    sub_objectives?: Sp80053AssessmentObjective[],
}


/**
 * One assessment method SP 800-53A gives a control or enhancement, with the objects an assessor selects from: documents and records to examine, people to interview, or mechanisms and activities to test.
 */
export interface Sp80053AssessmentMethod {
    /** Which of the three methods this is. */
    assessment_method: string,
    /** The objects the method is applied to, in the order the publication lists them. */
    assessment_objects: string[],
}


/**
 * A publication the catalog's references list, as they list it: its label, its citation and its address.
 */
export interface Sp80053Reference {
    /** The label the controls cite the publication by, such as SP 800-12. */
    reference_label: string,
    /** The citation, as the catalog prints it. */
    reference_citation?: string,
    /** The address the catalog gives for the publication. */
    reference_url?: string,
}


/**
 * One of the four control baselines SP 800-53B defines: the controls and enhancements selected for systems at the low, moderate or high impact level, or for privacy.
 */
export interface Sp80053Baseline {
    /** Which of the four baselines this is. */
    baseline_level: string,
    /** The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline. */
    title: string,
    /** The controls and enhancements the baseline selects, by identifier, in the order the catalog gives them. */
    baseline_controls: string[],
}



