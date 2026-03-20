package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Base class for catalog elements
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CatalogElement  {

  private String id;
  private List<Property> props;
  private List<Link> links;
  private List<Part> parts;

}