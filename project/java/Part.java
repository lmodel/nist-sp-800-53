package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Structured narrative part that can contain nested parts
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Part extends IdentifiedElement {

  private String name;
  private String prose;

}