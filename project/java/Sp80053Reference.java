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
  A publication the catalog's references list, as they list it: its label, its citation and its address.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053Reference  {

  private String referenceLabel;
  private String referenceCitation;
  private URI referenceUrl;


}