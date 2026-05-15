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
  A name-value property with optional namespace and class attributes
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Property  {

  private String name;
  private String value;
  private String ns;
  private String class_;


}