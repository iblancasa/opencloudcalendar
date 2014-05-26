package com.iblancasa.opencloudcalendar;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class MostrarEvento extends Activity{
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		setContentView(R.layout.mostrar_evento);
		
		 Bundle bundle = getIntent().getExtras();

		 String titulo = bundle.getString("titulo");
		 String descripcion = bundle.getString("descripcion");
		 String hora = bundle.getString("hora");
		 String lugar = bundle.getString("lugar");
		 
		 TextView tituloLabel = (TextView)findViewById(R.id.tituloEvento);
		 tituloLabel.setText(titulo);
		 
		 TextView descripcionLabel = (TextView)findViewById(R.id.descripcionEvento);
		 descripcionLabel.setText(descripcion);
		 
		 TextView horaLabel = (TextView)findViewById(R.id.horaEvento);
		 horaLabel.setText(hora);
		 
		 TextView lugarLabel = (TextView)findViewById(R.id.lugarEvento);
		 lugarLabel.setText(lugar);
	}
	
}
