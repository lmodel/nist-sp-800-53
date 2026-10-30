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
  One release of the control catalog as a whole: its families, each holding its controls and their enhancements, the baselines that select from them, and the publications the catalog lists.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053Catalog  {

  private String catalogRelease;
  private List<Sp80053Family> controlFamilies;
  private List<Sp80053Baseline> controlBaselines;
  private List<Sp80053Reference> catalogReferences;


}