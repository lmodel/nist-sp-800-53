package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Metadata revision entry
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Revision  {

  private String title;
  private String last-modified;
  private String version;
  private String oscal-version;
  private List<Link> links;
  private String remarks;

}