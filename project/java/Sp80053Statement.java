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
  A control statement: the text of what a control or enhancement requires, and the items it is divided into.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053Statement  {

  private List<Sp80053StatementItem> statementItems;
  private String statementText;


}