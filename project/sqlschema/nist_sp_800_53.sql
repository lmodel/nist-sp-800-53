-- # Class: Sp80053Catalog Description: One release of the control catalog as a whole: its families, each holding its controls and their enhancements, the baselines that select from them, and the publications the catalog lists.
--     * Slot: id
--     * Slot: catalog_release Description: The release of Revision 5 the catalog carries, as NIST numbers it, such as 5.2.0.
-- # Class: Sp80053Family Description: One of the twenty families SP 800-53 sorts its controls into, such as Access Control or Supply Chain Risk Management.
--     * Slot: id
--     * Slot: title Description: The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline.
--     * Slot: description Description: What the family is about, in the words of whoever records it. SP 800-53 gives the Program Management family an overview of its own, and the other families none.
--     * Slot: family_id Description: The family's two letters, such as AC for Access Control.
--     * Slot: Sp80053Catalog_id Description: Autocreated FK slot
-- # Class: Sp80053Control Description: A security or privacy control: a safeguard with an identifier, a statement of what it requires, a discussion, parameters the organization defines, related controls, references, the assessment objective and methods SP 800-53A gives it, and its enhancements. A control Revision 5 withdrew keeps its identifier and says where it went.
--     * Slot: id
--     * Slot: title Description: The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline.
--     * Slot: control_discussion Description: The discussion that follows the statement: context and guidance that help apply the control, which the publication does not require.
--     * Slot: control_status Description: The status the catalog gives a control or enhancement that Revision 5 withdrew. An active one carries none.
--     * Slot: withdrawal_reason Description: For a withdrawn control or enhancement that the publication neither moved nor incorporated, what it says instead, such as that the enhancement is addressed through tailoring.
--     * Slot: contributes_to_assurance Description: True where NIST's reference data marks the control or enhancement as one that contributes to assurance; absent otherwise.
--     * Slot: control_identifier Description: The control's identifier, such as AC-2.
--     * Slot: Sp80053Family_id Description: Autocreated FK slot
--     * Slot: control_statement_id Description: The control statement: what the control or enhancement requires, as one text, a lettered or numbered list of items, or both.
--     * Slot: assessment_objective_id Description: The assessment objective SP 800-53A gives the control or enhancement: the determination statements an assessor checks, nested as the statement's items are.
-- # Class: Sp80053ControlEnhancement Description: A control enhancement: added functionality or strength for a control, with an identifier of its own, which the publication and other documents cite apart from the control. It carries what a control carries, and names the control or enhancement it requires.
--     * Slot: id
--     * Slot: title Description: The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline.
--     * Slot: control_discussion Description: The discussion that follows the statement: context and guidance that help apply the control, which the publication does not require.
--     * Slot: control_status Description: The status the catalog gives a control or enhancement that Revision 5 withdrew. An active one carries none.
--     * Slot: withdrawal_reason Description: For a withdrawn control or enhancement that the publication neither moved nor incorporated, what it says instead, such as that the enhancement is addressed through tailoring.
--     * Slot: contributes_to_assurance Description: True where NIST's reference data marks the control or enhancement as one that contributes to assurance; absent otherwise.
--     * Slot: enhancement_id Description: The enhancement's identifier, such as AC-2(1).
--     * Slot: Sp80053Control_id Description: Autocreated FK slot
--     * Slot: control_statement_id Description: The control statement: what the control or enhancement requires, as one text, a lettered or numbered list of items, or both.
--     * Slot: assessment_objective_id Description: The assessment objective SP 800-53A gives the control or enhancement: the determination statements an assessor checks, nested as the statement's items are.
-- # Class: Sp80053Statement Description: A control statement: the text of what a control or enhancement requires, and the items it is divided into.
--     * Slot: id
--     * Slot: statement_text Description: The statement's own text, before any items. A placeholder of the form {{ insert: param, <identifier> }} marks where an organization-defined parameter is inserted.
-- # Class: Sp80053StatementItem Description: One lettered or numbered item of a control statement, which may hold items of its own.
--     * Slot: id
--     * Slot: item_label Description: The item's label as the publication prints it, such as a., 1. or (a).
--     * Slot: item_text Description: The item's text, with the same placeholders for parameters as the statement's text.
--     * Slot: Sp80053Statement_id Description: Autocreated FK slot
--     * Slot: Sp80053StatementItem_id Description: Autocreated FK slot
-- # Class: Sp80053Parameter Description: An organization-defined parameter: a value the control statement leaves to the organization, either an assignment the organization fills in or a selection from the choices the publication lists. SP 800-53A labels each parameter but the ones that aggregate others, and gives most a guideline.
--     * Slot: id
--     * Slot: parameter_id Description: The parameter's identifier in NIST's catalog, such as ac-02_odp.01.
--     * Slot: assessment_label Description: The label SP 800-53A gives the parameter, such as AC-02_ODP[01]. A parameter that aggregates several has none.
--     * Slot: parameter_label Description: For an assignment, what the organization defines, such as personnel or roles.
--     * Slot: selection_cardinality Description: For a selection, how many choices the organization picks. The catalog marks one or more, and leaves the slot out when one choice is allowed, which is how OSCAL reads an absent how-many.
--     * Slot: alternative_label Description: The label SP 800-53 prints where it differs from the one SP 800-53A gives.
--     * Slot: Sp80053Control_id Description: Autocreated FK slot
--     * Slot: Sp80053ControlEnhancement_id Description: Autocreated FK slot
-- # Class: Sp80053AssessmentObjective Description: An assessment objective of SP 800-53A: a determination statement an assessor checks, or a heading that groups the determination statements of one item of the control statement.
--     * Slot: id
--     * Slot: objective_label Description: The label SP 800-53A gives the objective, such as AC-02a.[01].
--     * Slot: objective_text Description: The determination statement, with the same placeholders for parameters as the control statement. A heading has none.
--     * Slot: Sp80053AssessmentObjective_id Description: Autocreated FK slot
-- # Class: Sp80053AssessmentMethod Description: One assessment method SP 800-53A gives a control or enhancement, with the objects an assessor selects from: documents and records to examine, people to interview, or mechanisms and activities to test.
--     * Slot: id
--     * Slot: assessment_method Description: Which of the three methods this is.
--     * Slot: Sp80053Control_id Description: Autocreated FK slot
--     * Slot: Sp80053ControlEnhancement_id Description: Autocreated FK slot
-- # Class: Sp80053Reference Description: A publication the catalog's references list, as they list it: its label, its citation and its address.
--     * Slot: id
--     * Slot: reference_label Description: The label the controls cite the publication by, such as SP 800-12.
--     * Slot: reference_citation Description: The citation, as the catalog prints it.
--     * Slot: reference_url Description: The address the catalog gives for the publication.
--     * Slot: Sp80053Catalog_id Description: Autocreated FK slot
-- # Class: Sp80053Baseline Description: One of the four control baselines SP 800-53B defines: the controls and enhancements selected for systems at the low, moderate or high impact level, or for privacy.
--     * Slot: id
--     * Slot: title Description: The name SP 800-53 gives the family, control or control enhancement, or the title NIST's profile gives the baseline.
--     * Slot: baseline_level Description: Which of the four baselines this is.
--     * Slot: Sp80053Catalog_id Description: Autocreated FK slot
-- # Class: Sp80053Control_related_control_ids
--     * Slot: Sp80053Control_id Description: Autocreated FK slot
--     * Slot: related_control_ids Description: The controls and enhancements the publication lists as related, by identifier.
-- # Class: Sp80053Control_control_references
--     * Slot: Sp80053Control_id Description: Autocreated FK slot
--     * Slot: control_references Description: The publications the control or enhancement cites, by the labels the catalog's references carry, such as SP 800-12 or OMB A-130.
-- # Class: Sp80053Control_incorporated_into
--     * Slot: Sp80053Control_id Description: Autocreated FK slot
--     * Slot: incorporated_into Description: For a withdrawn control or enhancement, what it was incorporated into, as the publication states it.
-- # Class: Sp80053Control_moved_to
--     * Slot: Sp80053Control_id Description: Autocreated FK slot
--     * Slot: moved_to Description: For a withdrawn control or enhancement, the control or enhancement it moved to, as the publication states it.
-- # Class: Sp80053Control_implementation_level
--     * Slot: Sp80053Control_id Description: Autocreated FK slot
--     * Slot: implementation_level Description: Who implements the control or enhancement, as NIST's reference data marks it: the organization, the system, or both.
-- # Class: Sp80053ControlEnhancement_related_control_ids
--     * Slot: Sp80053ControlEnhancement_id Description: Autocreated FK slot
--     * Slot: related_control_ids Description: The controls and enhancements the publication lists as related, by identifier.
-- # Class: Sp80053ControlEnhancement_control_references
--     * Slot: Sp80053ControlEnhancement_id Description: Autocreated FK slot
--     * Slot: control_references Description: The publications the control or enhancement cites, by the labels the catalog's references carry, such as SP 800-12 or OMB A-130.
-- # Class: Sp80053ControlEnhancement_incorporated_into
--     * Slot: Sp80053ControlEnhancement_id Description: Autocreated FK slot
--     * Slot: incorporated_into Description: For a withdrawn control or enhancement, what it was incorporated into, as the publication states it.
-- # Class: Sp80053ControlEnhancement_moved_to
--     * Slot: Sp80053ControlEnhancement_id Description: Autocreated FK slot
--     * Slot: moved_to Description: For a withdrawn control or enhancement, the control or enhancement it moved to, as the publication states it.
-- # Class: Sp80053ControlEnhancement_implementation_level
--     * Slot: Sp80053ControlEnhancement_id Description: Autocreated FK slot
--     * Slot: implementation_level Description: Who implements the control or enhancement, as NIST's reference data marks it: the organization, the system, or both.
-- # Class: Sp80053ControlEnhancement_required_controls
--     * Slot: Sp80053ControlEnhancement_id Description: Autocreated FK slot
--     * Slot: required_controls Description: The controls and enhancements that must be implemented for the enhancement to apply, as NIST's catalog links them: its own control, and for SC-42(2) also SC-42(1).
-- # Class: Sp80053Parameter_parameter_guidelines
--     * Slot: Sp80053Parameter_id Description: Autocreated FK slot
--     * Slot: parameter_guidelines Description: The guidelines that say what a value must settle, such as that the frequency of a review is defined.
-- # Class: Sp80053Parameter_selection_choices
--     * Slot: Sp80053Parameter_id Description: Autocreated FK slot
--     * Slot: selection_choices Description: For a selection, the choices the publication lists, in order.
-- # Class: Sp80053Parameter_aggregated_parameters
--     * Slot: Sp80053Parameter_id Description: Autocreated FK slot
--     * Slot: aggregated_parameters Description: For a parameter that stands for several, the parameters it aggregates, by identifier.
-- # Class: Sp80053Parameter_alternative_identifiers
--     * Slot: Sp80053Parameter_id Description: Autocreated FK slot
--     * Slot: alternative_identifiers Description: The identifiers an earlier release of the catalog gave the parameter, such as ac-1_prm_2 for ac-01_odp.03.
-- # Class: Sp80053AssessmentMethod_assessment_objects
--     * Slot: Sp80053AssessmentMethod_id Description: Autocreated FK slot
--     * Slot: assessment_objects Description: The objects the method is applied to, in the order the publication lists them.
-- # Class: Sp80053Baseline_baseline_controls
--     * Slot: Sp80053Baseline_id Description: Autocreated FK slot
--     * Slot: baseline_controls Description: The controls and enhancements the baseline selects, by identifier, in the order the catalog gives them.

