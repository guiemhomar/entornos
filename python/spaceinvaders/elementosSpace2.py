from typing import Any
import pygame


class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion):
        super().__init__()
        #cargamos la imagen
        self.image = pygame.image.load("balonAntes.png")
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizr la posicion del rectangulo para que councida con "posicion"
        self.rect.topleft = posicion

    #update
    def update(self, *args: Any, **kwargs: Any) -> None:
        teclas = args[0]
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 2
        pass