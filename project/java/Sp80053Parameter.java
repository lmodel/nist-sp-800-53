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
  An organization-defined parameter: a value the control statement leaves to the organization, either an assignment the organization fills in or a selection from the choices the publication lists. SP 800-53A gives each a label and a guideline of its own.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053Parameter  {

  private String parameterId;
  private String assessmentLabel;
  private String parameterLabel;
  private List<String> parameterGuidelines;
  private List<String> selectionChoices;
  private String selectionCardinality;
  private List<String> aggregatedParameters;
  private List<String> alternativeIdentifiers;
  private String alternativeLabel;


}