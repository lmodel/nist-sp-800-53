package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  A group of controls (family)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlGroup extends IdentifiedElement {

  private List<Control> controls;

}