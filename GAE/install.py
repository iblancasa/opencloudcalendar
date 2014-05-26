#!/usr/bin/env python

import cgi
import datetime
import webapp2

import hashlib, sys

from google.appengine.ext import ndb
from google.appengine.api import users
from datetime import datetime

configuracion_key = ndb.Key('Configuracion', 'default_configuracion')

class Configuracion(ndb.Model):
  titulo = ndb.StringProperty()
  admin = ndb.StringProperty()
  password = ndb.StringProperty()
  email = ndb.StringProperty()


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("""
      <!doctype html>
      <html>
        <head>
         <title>OpenCloudCalendar</title>
         <link type="text/css" rel="stylesheet" href="/stylesheets/estilo.css" />
        </head>
      <body>
        <section id="wrapper">
          <header><h1>OpenCloudCalendar</h1></header>
          \n""")


    configuracion = ndb.gql('SELECT * FROM Configuracion')
    if configuracion.count() == 0:


      self.response.out.write("""
            <section id="formulario">
              <form action="/instalarBD" method="post" id="nuevoEvento">
                <fieldset>
                  <div class="elementoForm">
                    <label for="titulo">Titulo del sitio</label>
                    <input type="text" id="titulo" name="titulo" required/>
                  </div>
                  <div class="elementoForm">
                    <label for="admin">Administrador</label>
                    <input type="text" id="admin" name="admin" pattern="^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$" required/>
                  </div>
                  <div class="elementoForm">
                    <label for="password">Contrase&ntilde;a</label>
                    <input type="password" id="password" name="password" pattern="(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" required/>
                  </div>

                  <div class="elementoForm">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required/>
                  </div>

                  <div class="elementoForm">
                      <input type="submit" value="Instalar">
                  </div>
                </fieldset>
              </form>
              <p>Todos los campos son obligatorios</p>
              <p>El nombre de usuario debe estar compuesto solo por caracteres alfanum&eacute;ricos</p>
              <p>La contrase&ntilde;a debe de tener, al menos:</p>
              <ul>
                <li>Una may&uacute;scula</li>
                <li>Una min&uacute;scula</li>
                <li>Un n&uacute;mero</li>
                <li>M&iacute;nimo 8 caracteres</li>
              </ul>
            </section>
            <footer>
              <details>
                <summary>Powered by OpenCloudCalendar</summary>
                <p>Web funcionando con OpenCloudCalendar</p>
              </details>
              <p><a href="http://www.gnu.org/licenses/gpl.txt">Licensing under GPLv3</a></p>
            </footer>
           </section>
          </body>
        </html>""")

    else:
      self.redirect('/')

class Instalador(webapp2.RequestHandler):
  def post(self):
    config = Configuracion(parent=configuracion_key)

    config.titulo = cgi.escape(self.request.get('titulo'))
    config.admin = cgi.escape(self.request.get('admin'))
    config.password = hashlib.sha256(cgi.escape(self.request.get('password'))).hexdigest()
    config.email = cgi.escape(self.request.get('email'))

    config.put()

    self.redirect('/')


app = webapp2.WSGIApplication([
  ('/instalacion', MainPage),
  ('/instalarBD', Instalador)
], debug=True)
