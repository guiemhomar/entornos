import pygame


class Nave:
    def __init__(self) -> None:
        pantalla = pygame.display.get_surface()
        imagenes = [pygame.image.load("messiAntes.png"),pygame.image.load("messiDespues.png"),pygame.image.load("cr7.png"),pygame.image.load("campo de futbol.png")]
        self.messi = [pygame.transform.scale(imagenes[0],(90, 90)), pygame.transform.scale(imagenes[1],(90, 90))]
        self.campo = pygame.transform.scale(imagenes[3], (800  ,600))
        self.cristiano = pygame.transform.scale(imagenes[2], (60, 60))
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

    def fondo(self):
        pantalla = pygame.display.get_surface()
        pantalla.blit(self.campo, (0, 0))
    
    def cr7(self):
        pantalla = pygame.display.get_surface()
        pantalla.blit(self.cristiano, (pantalla.get_height(), pantalla.get_height() - self.cristiano.get_height()))
