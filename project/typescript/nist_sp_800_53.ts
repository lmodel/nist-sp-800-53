/**
* Allowed values for element-level class values
*/
export enum CatalogElementClassValue {
    
    family = "family",
    SP800_53 = "SP800-53",
    SP800_53_enhancement = "SP800-53-enhancement",
    assessment_objective = "assessment-objective",
};
/**
* Allowed values for property-level class values
*/
export enum CatalogPropertyClassValue {
    
    sp800_53 = "sp800-53",
    sp800_53a = "sp800-53a",
    zero_padded = "zero-padded",
};
/**
* Allowed element_type values in NIST CPRT export data
*/
export enum CPRTElementTypeValue {
    
    /** SP 800-53 control family (e.g. AC, AU) */
    family = "family",
    /** Top-level security or privacy control (e.g. AC-1) */
    control = "control",
    /** Control enhancement (e.g. AC-1(1)) */
    control_enhancement = "control_enhancement",
    /** Normative control statement text */
    control_statement = "control_statement",
    /** Non-normative discussion text for a control */
    discussion = "discussion",
    /** Organization-Defined Parameter */
    odp = "odp",
    /** ODP category (e.g. assignment, selection) */
    odp_type = "odp_type",
    /** Full ODP statement text */
    odp_statement = "odp_statement",
    /** SP 800-53A Examine assessment objective */
    examine = "examine",
    /** SP 800-53A Interview assessment objective */
    interview = "interview",
    /** SP 800-53A Test assessment objective */
    test = "test",
    /** Assessment determination criterion */
    determination = "determination",
    /** Reason a control was withdrawn from SP 800-53 */
    withdraw_reason = "withdraw_reason",
    /** Informational reference to an external publication */
    reference = "reference",
    /** Security baseline designation (LOW / MODERATE / HIGH / NOT SELECTED) */
    security_baseline = "security_baseline",
    /** Privacy baseline designation (P-HIGH / NOT SELECTED) */
    privacy_baseline = "privacy_baseline",
    /** Sort-order key for display purposes */
    sort = "sort",
    /** Sort-order key for control name ordering */
    control_name_sort = "control_name_sort",
};
/**
* Relationship type identifiers used in NIST CPRT export data
*/
export enum CPRTRelationshipTypeValue {
    
    /** Represents a relationship between two elements */
    projection = "projection",
    /** Denotes where a control is related to another control */
    related = "related",
    /** Denotes where a withdrawn control was incorporated into another */
    incorporated_into = "incorporated_into",
    /** Denotes where a withdrawn control was moved to */
    moved_to = "moved_to",
};


/**
 * Unified root wrapper for catalog, profile, or CPRT content
 */
export interface SP80053Document {
    /** Root catalog payload */
    catalog?: CatalogBody,
    /** Root profile payload */
    profile?: ProfileBody,
    /** Top-level CPRT API response wrapper */
    response?: CPRTResponse,
}


/**
 * Top-level wrapper that mirrors OSCAL catalog shape
 */
export interface Catalog {
    /** Root catalog payload */
    catalog?: CatalogBody,
}


/**
 * Top-level wrapper for OSCAL profile files
 */
export interface ProfileDocument {
    /** Root profile payload */
    profile?: ProfileBody,
}


/**
 * Main catalog object
 */
export interface CatalogBody {
    /** UUID for profile, metadata, or resource element */
    uuid?: string,
    /** Profile and Catalog metadata */
    metadata?: Metadata,
    /** List of control groups in the catalog */
    groups?: ControlGroup[],
    /** Back-matter references and resources */
    back_matter?: BackMatter,
}


/**
 * OSCAL profile body
 */
export interface ProfileBody {
    /** UUID for profile, metadata, or resource element */
    uuid?: string,
    /** Profile and Catalog metadata */
    metadata?: Metadata,
    /** Imported catalogs or profiles */
    imports?: ImportResource[],
    /** Merge behavior settings */
    merge?: MergeRules,
    /** Profile modification directives — parameter overrides and control alterations */
    modify?: ProfileModify,
    /** Back-matter references and resources */
    back_matter?: BackMatter,
}


/**
 * OSCAL metadata section used in catalogs and profiles
 */
