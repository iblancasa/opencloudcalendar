#!/usr/bin/env python


import webapp2


class MainPage(webapp2.RequestHandler):
  def get(self):
           self.response.out.write("""
      <!doctype html>
      <html>
        <head>
          <meta http-equiv="Refresh" content="5;url=http://opencloudcalendar.appspot.com">
         <title>OpenCloudCalendar</title>
         <link type="text/css" rel="stylesheet" href="/stylesheets/estilo.css" />
        </head>
      <body>
        <section id="wrapper">
          <header><h1>OpenCloudCalendar</h1></header>
          <section>
            <h2 id="error">Su petici&oacute;n no pudo completarse de forma satisfactoria</h2>
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

app = webapp2.WSGIApplication([
  ('/error', MainPage)
], debug=True)
