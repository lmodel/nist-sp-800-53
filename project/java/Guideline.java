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
  Additional prose guidance associated with a parameter
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Guideline  {

  private String prose;


}