export interface Metadata {
    /** Human-readable title */
    title?: string,
    /** Last modification timestamp */
    last_modified?: string,
    /** Version identifier */
    version?: string,
    /** OSCAL version identifier */
    oscal_version?: string,
    /** Metadata revisions */
    revisions?: Revision[],
    /** List of properties */
    props?: Property[],
    /** List of links and relationships */
    links?: Link[],
    /** Roles used in metadata */
    roles?: Role[],
    /** Parties used in metadata */
    parties?: Party[],
    /** Responsible party assignments */
    responsible_parties?: ResponsibleParty[],
    /** Supplemental remarks */
    remarks?: string,
}


/**
 * Metadata revision entry
 */
export interface Revision {
    /** Human-readable title */
    title?: string,
    /** Last modification timestamp */
    last_modified?: string,
    /** Version identifier */
    version?: string,
    /** OSCAL version identifier */
    oscal_version?: string,
    /** List of links and relationships */
    links?: Link[],
    /** Supplemental remarks */
    remarks?: string,
}


/**
 * Role definition
 */
export interface Role {
    /** Unique identifier for an element */
    id?: string,
    /** Human-readable title */
    title?: string,
}


/**
 * Party definition
 */
export interface Party {
    /** UUID for profile, metadata, or resource element */
    uuid?: string,
    /** Party type */
    type?: string,
    /** Name of a property, part, or party */
    name?: string,
    /** Short display name */
    short_name?: string,
    /** Party email addresses */
    email_addresses?: string[],
    /** Postal addresses */
    addresses?: Address[],
}


/**
 * Postal address
 */
export interface Address {
    /** Address lines */
    addr_lines?: string[],
    /** City name */
    city?: string,
    /** State or region */
    state?: string,
    /** Postal code */
    postal_code?: string,
}


/**
 * Assignment of parties to a role
 */
export interface ResponsibleParty {
    /** Assigned role identifier */
    role_id?: string,
    /** Referenced party UUIDs */
    party_uuids?: string[],
}


/**
 * OSCAL back-matter section
 */
export interface BackMatter {
    /** Back-matter resources */
    resources?: Resource[],
}


/**
 * Referenced resource
 */
export interface Resource {
    /** UUID for profile, metadata, or resource element */
    uuid?: string,
    /** Human-readable title */
    title?: string,
    /** Resource description */
    description?: string,
    /** Citation details for a resource */
    citation?: Citation,
    /** Resource links */
    rlinks?: ResourceLink[],
}


/**
 * Citation wrapper
 */
export interface Citation {
    /** Citation text */
    text?: string,
}


/**
 * Reference link for a resource
 */
export interface ResourceLink {
    /** Link or resource reference */
    href?: string,
    /** Media type for a resource link */
    media_type?: string,
}


/**
 * Base class for catalog elements
 */
export interface CatalogElement {
    /** Unique identifier for an element */
    id?: string,
    /** List of properties */
    props?: Property[],
    /** List of links and relationships */
    links?: Link[],
    /** Nested parts that provide prose and structure */
    parts?: Part[],
}


/**
 * A catalog element with required id and optional title/class
 */
export interface IdentifiedElement extends CatalogElement {
    /** Human-readable title */
    title?: string,
    /** Classification of a catalog element or property */
    class?: string,
    /** Human-readable label */
    label?: string,
}


/**
 * A group of controls (family)
 */
export interface ControlGroup extends IdentifiedElement {
    /** List of control groups in the catalog */
    groups?: ControlGroup[],
    /** List of controls in a group */
    controls?: Control[],
}


/**
 * A security control
 */
export interface Control extends IdentifiedElement {
    /** List of parameters for a control */
    params?: Parameter[],
    /** List of controls in a group */
    controls?: ControlEnhancement[],
}


/**
 * An enhancement to a control
 */
export interface ControlEnhancement extends IdentifiedElement {
    /** List of parameters for a control */
    params?: Parameter[],
    /** List of controls in a group */
    controls?: ControlEnhancement[],
}


/**
 * A configurable parameter used by a control
 */
export interface Parameter extends IdentifiedElement {
    /** List of guidelines */
    guidelines?: Guideline[],
    /** Selection parameters for a parameter definition */
    select?: Selection,
    /** Identifier of another parameter this one depends on (SP 800-53 Rev 4 only) */
    depends_on?: string,
}


