#!/usr/bin/env python

import cgi
import datetime
import webapp2

import hashlib, sys

from google.appengine.ext import ndb
from google.appengine.api import users
from datetime import datetime

convocatoria_key = ndb.Key('Convocatoria', 'default_convocatoria')


class Convocatoria(ndb.Model):
  titulo = ndb.StringProperty()
  lugar = ndb.TextProperty()
  descripcion = ndb.TextProperty()
  date = ndb.DateTimeProperty()

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
          <section id="formulario">
            <form action="/publicar" method="post" id="nuevoEvento">
              <fieldset>
                <div class="elementoForm">
                  <label for="titulo">Titulo</label>
                  <input type="text" id="titulo" name="titulo"/>
                </div>

                <div class="elementoForm">
                  <label for="descripcion">Descripci&oacute;n</label>
                  <textarea name="descripcion" rows="10" cols="50"></textarea>
                </div>

                <div class="elementoForm">
                  <label for="lugar">Lugar</label>
                  <input type="text" id="lugar" name="lugar"/>
                </div>

                <div class="elementoForm">
                  <label for="dia">Fecha</label>
                  <select type="text" id="dia" name="dia"/>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="7">7</option>
                    <option value="8">8</option>
                    <option value="9">9</option>
                    <option value="10">10</option>
                    <option value="11">11</option>
                    <option value="12">12</option>
                    <option value="13">13</option>
                    <option value="14">14</option>
                    <option value="15">15</option>
                    <option value="16">16</option>
                    <option value="17">17</option>
                    <option value="18">18</option>
                    <option value="19">19</option>
                    <option value="20">20</option>
                    <option value="21">21</option>
                    <option value="22">22</option>
                    <option value="23">23</option>
                    <option value="24">24</option>
                    <option value="25">25</option>
                    <option value="26">26</option>
                    <option value="27">27</option>
                    <option value="28">28</option>
                    <option value="29">29</option>
                    <option value="30">30</option>
                    <option value="31">31</option>
                  </select>

                  <select type="text" id="mes" name="mes"/>
                    <option value="1">Enero</option>
                    <option value="2">Febrero</option>
                    <option value="3">Marzo</option>
                    <option value="4">Abril</option>
                    <option value="5">Mayo</option>
                    <option value="6">Junio</option>
                    <option value="7">Julio</option>
                    <option value="8">Agosto</option>
                    <option value="9">Septiembre</option>
                    <option value="10">Octubre</option>
                    <option value="11">Noviembre</option>
                    <option value="12">Diciembre</option>
                  </select>

                  <select type="text" id="anio" name="anio"/>
                    <option value="2014">2014</option>
                    <option value="2015">2015</option>
                    <option value="2016">2016</option>
                  </select>
                </div>

                <div class="elementoForm">
                  <label for="hora">Hora</label>
                    <select type="text" id="hora" name="hora"/>
                      <option value="0">00</option>
                      <option value="1">01</option>
                      <option value="2">02</option>
                      <option value="3">03</option>
                      <option value="4">04</option>
                      <option value="5">05</option>
                      <option value="6">06</option>
                      <option value="7">07</option>
                      <option value="8">08</option>
                      <option value="9">09</option>
                      <option value="10">10</option>
                      <option value="11">11</option>
                      <option value="12">12</option>
                      <option value="13">13</option>
                      <option value="14">14</option>
                      <option value="15">15</option>
                      <option value="16">16</option>
                      <option value="17">17</option>
                      <option value="18">18</option>
                      <option value="19">19</option>
                      <option value="20">20</option>
                      <option value="21">21</option>
                      <option value="22">22</option>
                      <option value="23">23</option>
                    </select>

                    <select type="text" id="minuto" name="minuto"/>
                      <option value="00">00</option>
                      <option value="01">01</option>
                      <option value="02">02</option>
                      <option value="03">03</option>
                      <option value="04">04</option>
                      <option value="05">05</option>
                      <option value="06">06</option>
                      <option value="07">07</option>
                      <option value="08">08</option>
                      <option value="09">09</option>
                      <option value="10">10</option>
                      <option value="11">11</option>
                      <option value="12">12</option>
                      <option value="13">13</option>
                      <option value="14">14</option>
                      <option value="15">15</option>
                      <option value="16">16</option>
                      <option value="17">17</option>
                      <option value="18">18</option>
                      <option value="19">19</option>
                      <option value="20">20</option>
                      <option value="21">21</option>
                      <option value="22">22</option>
                      <option value="23">23</option>
                      <option value="24">24</option>
                      <option value="25">25</option>
                      <option value="26">26</option>
                      <option value="27">27</option>
                      <option value="28">28</option>
                      <option value="29">29</option>
                      <option value="30">30</option>
                      <option value="31">31</option>
                      <option value="32">32</option>
                      <option value="33">33</option>
                      <option value="34">34</option>
                      <option value="35">35</option>
                      <option value="36">36</option>
                      <option value="37">37</option>
                      <option value="38">38</option>
                      <option value="39">39</option>
                      <option value="40">40</option>
                      <option value="41">41</option>
                      <option value="42">42</option>
                      <option value="43">43</option>
                      <option value="44">44</option>
                      <option value="45">45</option>
                      <option value="46">46</option>
                      <option value="47">47</option>
                      <option value="48">48</option>
                      <option value="49">49</option>
                      <option value="50">50</option>
                      <option value="51">51</option>
                      <option value="52">52</option>
                      <option value="53">53</option>
                      <option value="54">54</option>
                      <option value="55">55</option>
                      <option value="56">56</option>
                      <option value="57">57</option>
                      <option value="58">58</option>
                      <option value="59">59</option>
                    </select>
                  </div>

                  <div class="elementoForm">
                    <label for="usuario">Usuario</label>
                    <input type="text" id="usuario" name="usuario"/>
                  </div>

                  <div class="elementoForm">
                    <label for="password">Contrase&ntilde;a</label>
                    <input type="password" id="password" name="password"/>
                  </div>

                  <div class="elementoForm">
                    <input type="submit" value="Publicar evento">
                  </div>
              </fieldset>
            </form>
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


class Publicador(webapp2.RequestHandler):
  def post(self):

    configuracion = ndb.gql('SELECT * FROM Configuracion')
    config = configuracion.get()

    if config.admin == self.request.get('usuario') and config.password == hashlib.sha256(cgi.escape(self.request.get('password'))).hexdigest():   
      evento = Convocatoria(parent=convocatoria_key)
      mes = int(self.request.get('mes'))
      dia =  int(self.request.get('dia'))
      anio =  int(self.request.get('anio'))

      string_date = self.request.get('dia')
      string_date += " " + self.request.get('mes')
      string_date += " " + self.request.get('anio')
      string_date += " " + self.request.get('hora')
      string_date += ":" + self.request.get('minuto')
      fecha = datetime.strptime(string_date, '%d %m %Y %H:%M')

      if anio%4==0 and (anio%100!=0 or anio%400==0):
        bisiesto=True;
      else:
        bisiesto=False;
      
      if (mes==2 and bisiesto==True and dia>29):
        self.redirect('/error')
      elif (mes==2 and bisiesto==False and dia>28):
        self.redirect('/error')
      elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
        self.redirect('/error')
      else:
        evento.titulo = self.request.get('titulo')
        evento.descripcion = self.request.get('descripcion')
        evento.lugar = self.request.get('lugar')
        evento.date = fecha
        evento.put()

        self.redirect('/satisfactorio')
    else:
      self.redirect('/error')
      
    



app = webapp2.WSGIApplication([
  ('/escribir', MainPage),
  ('/publicar', Publicador),
], debug=True)
