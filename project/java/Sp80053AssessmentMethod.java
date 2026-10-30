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
  One assessment method SP 800-53A gives a control or enhancement, with the objects an assessor selects from: documents and records to examine, people to interview, or mechanisms and activities to test.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053AssessmentMethod  {

  private String assessmentMethod;
  private List<String> assessmentObjects;


}