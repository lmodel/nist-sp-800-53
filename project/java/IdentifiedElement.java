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
  A catalog element with required id and optional title/class
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IdentifiedElement extends CatalogElement {

  private String title;
  private String class_;
  private String label;


}