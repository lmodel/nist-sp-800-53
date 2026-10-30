package example;

/* metamodel_version: 1.12.0 */
/* version: 5.2.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One of the twenty families SP 800-53 sorts its controls into, such as Access Control or Supply Chain Risk Management.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053Family  {

  private String title;
  private String description;
  private String familyId;
  private List<Sp80053Control> familyControls;


}