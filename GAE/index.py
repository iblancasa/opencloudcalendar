#!/usr/bin/env python

import cgi
import datetime
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users
from datetime import datetime

convocatoria_key = ndb.Key('Convocatoria', 'default_convocatoria')



class Convocatoria(ndb.Model):
  titulo = ndb.StringProperty()
  lugar = ndb.TextProperty()
  descripcion = ndb.TextProperty()
  date = ndb.DateTimeProperty()


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("""
      <!doctype html>
      <html>
        <head>
          <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
         <title>OpenCloudCalendar</title>
         <link type="text/css" rel="stylesheet" href="/stylesheets/estilo.css" />
        </head>
      <body>
        <section id="wrapper">
          <header><h1>OpenCloudCalendar</h1></header>
          <section id="convocatorias">\n""")

    convocatorias = ndb.gql('SELECT * '
                        'FROM Convocatoria '
                        'ORDER BY date ASC')

    for convocatoria in convocatorias:
      self.response.out.write('           <article class="convocatoria"> \n')
      self.response.out.write("""            <h2 class="titulo">%s</h2>\n""" %
                               cgi.escape(convocatoria.titulo))
      self.response.out.write("""            <span class="lugar">%s</span>
            <span class="lugarLabel">Lugar:</span>\n""" %
                              cgi.escape(convocatoria.lugar))
      self.response.out.write("""            <p class="descripcion">%s</p>\n""" %
                              cgi.escape(convocatoria.descripcion))
      self.response.out.write("""            <span class="fechaLabel">Fecha</span>
            <span class="fecha"> %s</span>\n""" %
                              cgi.escape(convocatoria.date.strftime('%m/%d/%Y %H:%M')))
      self.response.out.write("""           </article>\n""")
    self.response.out.write("""         </section>""")



    self.response.out.write("""
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


app = webapp2.WSGIApplication([
  ('/', MainPage)
], debug=True)