CREATE TABLE "Sp80053Catalog" (
	id INTEGER NOT NULL,
	catalog_release TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Sp80053Catalog_id" ON "Sp80053Catalog" (id);

CREATE TABLE "Sp80053Statement" (
	id INTEGER NOT NULL,
	statement_text TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Sp80053Statement_id" ON "Sp80053Statement" (id);

CREATE TABLE "Sp80053AssessmentObjective" (
	id INTEGER NOT NULL,
	objective_label TEXT NOT NULL,
	objective_text TEXT,
	"Sp80053AssessmentObjective_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp80053AssessmentObjective_id") REFERENCES "Sp80053AssessmentObjective" (id)
);
CREATE INDEX "ix_Sp80053AssessmentObjective_id" ON "Sp80053AssessmentObjective" (id);

CREATE TABLE "Sp80053Family" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	family_id TEXT NOT NULL,
	"Sp80053Catalog_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp80053Catalog_id") REFERENCES "Sp80053Catalog" (id)
);
CREATE INDEX "ix_Sp80053Family_id" ON "Sp80053Family" (id);

CREATE TABLE "Sp80053StatementItem" (
	id INTEGER NOT NULL,
	item_label TEXT NOT NULL,
	item_text TEXT NOT NULL,
	"Sp80053Statement_id" INTEGER,
	"Sp80053StatementItem_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp80053Statement_id") REFERENCES "Sp80053Statement" (id),
	FOREIGN KEY("Sp80053StatementItem_id") REFERENCES "Sp80053StatementItem" (id)
);
CREATE INDEX "ix_Sp80053StatementItem_id" ON "Sp80053StatementItem" (id);

