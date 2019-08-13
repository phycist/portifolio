#Bibliotecas###########
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner 
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
#########################################
##################
class Botao(ButtonBehavior,Label):
      cor_normal = ListProperty([0.1,0.5,0.7,1])
      cor_press =  ListProperty([0.7,0.1,0.7,1])
      def __init__(self,**kwargs):
          super(Botao,self).__init__(**kwargs)
          self.atualizar()
      def on_pos(self,*args):
          self.atualizar()
      
      def on_size(self,*args):
          self.atualizar()

      def on_press(self, *args):
          self.cor_normal, self.cor_press = self.cor_press, self.cor_normal

      def on_release(self, *args):
          self.cor_normal, self.cor_press = self.cor_press, self.cor_normal 

      def on_cor_normal(self,*args):
          self.atualizar()

      def atualizar(self,*args): 
          self.canvas.before.clear()
          with self.canvas.before:
               Color(rgba=self.cor_normal)
               Ellipse(size=(10*self.height,self.height),
                           pos=(self.center_x-180,self.center_y - 20))


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
class entradaJanela(BoxLayout):
        #   Inicializar o app
      def __init__(self, **kwargs):
          super(entradaJanela,self).__init__(**kwargs)
          self.valor='' 
    ###############################################
      
#----------fucionalidades------------------------------------
      def spinner_clicked(self, value):
          print(value)
          if value == 'locador':
             print("chamando locador")
             self.valor = value
          else:
              if value == 'locatario':
                 print("Chamando locatario")
                 self.valor = value
           
          print("voce escolheu")
      
      
#----------------verificação do login --------------------
      
      def pegar_valores(self):
          
         # pegar valor da escolha
         escolha = self.ids.spinner_id_head
         print(escolha)
         # pegar o valor login
         login = self.ids.text_input_login.text
         print(login)
         # pegar o valor password
         password = self.ids.text_input_password.text
         print(password)
         if login !="" and password !="":
            return [login, password]
         else:
             print("Acesso negado")
      
      def validacao(self):
          validar = self.pegar_valores()
          if validar != []:
              print("O seu login é ")
              print(validar[0])
              print("A sua senha é ")
              print(validar[1])

          else:
              print("Deu Pau")

#--------------------------------------------------------

              









     
          

