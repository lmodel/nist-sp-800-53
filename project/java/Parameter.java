package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  A configurable parameter used by a control
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Parameter extends IdentifiedElement {

  private List<Guideline> guidelines;
  private Selection select;

}