CREATE TABLE "Sp80053Reference" (
	id INTEGER NOT NULL,
	reference_label TEXT NOT NULL,
	reference_citation TEXT,
	reference_url TEXT,
	"Sp80053Catalog_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp80053Catalog_id") REFERENCES "Sp80053Catalog" (id)
);
CREATE INDEX "ix_Sp80053Reference_id" ON "Sp80053Reference" (id);

CREATE TABLE "Sp80053Baseline" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	baseline_level VARCHAR(8) NOT NULL,
	"Sp80053Catalog_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp80053Catalog_id") REFERENCES "Sp80053Catalog" (id)
);
CREATE INDEX "ix_Sp80053Baseline_id" ON "Sp80053Baseline" (id);

CREATE TABLE "Sp80053Control" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	control_discussion TEXT,
	control_status VARCHAR(9),
	withdrawal_reason TEXT,
	contributes_to_assurance BOOLEAN,
	control_identifier TEXT NOT NULL,
	"Sp80053Family_id" INTEGER,
	control_statement_id INTEGER,
	assessment_objective_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp80053Family_id") REFERENCES "Sp80053Family" (id),
	FOREIGN KEY(control_statement_id) REFERENCES "Sp80053Statement" (id),
	FOREIGN KEY(assessment_objective_id) REFERENCES "Sp80053AssessmentObjective" (id)
);
CREATE INDEX "ix_Sp80053Control_id" ON "Sp80053Control" (id);

