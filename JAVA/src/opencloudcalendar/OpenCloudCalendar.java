
package opencloudcalendar;

import java.util.ArrayList;

/**
 *
 * @author iblancasa
 */
public class OpenCloudCalendar {
    public static void main(String args[]) {
        Parseador pars = new Parseador("http://pruebaphpisrael.appspot.com");
        ArrayList<Convocatoria> convocatorias = pars.parse();
        
        for(int i=0; i<convocatorias.size();i++){
            System.out.println("Titulo " + convocatorias.get(i).getTitulo());
        }
    }
}
