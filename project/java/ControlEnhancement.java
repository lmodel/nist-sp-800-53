package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  An enhancement to a control
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlEnhancement extends IdentifiedElement {

  private List<Parameter> params;
  private List<ControlEnhancement> controls;

}