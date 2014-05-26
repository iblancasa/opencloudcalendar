#!/usr/bin/env python


import webapp2
import datetime


from google.appengine.ext import ndb



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

    for convocatoria in convocatorias:
      diff = datetime.datetime.now() - convocatoria.date

      if diff > datetime.timedelta( seconds = 0 ):
        convocatoria.key.delete()

      else:
        break

app = webapp2.WSGIApplication([
  ('/borrado', MainPage)
], debug=True)
