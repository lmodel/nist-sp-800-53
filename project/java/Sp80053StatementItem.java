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
  One lettered or numbered item of a control statement, which may hold items of its own.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp80053StatementItem  {

  private List<Sp80053StatementItem> statementItems;
  private String itemLabel;
  private String itemText;


}