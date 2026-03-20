package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Selection criteria for a parameter
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Selection  {

  private String how-many;
  private List<String> choice;

}