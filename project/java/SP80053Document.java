package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Unified root wrapper for catalog or profile content
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SP80053Document  {

  private CatalogBody catalog;
  private ProfileBody profile;

}