/**
 * Additional prose guidance associated with a parameter
 */
export interface Guideline {
    /** Free-text prose content */
    prose?: string,
}


/**
 * A name-value property with optional namespace and class attributes
 */
export interface Property {
    /** Name of a property, part, or party */
    name?: string,
    /** Property value */
    value?: string,
    /** Namespace URI for a property */
    ns?: string,
    /** Classification of a catalog element or property */
    class?: string,
}


/**
 * Selection criteria for a parameter
 */
export interface Selection {
    /** How many selections are allowed */
    how_many?: string,
    /** List of selection options */
    choice?: string[],
}


/**
 * Relationship link
 */
export interface Link {
    /** Link or resource reference */
    href?: string,
    /** Relationship type for a link */
    rel?: string,
}


/**
 * Structured narrative part that can contain nested parts
 */
export interface Part extends IdentifiedElement {
    /** Name of a property, part, or party */
    name?: string,
    /** Free-text prose content */
    prose?: string,
}


/**
 * Imported profile or catalog reference
 */
export interface ImportResource {
    /** Link or resource reference */
    href?: string,
    /** Include-controls selectors */
    include_controls?: IncludeControlsSelection[],
    /** Controls to explicitly exclude from an import */
    exclude_controls?: ExcludeControlsSelection[],
}


/**
 * Control inclusion selector
 */
export interface IncludeControlsSelection {
    /** Explicit control identifiers to include */
    with_ids?: string[],
    /** Pattern-based control selectors using glob or regex patterns */
    matching?: ControlPattern[],
}


/**
 * Merge configuration
 */
export interface MergeRules {
    /** Keep source order and content during merge */
    as_is?: boolean,
    /** Flat merge strategy — de-duplicate and merge all controls without source hierarchy */
    flat?: FlatMerge,
}


/**
 * Marker object indicating flat merge strategy for profile resolution
 */
export interface FlatMerge {
}


/**
 * Glob or regex pattern for selecting controls by identifier
 */
export interface ControlPattern {
    /** Glob or regex pattern for matching control identifiers */
    pattern?: string,
}


/**
 * Selection of controls to explicitly exclude from a profile import
 */
export interface ExcludeControlsSelection {
    /** Explicit control identifiers to include */
    with_ids?: string[],
    /** Pattern-based control selectors using glob or regex patterns */
    matching?: ControlPattern[],
}


/**
 * Profile modification section containing parameter overrides and control alterations
 */
export interface ProfileModify {
    /** Parameter value overrides applied by the profile */
    set_parameters?: ProfileSetParameter[],
    /** Control alterations — add or remove parts from referenced controls */
    alters?: ProfileAlter[],
}


/**
 * Override the value of a parameter in a referenced control
 */
export interface ProfileSetParameter {
    /** Identifier of the parameter to be set */
    param_id?: string,
    /** Human-readable label */
    label?: string,
}


/**
 * Alteration to a referenced control — adds or removes parts
 */
export interface ProfileAlter {
    /** Identifier of the control to alter */
    control_id?: string,
    /** Parts, parameters, or properties added to a control by an alteration */
    adds?: ProfileAdd[],
}


/**
 * Content to be added to a control via profile alteration
 */
export interface ProfileAdd {
    /** Position at which to add content relative to the by-id anchor */
    position?: string,
    /** Identifier of the anchor part relative to which additions are positioned */
    by_id?: string,
    /** Nested parts that provide prose and structure */
    parts?: Part[],
    /** List of properties */
    props?: Property[],
}


/**
 * Semantic class for NIST CPRT (Cybersecurity and Privacy Reference Tool) export documents covering SP 800-53, SP 800-53A, and SP 800-53B. Validate with: linkml validate -C SP80053Document -s <schema> <file.json>
 */
export interface CPRTDocument {
    /** Top-level CPRT API response wrapper */
    response?: CPRTResponse,
}


/**
 * CPRT API response container holding document metadata, typed elements (controls, enhancements, ODPs, assessment objectives, baselines), relationship types, and element relationships
 */
export interface CPRTResponse {
}