CREATE TABLE "Sp80053Baseline_baseline_controls" (
	"Sp80053Baseline_id" INTEGER,
	baseline_controls TEXT NOT NULL,
	PRIMARY KEY ("Sp80053Baseline_id", baseline_controls),
	FOREIGN KEY("Sp80053Baseline_id") REFERENCES "Sp80053Baseline" (id)
);
CREATE INDEX "ix_Sp80053Baseline_baseline_controls_Sp80053Baseline_id" ON "Sp80053Baseline_baseline_controls" ("Sp80053Baseline_id");
CREATE INDEX "ix_Sp80053Baseline_baseline_controls_baseline_controls" ON "Sp80053Baseline_baseline_controls" (baseline_controls);

CREATE TABLE "Sp80053ControlEnhancement" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	control_discussion TEXT,
	control_status VARCHAR(9),
	withdrawal_reason TEXT,
	contributes_to_assurance BOOLEAN,
	enhancement_id TEXT NOT NULL,
	"Sp80053Control_id" INTEGER,
	control_statement_id INTEGER,
	assessment_objective_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp80053Control_id") REFERENCES "Sp80053Control" (id),
	FOREIGN KEY(control_statement_id) REFERENCES "Sp80053Statement" (id),
	FOREIGN KEY(assessment_objective_id) REFERENCES "Sp80053AssessmentObjective" (id)
);
CREATE INDEX "ix_Sp80053ControlEnhancement_id" ON "Sp80053ControlEnhancement" (id);

CREATE TABLE "Sp80053Control_related_control_ids" (
	"Sp80053Control_id" INTEGER,
	related_control_ids TEXT,
	PRIMARY KEY ("Sp80053Control_id", related_control_ids),
	FOREIGN KEY("Sp80053Control_id") REFERENCES "Sp80053Control" (id)
);
CREATE INDEX "ix_Sp80053Control_related_control_ids_Sp80053Control_id" ON "Sp80053Control_related_control_ids" ("Sp80053Control_id");
CREATE INDEX "ix_Sp80053Control_related_control_ids_related_control_ids" ON "Sp80053Control_related_control_ids" (related_control_ids);

