package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Imported profile or catalog reference
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImportResource  {

  private String href;
  private List<IncludeControlsSelection> include-controls;

}