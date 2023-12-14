from typing import Any
import pygame


class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion):
        super().__init__()
        #cargamos la imagen
        self.fotos = [pygame.image.load("balonAntes.png"), pygame.image.load("balonDespues.png")]
        self.indice_image = 0
        self.image = self.fotos[self.indice_image]
        self.contador_fotos = 0
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizr la posicion del rectangulo para que councida con "posicion"
        self.rect.topleft = posicion

    #update
    def update(self, *args: Any, **kwargs: Any) -> None:
        teclas = args[0]
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()

        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
            self.rect.x = max(0, self.rect.x)
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 2
            self.rect.x = min(pantalla.get_width()-self.fotos.get_width(), self.rect.x)
        #gestionamos la animacion
        self.contador_fotos = (self.contador_fotos + 1) % 40
        self.indice_image = self.contador_fotos // 20
        self.image = self.fotos[self.indice_image]


class Enemigo(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion):
        super().__init__()
        #cargamos la imagen
        imagen = pygame.image.load("balonAntes.png")
        self.image = pygame.transform.rotate(imagen, 180)
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizr la posicion del rectangulo para que councida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y += 1