CREATE TABLE "Sp80053Control_control_references" (
	"Sp80053Control_id" INTEGER,
	control_references TEXT,
	PRIMARY KEY ("Sp80053Control_id", control_references),
	FOREIGN KEY("Sp80053Control_id") REFERENCES "Sp80053Control" (id)
);
CREATE INDEX "ix_Sp80053Control_control_references_control_references" ON "Sp80053Control_control_references" (control_references);
CREATE INDEX "ix_Sp80053Control_control_references_Sp80053Control_id" ON "Sp80053Control_control_references" ("Sp80053Control_id");

CREATE TABLE "Sp80053Control_incorporated_into" (
	"Sp80053Control_id" INTEGER,
	incorporated_into TEXT,
	PRIMARY KEY ("Sp80053Control_id", incorporated_into),
	FOREIGN KEY("Sp80053Control_id") REFERENCES "Sp80053Control" (id)
);
CREATE INDEX "ix_Sp80053Control_incorporated_into_incorporated_into" ON "Sp80053Control_incorporated_into" (incorporated_into);
CREATE INDEX "ix_Sp80053Control_incorporated_into_Sp80053Control_id" ON "Sp80053Control_incorporated_into" ("Sp80053Control_id");

CREATE TABLE "Sp80053Control_moved_to" (
	"Sp80053Control_id" INTEGER,
	moved_to TEXT,
	PRIMARY KEY ("Sp80053Control_id", moved_to),
	FOREIGN KEY("Sp80053Control_id") REFERENCES "Sp80053Control" (id)
);
CREATE INDEX "ix_Sp80053Control_moved_to_moved_to" ON "Sp80053Control_moved_to" (moved_to);
CREATE INDEX "ix_Sp80053Control_moved_to_Sp80053Control_id" ON "Sp80053Control_moved_to" ("Sp80053Control_id");

CREATE TABLE "Sp80053Control_implementation_level" (
	"Sp80053Control_id" INTEGER,
	implementation_level VARCHAR(12),
	PRIMARY KEY ("Sp80053Control_id", implementation_level),
	FOREIGN KEY("Sp80053Control_id") REFERENCES "Sp80053Control" (id)
);
CREATE INDEX "ix_Sp80053Control_implementation_level_Sp80053Control_id" ON "Sp80053Control_implementation_level" ("Sp80053Control_id");
CREATE INDEX "ix_Sp80053Control_implementation_level_implementation_level" ON "Sp80053Control_implementation_level" (implementation_level);

CREATE TABLE "Sp80053Parameter" (
	id INTEGER NOT NULL,
	parameter_id TEXT NOT NULL,
	assessment_label TEXT,
	parameter_label TEXT,
	selection_cardinality VARCHAR(11),
	alternative_label TEXT,
	"Sp80053Control_id" INTEGER,
	"Sp80053ControlEnhancement_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp80053Control_id") REFERENCES "Sp80053Control" (id),
	FOREIGN KEY("Sp80053ControlEnhancement_id") REFERENCES "Sp80053ControlEnhancement" (id)
);
CREATE INDEX "ix_Sp80053Parameter_id" ON "Sp80053Parameter" (id);

CREATE TABLE "Sp80053AssessmentMethod" (
	id INTEGER NOT NULL,
	assessment_method VARCHAR(9) NOT NULL,
	"Sp80053Control_id" INTEGER,
	"Sp80053ControlEnhancement_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp80053Control_id") REFERENCES "Sp80053Control" (id),
	FOREIGN KEY("Sp80053ControlEnhancement_id") REFERENCES "Sp80053ControlEnhancement" (id)
);
CREATE INDEX "ix_Sp80053AssessmentMethod_id" ON "Sp80053AssessmentMethod" (id);

