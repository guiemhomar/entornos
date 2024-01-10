from typing import Any
import pygame
from pygame.sprite import Group


class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion):
        super().__init__()
        #cargamos la imagen
        self.fotos = [pygame.image.load("balonAntes.png"), pygame.image.load("balonDespues.png")]
        self.indice_image = 0
        self.image = self.fotos[self.indice_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.contador_fotos = 0
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizr la posicion del rectangulo para que councida con "posicion"
        self.rect.topleft = posicion
        self.ultimo_disparo = 0

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
            self.rect.x = min(pantalla.get_width()-self.image.get_width(), self.rect.x)
        #gestionamos la animacion
        self.contador_fotos = (self.contador_fotos + 1) % 40
        self.indice_image = self.contador_fotos // 20
        self.image = self.fotos[self.indice_image]
        #capturamos grupo_sprites_enemigos
        grupo_sprites_enemigos = args[3]
        #capturamos la variable de control running
        running = args [4]
        #detectar colisiones con enemigos
        enemigo_colision = pygame.sprite.spritecollideany(self, grupo_sprites_enemigos, pygame.sprite.collide_mask)
        if enemigo_colision:
            enemigo_colision.kill()
            running[0] = False
    
    
    def disparar(self,grupo_sprites):
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimo_disparo + 200:
            bala = Bala((self.rect.x + self.image.get_width() / 2, self.rect.y))
            grupo_sprites.add(bala)
            self.ultimo_disparo = momento_actual


class Enemigo(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion):
        super().__init__()
        #cargamos la imagen
        imagen = pygame.image.load("balonAntes.png")
        self.image = pygame.transform.rotate(imagen, 180)
        self.mask = pygame.mask.from_surface(self.image)
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizr la posicion del rectangulo para que councida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y += 1
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        if (self.rect.y > pantalla.get_height()):
            self.kill()
    
class Fondo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        #cargamos la imagen
        imagen = pygame.image.load("campo de futbol.png")
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height()))
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizr la posicion del rectangulo para que councida con "posicion"
        self.rect.topleft = (0,0)

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y += 1
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        if self.rect.y >= pantalla.get_height():
                self.rect.y = - pantalla.get_height()
        

class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        #creamos un rectangulo
        self.image = pygame.Surface((5,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y -= 5

    