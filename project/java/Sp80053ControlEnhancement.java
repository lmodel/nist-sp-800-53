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
  A control enhancement: added functionality or strength for a control, with an identifier of its own, which the publication and other documents cite apart from the control. It carries what a control carries, and names the control or enhancement it requires.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053ControlEnhancement  {

  private String enhancementId;
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
  private List<String> requiredControls;


}