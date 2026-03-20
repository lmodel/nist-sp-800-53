package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  OSCAL profile body
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProfileBody  {

  private String uuid;
  private Metadata metadata;
  private List<ImportResource> imports;
  private MergeRules merge;
  private BackMatter back-matter;

}