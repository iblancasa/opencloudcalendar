package com.iblancasa.opencloudcalendar;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		findViewById(R.id.view_events).setOnClickListener(new OnClickListener(){
            public void onClick(View arg0) {
            	Intent intent = new Intent("com.iblancasa.opencloudcalendar.ListaEventos");
                startActivity(intent);
            }
            });
		
		findViewById(R.id.creditsButton).setOnClickListener(new OnClickListener(){
            public void onClick(View arg0) {
            	Intent intent = new Intent("com.iblancasa.opencloudcalendar.Creditos");
                startActivity(intent);
            }
            });
	}
}
