package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  OSCAL metadata section used in catalogs and profiles
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Metadata  {

  private String title;
  private String last-modified;
  private String version;
  private String oscal-version;
  private List<Revision> revisions;
  private List<Property> props;
  private List<Link> links;
  private List<Role> roles;
  private List<Party> parties;
  private List<ResponsibleParty> responsible-parties;
  private String remarks;

}