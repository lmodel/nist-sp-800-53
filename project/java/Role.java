package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Role definition
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Role  {

  private String id;
  private String title;

}