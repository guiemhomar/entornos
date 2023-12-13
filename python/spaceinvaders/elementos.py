import pygame
import math

class Fondo:
    def __init__(self) -> None:
        #localizar la pantalla
        pantalla = pygame.display.get_surface()
        #cargamos la imagen
        imagen = pygame.image.load("campo de futbol.png")
        self.campo = pygame.transform.scale(imagen,(800,600))
        #scroll
        #self.scroll = 0
        #cuantas piezas de fondo necesitamos
        #self.piezas = math.ceil(pantalla.get_height() / self.campo.get_height()) +1

    def fons(self):
        #aumentar el scroll
        self.scroll += 1
        #localizar la pantalla
        pantalla = pygame.display.get_surface()
        #resetear el scroll
        if self.scroll > pantalla.get_width():
            self.scroll = 0
        #dibujamos el fondo
        for i in range(0,self.piezas):
            pantalla.blit(self.campo, (0, 0))
            #pantalla.blit(self.fondo, (0, - self.fondo.get.height() + i * self.fondo.get.height() + self.scroll))


        
        


class Nave:
    def __init__(self) -> None:
        pantalla = pygame.display.get_surface()
        imagenes = [pygame.image.load("messiAntes.png"),pygame.image.load("messiDespues.png"),pygame.image.load("cr7.png"), pygame.image.load("balonAntes.png"), pygame.image.load("balonDespues.png")]
        self.messi = [pygame.transform.scale(imagenes[0],(90, 90)), pygame.transform.scale(imagenes[1],(90, 90))]
        self.cristiano = pygame.transform.scale(imagenes[2], (60, 60))
        #self.balon = [pygame.transform.scale(imagenes[3],(90, 90)), pygame.transform.scale(imagenes[4],(90, 90))]
        self.x = pantalla.get_width() // 2 - self.messi[0].get_width() // 2
        self.y = 0
        self.contador = 0
        
        
    def moverDerecha(self):
        velocidad = 4
        self.x += velocidad
        self.x += 1
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width()
        self.x = min(self.x, limite - self.messi[0].get_width())
        
    def moverIzquierda(self):
        velocidad = 4
        self.x -= velocidad
        self.x -= 1
        limite = 0
        self.x = max(self.x, limite)
        
    def Messi(self):
        #aumento el contador
        self.contador = (self.contador + 1) % 40
        pantalla = pygame.display.get_surface()
        
        #seleccionar la imagen que toca
        seleccionada = self.contador // 20
        pantalla.blit(self.messi[seleccionada], (self.x, self.y))
    
    def cr7(self):
        pantalla = pygame.display.get_surface()
        pantalla.blit(self.cristiano, (pantalla.get_width() - self.cristiano.get_width(), pantalla.get_height() - self.cristiano.get_height()))

    #def pelota(self):
        #aumento el contador
        #self.contador = (self.contador + 1) % 40
        #pantalla = pygame.display.get_surface()
        
        #seleccionar la imagen que toca
        #seleccionada = self.contador // 20
        #pantalla.blit(self.balon[seleccionada], (self.x, self.y))    

    #cristiano abaix a la dreta, perque amb es pantalla width no funciona, pero si pos height si que se posa