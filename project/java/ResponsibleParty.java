package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Assignment of parties to a role
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ResponsibleParty  {

  private String role-id;
  private List<String> party-uuids;

}