CREATE TABLE "Sp80053ControlEnhancement_related_control_ids" (
	"Sp80053ControlEnhancement_id" INTEGER,
	related_control_ids TEXT,
	PRIMARY KEY ("Sp80053ControlEnhancement_id", related_control_ids),
	FOREIGN KEY("Sp80053ControlEnhancement_id") REFERENCES "Sp80053ControlEnhancement" (id)
);
CREATE INDEX "ix_Sp80053ControlEnhancement_related_control_ids_related_control_ids" ON "Sp80053ControlEnhancement_related_control_ids" (related_control_ids);
CREATE INDEX "ix_Sp80053ControlEnhancement_related_control_ids_Sp80053ControlEnhancement_id" ON "Sp80053ControlEnhancement_related_control_ids" ("Sp80053ControlEnhancement_id");

CREATE TABLE "Sp80053ControlEnhancement_control_references" (
	"Sp80053ControlEnhancement_id" INTEGER,
	control_references TEXT,
	PRIMARY KEY ("Sp80053ControlEnhancement_id", control_references),
	FOREIGN KEY("Sp80053ControlEnhancement_id") REFERENCES "Sp80053ControlEnhancement" (id)
);
CREATE INDEX "ix_Sp80053ControlEnhancement_control_references_Sp80053ControlEnhancement_id" ON "Sp80053ControlEnhancement_control_references" ("Sp80053ControlEnhancement_id");
CREATE INDEX "ix_Sp80053ControlEnhancement_control_references_control_references" ON "Sp80053ControlEnhancement_control_references" (control_references);

CREATE TABLE "Sp80053ControlEnhancement_incorporated_into" (
	"Sp80053ControlEnhancement_id" INTEGER,
	incorporated_into TEXT,
	PRIMARY KEY ("Sp80053ControlEnhancement_id", incorporated_into),
	FOREIGN KEY("Sp80053ControlEnhancement_id") REFERENCES "Sp80053ControlEnhancement" (id)
);
CREATE INDEX "ix_Sp80053ControlEnhancement_incorporated_into_Sp80053ControlEnhancement_id" ON "Sp80053ControlEnhancement_incorporated_into" ("Sp80053ControlEnhancement_id");
CREATE INDEX "ix_Sp80053ControlEnhancement_incorporated_into_incorporated_into" ON "Sp80053ControlEnhancement_incorporated_into" (incorporated_into);

CREATE TABLE "Sp80053ControlEnhancement_moved_to" (
	"Sp80053ControlEnhancement_id" INTEGER,
	moved_to TEXT,
	PRIMARY KEY ("Sp80053ControlEnhancement_id", moved_to),
	FOREIGN KEY("Sp80053ControlEnhancement_id") REFERENCES "Sp80053ControlEnhancement" (id)
);
CREATE INDEX "ix_Sp80053ControlEnhancement_moved_to_Sp80053ControlEnhancement_id" ON "Sp80053ControlEnhancement_moved_to" ("Sp80053ControlEnhancement_id");
CREATE INDEX "ix_Sp80053ControlEnhancement_moved_to_moved_to" ON "Sp80053ControlEnhancement_moved_to" (moved_to);

CREATE TABLE "Sp80053ControlEnhancement_implementation_level" (
	"Sp80053ControlEnhancement_id" INTEGER,
	implementation_level VARCHAR(12),
	PRIMARY KEY ("Sp80053ControlEnhancement_id", implementation_level),
	FOREIGN KEY("Sp80053ControlEnhancement_id") REFERENCES "Sp80053ControlEnhancement" (id)
);
CREATE INDEX "ix_Sp80053ControlEnhancement_implementation_level_Sp80053ControlEnhancement_id" ON "Sp80053ControlEnhancement_implementation_level" ("Sp80053ControlEnhancement_id");
CREATE INDEX "ix_Sp80053ControlEnhancement_implementation_level_implementation_level" ON "Sp80053ControlEnhancement_implementation_level" (implementation_level);

