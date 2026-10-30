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
  An assessment objective of SP 800-53A: a determination statement an assessor checks, or a heading that groups the determination statements of one item of the control statement.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053AssessmentObjective  {

  private String objectiveLabel;
  private String objectiveText;
  private List<Sp80053AssessmentObjective> subObjectives;


}