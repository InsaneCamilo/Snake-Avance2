import turtle
import time
import random

# Clase de la comida
class Comida():

    def __init__(self, colorComida, screen,size):
        x=0
        y=0
        if (size/50)%2==0:
            x=-25
            y=-25
        else:
          x=50
          y=50
        """self.comida = turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape('img/Comida.gif')
        self.comida.color(colorComida)
        self.comida.penup()
        self.comida.goto(x-100,y)"""

        self.lado = screen.lado
    def posMin(self,pos):
      #pos=[["1","1","1"],["1","1","1"],["1","0","1"]] 
      sizeMat=len(pos)
      des=0
      if sizeMat%2==0:
        des=25
      print(sizeMat)
      for i in range(sizeMat):
        for j in range(sizeMat):
          if pos[i][j]=="1":
            x=j*50-50-des
            y=-i*50+50+des
            self.comida = turtle.Turtle()
            self.comida.speed(0)
            self.comida.shape('img/Comida.gif')
            self.comida.penup()
            self.comida.goto(x,y)
            print("x:",x," y:",y)
      return True

          
    # Método de cuando la serpiente colisiona con la comida
    def alColisionar(self, serpiente, game):
        if serpiente.cabeza.distance(self.comida) < 50:
            condicion = True
            while condicion:
                # Posición random
                x = (random.randint(0, 19)*50+25)-(self.lado/2)
                y = (random.randint(0, 19)*50+25)-(self.lado/2)

                # Comprueba que no coincida con el cuerpo de la serpiente
                if len(serpiente.segmentos)>0:
                    for seg in serpiente.segmentos:
                        if x==seg.xcor() and y==seg.ycor():
                            condicion = True
                            break
                        else:
                            condicion = False
                else:
                    condicion = False
            # Mueve la comida a la nueva posición
            self.comida.goto(x,y)

            # Se suma el puntaje
            game.actualizarPuntaje(10)
            
            # Se le agrega un nuevo segmento a la sepiente
            serpiente.agregarSegmentos()

            return True
        else:
            return False     

