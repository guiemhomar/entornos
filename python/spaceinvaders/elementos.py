import pygame


class Nave:
    def __init__(self) -> None:
        self.x = 30
        self.y = 30
        self.imagenes = [pygame.image.load("messiAntes.png"),pygame.image.load("messiDespues.png")]
        self.contador = 0
   
    def moverDerecha(self):
        self.x += 1
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width()
        self.x = min(self.x, limite - self.imagenes[0].get_width())


    def moverIzquierda(self):
        self.x -= 1
        pantalla = pygame.display.get_surface()
        limite = 0
        self.x = max(self.y, limite)


    def dibujar(self):
        #aumento el contador
        self.contador = (self.contador + 1) % 40
        pantalla = pygame.display.get_surface()
        #cojo el puntero a la pantalla
        pantalla.blit(self.imagenes, (self.x, self.y))
        #seleccionar la imagen que toca
        seleccionada = self.contador // 20
        pantalla.blit(self.imagenes[seleccionada], (self.x, self.y))
