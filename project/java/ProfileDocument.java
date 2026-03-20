package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Top-level wrapper for OSCAL profile files
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProfileDocument  {

  private ProfileBody profile;

}