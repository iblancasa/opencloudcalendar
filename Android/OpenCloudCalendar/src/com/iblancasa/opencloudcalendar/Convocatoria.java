package com.iblancasa.opencloudcalendar;

public class Convocatoria {
    String hora;
    String lugar;
    String titulo;
    String descripcion;
    
    public Convocatoria(String newTitulo, String newLugar, String newHora, String newDescripcion){
        hora=newHora;
        lugar=newLugar;
        titulo=newTitulo;
        descripcion=newDescripcion;
    }
    
    public String getHora(){
        return hora;
    }
    
    public String getLugar(){
        return lugar;
    }
    
    public String getTitulo(){
        return titulo;
    }
    
    public String getDescripcion(){
        return descripcion;
    }
}