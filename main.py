__version__ = "1.0.2"

#--------------------------------------------
import ssl
import urllib.request # => para Python3
import urllib.error
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
#--------------------------------------------

import kivy
kivy.require("1.11.1") 

#Teclado
from kivy.config import Config
#Teclado de windows
Config.set('kivy', 'keyboard_mode', 'system')
#Teclado para Linux
#Config.set('kivy', 'keyboard_mode', 'systemandmulti')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.graphics import Line, RenderContext
from kivy.animation import Animation

#Colores Hex
import utils
from utils import enum
import python_utils
import logging
from python_utils import converters
from python_utils.import_ import import_global

import datetime
from datetime import date

import json

import os
import os.path
import threading
import subprocess
import sys

from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock,  mainthread
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.core.audio import SoundLoader
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.image import Image
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.graphics import *
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

class Menu_Principal(Screen):
	def salir(self):
		show_popup_salir(False)		

class Json_Interno(Screen):
	def traer_datos(self):
		#Varias opciones
		#Diccionario
		datos = """
		[
			{
		        "nombre": "Juan Perez",
		        "edad": 18,
		        "pais": "Panama"
			},
			{
		        "nombre": "Javi",
		        "edad": 34,
		        "pais": "París"
			}
		]
		"""
		json_datos = json.loads(datos);
		print("Objeto tipo diccionario:", json_datos)
		#---------------------------------------
		#Imprimir un listado json con datos  
		#---------------------------------------
		datos_1 =[
				{
			    "nombre" : "Juan",
			    "edad"   : 38,
			    "pais"   : "Alicante"
				},
				{
		        "nombre": "Luis",
		        "edad": 28,
		        "pais": "Madrid"
				}
				]
		json_str = json.dumps(datos_1)
		print('Datos en formato JSON:', json_str)
		#---------------------------------------
		#Grabar los datos en un fichero json
		#---------------------------------------
		with open('datos.json', 'w') as file:
			json.dump(datos_1, file)
		with open('datos.json', 'r') as file:
			datos = json.load(file)
			print("Salida del fichero Json: ", datos)	

class Api(Screen):
	datos_json = StringProperty("")
	def traer_datos_api(self):
		try:		
			url = "https://jsonplaceholder.typicode.com/todos/1"
			request_json = urllib.request.Request(
			    url, 
			    data=None, 
			    headers={
			        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; Android 9; Android 7.0) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
			    }
			)
			gcontext = ssl._create_unverified_context()
			response = urllib.request.urlopen(request_json, context = gcontext)
			if response.getcode() == 401:
				print("Acceso no Autorizado", str(response.getcode()))
			if response.getcode() == 403:
				print("Acceso Prohibido", str(response.getcode()))			
			if response.getcode() == 200:
				print("Acceso Autorizado:", str(response.getcode()))
				datos = json.loads(response.read())
				self.datos_json = str(datos)
				print(datos)					
		except (urllib.error.HTTPError) as e:
			print("Ocurrió un error de conexion: ", e)

class ScreenManager(ScreenManager):
	pass

class Menu(BoxLayout):
    pass

with open('main.kv', encoding='utf-8') as f:
    Builder.load_string(f.read())

class TestApp(App):
    title = 'Mi Comunidad'
    def build(self):
        return Menu()

if __name__ == '__main__':
    TestApp().run()
