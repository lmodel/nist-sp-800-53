package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Reference link for a resource
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResourceLink  {

  private String href;
  private String media-type;

}