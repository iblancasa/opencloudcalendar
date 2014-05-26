package com.iblancasa.opencloudcalendar;

import java.util.ArrayList;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class ListaEventos extends Activity {

	private ArrayList<Convocatoria> convocatorias;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		setContentView(R.layout.lista_eventos);
		
		ListView list;
		 
		 
        Parseador pars = new Parseador("http://opencloudcalendar.appspot.com");
        convocatorias = pars.parse();
        String [] eventos = new String [convocatorias.size()];
        
        
        for(int i=0; i<convocatorias.size();i++){
            eventos[i] = convocatorias.get(i).getTitulo();
        }
		 
		 
		 list = (ListView)findViewById(R.id.lista_eventos);
		 
		 
		 ArrayAdapter<String> adaptador = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, eventos);
		    
		 list.setAdapter(adaptador);
		 
		 list.setOnItemClickListener(new OnItemClickListener(){
	     
			    @Override
			    public void onItemClick(AdapterView<?> arg0, View arg1, int position, long id) {
			        // TODO Auto-generated method stub
			        Intent verEvento = new Intent("com.iblancasa.opencloudcalendar.MostrarEvento");
			        verEvento.putExtra("titulo", convocatorias.get(position).getTitulo());
			        verEvento.putExtra("descripcion", convocatorias.get(position).getDescripcion());
			        verEvento.putExtra("hora", convocatorias.get(position).getHora());
			        verEvento.putExtra("lugar", convocatorias.get(position).getLugar());
			        startActivity(verEvento);
			    }

			}); 
		
	}

	
}