CREATE TABLE "Sp80053ControlEnhancement_required_controls" (
	"Sp80053ControlEnhancement_id" INTEGER,
	required_controls TEXT,
	PRIMARY KEY ("Sp80053ControlEnhancement_id", required_controls),
	FOREIGN KEY("Sp80053ControlEnhancement_id") REFERENCES "Sp80053ControlEnhancement" (id)
);
CREATE INDEX "ix_Sp80053ControlEnhancement_required_controls_Sp80053ControlEnhancement_id" ON "Sp80053ControlEnhancement_required_controls" ("Sp80053ControlEnhancement_id");
CREATE INDEX "ix_Sp80053ControlEnhancement_required_controls_required_controls" ON "Sp80053ControlEnhancement_required_controls" (required_controls);

CREATE TABLE "Sp80053Parameter_parameter_guidelines" (
	"Sp80053Parameter_id" INTEGER,
	parameter_guidelines TEXT,
	PRIMARY KEY ("Sp80053Parameter_id", parameter_guidelines),
	FOREIGN KEY("Sp80053Parameter_id") REFERENCES "Sp80053Parameter" (id)
);
CREATE INDEX "ix_Sp80053Parameter_parameter_guidelines_parameter_guidelines" ON "Sp80053Parameter_parameter_guidelines" (parameter_guidelines);
CREATE INDEX "ix_Sp80053Parameter_parameter_guidelines_Sp80053Parameter_id" ON "Sp80053Parameter_parameter_guidelines" ("Sp80053Parameter_id");

CREATE TABLE "Sp80053Parameter_selection_choices" (
	"Sp80053Parameter_id" INTEGER,
	selection_choices TEXT,
	PRIMARY KEY ("Sp80053Parameter_id", selection_choices),
	FOREIGN KEY("Sp80053Parameter_id") REFERENCES "Sp80053Parameter" (id)
);
CREATE INDEX "ix_Sp80053Parameter_selection_choices_selection_choices" ON "Sp80053Parameter_selection_choices" (selection_choices);
CREATE INDEX "ix_Sp80053Parameter_selection_choices_Sp80053Parameter_id" ON "Sp80053Parameter_selection_choices" ("Sp80053Parameter_id");

CREATE TABLE "Sp80053Parameter_aggregated_parameters" (
	"Sp80053Parameter_id" INTEGER,
	aggregated_parameters TEXT,
	PRIMARY KEY ("Sp80053Parameter_id", aggregated_parameters),
	FOREIGN KEY("Sp80053Parameter_id") REFERENCES "Sp80053Parameter" (id)
);
CREATE INDEX "ix_Sp80053Parameter_aggregated_parameters_Sp80053Parameter_id" ON "Sp80053Parameter_aggregated_parameters" ("Sp80053Parameter_id");
CREATE INDEX "ix_Sp80053Parameter_aggregated_parameters_aggregated_parameters" ON "Sp80053Parameter_aggregated_parameters" (aggregated_parameters);

CREATE TABLE "Sp80053Parameter_alternative_identifiers" (
	"Sp80053Parameter_id" INTEGER,
	alternative_identifiers TEXT,
	PRIMARY KEY ("Sp80053Parameter_id", alternative_identifiers),
	FOREIGN KEY("Sp80053Parameter_id") REFERENCES "Sp80053Parameter" (id)
);
CREATE INDEX "ix_Sp80053Parameter_alternative_identifiers_alternative_identifiers" ON "Sp80053Parameter_alternative_identifiers" (alternative_identifiers);
CREATE INDEX "ix_Sp80053Parameter_alternative_identifiers_Sp80053Parameter_id" ON "Sp80053Parameter_alternative_identifiers" ("Sp80053Parameter_id");

CREATE TABLE "Sp80053AssessmentMethod_assessment_objects" (
	"Sp80053AssessmentMethod_id" INTEGER,
	assessment_objects TEXT NOT NULL,
	PRIMARY KEY ("Sp80053AssessmentMethod_id", assessment_objects),
	FOREIGN KEY("Sp80053AssessmentMethod_id") REFERENCES "Sp80053AssessmentMethod" (id)
);
CREATE INDEX "ix_Sp80053AssessmentMethod_assessment_objects_assessment_objects" ON "Sp80053AssessmentMethod_assessment_objects" (assessment_objects);
CREATE INDEX "ix_Sp80053AssessmentMethod_assessment_objects_Sp80053AssessmentMethod_id" ON "Sp80053AssessmentMethod_assessment_objects" ("Sp80053AssessmentMethod_id");
