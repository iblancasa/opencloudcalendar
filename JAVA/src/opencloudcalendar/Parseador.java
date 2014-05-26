package opencloudcalendar;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class Parseador {

    String urlXML;
    ArrayList<Convocatoria> convocatorias;
    
    public Parseador(String newurlXML){
            urlXML=newurlXML;
            
            if(!"/movil.xml".equals(urlXML.substring(urlXML.length()-10))){
                urlXML+="/movil.xml";
            }
            
            convocatorias = new ArrayList<>();
    }
    
    
    public ArrayList<Convocatoria> parse(){
        try {
            Convocatoria convo;

            URL url = new URL(urlXML);
            URLConnection urlConnection = url.openConnection();
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());

            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();

            Document doc = dBuilder.parse(in);
            doc.getDocumentElement().normalize();


            NodeList nodes = doc.getElementsByTagName("convocatoria");

            for (int i = 0; i < nodes.getLength(); i++) {
                Node node = nodes.item(i);

                if (node.getNodeType() == Node.ELEMENT_NODE) {

                    Element element = (Element) node;
                    String titulo = getValue("titulo", element);
                    String lugar =  getValue("lugar", element);
                    String descripcion = getValue("descripcion", element);
                    String fecha= getValue("fecha", element);

                    convo = new Convocatoria(titulo,lugar,fecha,descripcion);

                    convocatorias.add(convo);



                }
            }
        } catch (IOException | ParserConfigurationException | SAXException ex) {

        }
    
        return convocatorias;
    }

    private String getValue(String tag, Element element) {
            NodeList nodes = element.getElementsByTagName(tag).item(0).getChildNodes();
            Node node = (Node) nodes.item(0);
            return node.getNodeValue();
    }
}
