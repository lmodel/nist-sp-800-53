package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Referenced resource
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Resource  {

  private String uuid;
  private String title;
  private String description;
  private Citation citation;
  private List<ResourceLink> rlinks;

}