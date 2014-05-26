#!/usr/bin/env python

import cgi
import datetime
import webapp2

import hashlib, sys

from google.appengine.ext import ndb
from google.appengine.api import users
from datetime import datetime

from lxml import etree
from lxml.etree import tostring
from lxml.builder import E


convocatoria_key = ndb.Key('Convocatoria', 'default_convocatoria')

class Convocatoria(ndb.Model):
  titulo = ndb.StringProperty()
  lugar = ndb.TextProperty()
  descripcion = ndb.TextProperty()
  date = ndb.DateTimeProperty()


class MainPage(webapp2.RequestHandler):
  def get(self):

    convocatorias = ndb.gql('SELECT * '
                    'FROM Convocatoria '
                    'ORDER BY date ASC')


    eventos = etree.Element('eventos')

    for convocatoria in convocatorias:
        convocatoriaLabel = etree.Element('convocatoria')
        
        titulo = etree.Element('titulo')
        titulo.text = convocatoria.titulo
        convocatoriaLabel.append(titulo)

        lugar = etree.Element('lugar')
        lugar.text = convocatoria.lugar
        convocatoriaLabel.append(lugar)

        descripcion = etree.Element('descripcion')
        descripcion.text = convocatoria.descripcion
        convocatoriaLabel.append(descripcion)

        fecha = etree.Element('fecha')
        fecha.text = convocatoria.date.strftime('%m/%d/%Y %H:%M')
        convocatoriaLabel.append(fecha)

        eventos.append(convocatoriaLabel)
    

    s = etree.tostring(eventos, pretty_print=True)


    self.response.out.write("<?xml version=\"1.0\"?>\n")
    self.response.out.write(s)


app = webapp2.WSGIApplication([
  ('/movil.xml', MainPage),
], debug=True)
