package None;

/* metamodel_version: 1.11.0 */
/* version: 5.2.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A group of controls (family)
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlGroup extends IdentifiedElement {

  private List<ControlGroup> groups;
  private List<Control> controls;


}