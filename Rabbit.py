import turtle
import time
import random

#Clase de la serpiente
class Serpiente():
    #Atributo de lista de los segmentos del snake
    segmentos = []

    def __init__(self, colorCabeza, colorSegmento,size):
        x=0
        y=0
        if (size/50)%2==0:
            x=-25
            y=-25
        else:
          x=50
          y=50
        self.cabeza = turtle.Turtle()
        self.cabeza.speed(1)
        self.cabeza.shape('img/POU1.gif')
        self.cabeza.color(colorCabeza)
        self.cabeza.penup()
        self.cabeza.goto(x,y)
        self.cabeza.direction = "stop"

        # Color de los segmentos
        self.colorSegmento = colorSegmento
    
    #Configuración de controles y creación de listener para la ventana
    def controles(self, ventana, arriba, abajo, izquierda, derecha):
        ventana.listen()
        ventana.onkeypress(self.arriba, arriba)
        ventana.onkeypress(self.abajo, abajo)
        ventana.onkeypress(self.izquierda, izquierda)
        ventana.onkeypress(self.derecha, derecha)

    #Métodos de dirección
    def arriba(self):
        if self.cabeza.direction != "down":
            self.cabeza.direction = "up"
            self.cabeza.shape('img/POU1.gif')
    def abajo(self):
        if self.cabeza.direction != "up":
            self.cabeza.direction = "down"
            self.cabeza.shape('img/POU1.gif')
    def izquierda(self):
        if self.cabeza.direction != "right":
            self.cabeza.direction = "left"
            self.cabeza.shape('img/POU1.gif')
    def derecha(self):
        if self.cabeza.direction != "left":
            self.cabeza.direction = "right"
            self.cabeza.shape('img/POU1.gif')

    # Método principal de movimiento
    def movimiento(self, juego, screen):
        
        if self.cabeza.direction == "up":
            y = self.cabeza.ycor()
            if y < ((screen.lado/2)-50):
                self.cabeza.sety(y + 50)
            else:
                juego.perder = True

        if self.cabeza.direction == "down":
            y = self.cabeza.ycor()
            if y > (-(screen.lado/2)+50):
                self.cabeza.sety(y - 50)
            else:
                juego.perder = True

        if self.cabeza.direction == "left":
            x = self.cabeza.xcor()
            if x > (-(screen.lado/2)+50):
                self.cabeza.setx(x - 50)
            else:
                juego.perder = True
        if self.cabeza.direction == "right":
            x = self.cabeza.xcor()
            if x<((screen.lado/2)-50):
                self.cabeza.setx(x + 50)
            else:
                juego.perder = True
        self.cabeza.direction = "stop"
    
    # Método para agregar segmentos
    def agregarSegmentos(self):
        self.nuevo_segmento = turtle.Turtle()
        self.nuevo_segmento.speed(0)
        """self.nuevo_segmento.shape("circle")
        self.nuevo_segmento.color(self.colorSegmento)
        self.nuevo_segmento.penup()
        self.segmentos.append(self.nuevo_segmento)"""
      

    # Método para mover el resto del cuerpo
    def moverCuerpo(self):
        tamanio = len(self.segmentos)
        for i in range(tamanio -1, 0, -1):
            x = self.segmentos[i - 1].xcor()
            y = self.segmentos[i - 1].ycor()
            self.segmentos[i].goto(x,y)
        
        if tamanio > 0:
            x = self.cabeza.xcor()
            y = self.cabeza.ycor()
            self.segmentos[0].goto(x,y)

    # Comprueba si la serpiente colisiona consigo misma
    def colision(self, juego):
        for seg in self.segmentos:
            if seg.distance(self.cabeza) < 50:
                juego.alPerder(self)
