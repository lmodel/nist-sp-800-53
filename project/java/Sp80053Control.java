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
  A security or privacy control: a safeguard with an identifier, a statement of what it requires, a discussion, parameters the organization defines, related controls, references, the assessment objective and methods SP 800-53A gives it, and its enhancements. A control Revision 5 withdrew keeps its identifier and says where it went.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053Control  {

  private String title;
  private Sp80053Statement controlStatement;
  private String controlDiscussion;
  private List<Sp80053Parameter> controlParameters;
  private List<String> relatedControlIds;
  private List<String> controlReferences;
  private Sp80053AssessmentObjective assessmentObjective;
  private List<Sp80053AssessmentMethod> assessmentMethods;
  private String controlStatus;
  private List<String> incorporatedInto;
  private List<String> movedTo;
  private String withdrawalReason;
  private List<String> implementationLevel;
  private Boolean contributesToAssurance;
  private String controlIdentifier;
  private List<Sp80053ControlEnhancement> controlEnhancements;


}