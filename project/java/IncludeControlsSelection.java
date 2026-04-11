package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Control inclusion selector
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IncludeControlsSelection  {

  private List<String> with-ids;

}