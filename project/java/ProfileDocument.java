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
  Top-level wrapper for OSCAL profile files
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProfileDocument  {

  private Object profile;


}