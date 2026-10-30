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
  One of the four control baselines SP 800-53B defines: the controls and enhancements selected for systems at the low, moderate or high impact level, or for privacy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053Baseline  {

  private String baselineLevel;
  private String title;
  private List<String> baselineControls;


}