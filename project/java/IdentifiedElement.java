package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  A catalog element with required id and optional title/class
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IdentifiedElement extends CatalogElement {

  private String title;
  private String class;
  private String label;

}