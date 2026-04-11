/**
* Allowed values for element-level class values
*/
export enum CatalogElementClassValue {
    
    family = "family",
    SP800_53 = "SP800-53",
    SP800_53_enhancement = "SP800-53-enhancement",
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
 * Unified root wrapper for catalog or profile content
 */
export interface SP80053Document {
    /** Root catalog payload */
    catalog?: CatalogBody,
    /** Root profile payload */
    profile?: ProfileBody,
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
}


/**
 * Control inclusion selector
 */
export interface IncludeControlsSelection {
    /** Explicit control identifiers to include */
    with_ids?: string[],
}


/**
 * Merge configuration
 */
export interface MergeRules {
    /** Keep source order and content during merge */
    as_is?: boolean,
}



