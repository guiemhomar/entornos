import pygame

class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion) -> None:
        super().__init__()
        #cargamos la imagen
        self.image = pygame.transform.scale(pygame.image.load("messipixel.png"), (90, 90))
        self.mask = pygame.mask.from_surface(self.image)
        self.contador_imagen = 0
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion
        self.ultimo_disparo = 0
        #creamos las vidas
        self.vidas = 3
        #hacemos que parpadee al perder una vida
        self.parpadear = False
        self.tiempo_parpadear = pygame.time.get_ticks()

    def perder_vida(self):
        if self.vidas > 0:
            self.vidas -= 1
            
    
    
    def disparar(self, grupo_sprites_todos, grupo_sprites_bala):
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimo_disparo + 200:
            bala = Bala((self.rect.x + self.image.get_width() / 2, self.rect.y + self.image.get_width() / 2))
            grupo_sprites_bala.add(bala)
            grupo_sprites_todos.add(bala)
            self.ultimo_disparo = momento_actual

    #update
    def update(self, *args: any, **kwargs: any) -> None:
        teclas = args[0]
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        #capturamos todos
        grupo_sprites_todos = args[1]
        #capturamos balas
        grupo_sprites_bala = args[2]
        #gestionamos la teclas
            
        
        if self.parpadear:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual % 200 < 100:
                self.image = pygame.Surface((1,1)) #imagen invisible
            else:
                self.image = pygame.transform.scale(pygame.image.load("messipixel.png"), (60, 60))
                #reiniciar parpadeo
                if tiempo_actual - self.tiempo_parpadear > 1000: #duracion
                    self.parpadear = False
        else:
            self.image = pygame.transform.scale(pygame.image.load("messipixel.png"), (60, 60))

        
        if teclas[pygame.K_a]:
            self.rect.x -= 16
            self.rect.x = max(0, self.rect.x)
        if teclas[pygame.K_d]:
            self.rect.x += 16
            self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        if teclas[pygame.K_w]:
            self.rect.y -=16
        if teclas [pygame.K_s]:
            self.rect.y +=16    

            
        #gestionamos la animación
        self.contador_imagen = (self.contador_imagen + 5) % 40
        # self.image = pygame.transform.scale(pygame.image.load("messipixel.png"), (90, 90))
        
        #Capturar grupo sprites enemigos 3
        grupo_sprites_enemigos = args[3]
        
        #variable running
        running = args[4]
        
        #detectar colisiones
        enemigo_colision = pygame.sprite.spritecollideany(self, grupo_sprites_enemigos, pygame.sprite.collide_mask)
        if enemigo_colision:
            enemigo_colision.kill()
            if self.vidas > 0:
                #le quitamos vidas hasta llegar a 0
                self.vidas -=1
                self.parpadear = True
                self.tiempo_parpadear = pygame.time.get_ticks()
                
            else:
                #cuando vidas = a 0 --> cerrar el juego
                running[0] = False

        
#creador de enemigos
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        #cargamos la imagen
        imagen = [pygame.image.load("cr7pixel.png"), ]
        imagen2 = pygame.transform.scale(imagen, (60, 90))
        self.image = pygame.transform.rotate(imagen2, 0)
        self.mask = pygame.mask.from_surface(self.image)
        #creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        #actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion

    def update(self, *args: any, **kwargs: any):
        pantalla = pygame.display.get_surface()
        self.rect.y += 5
        self.rect.x = max(0, self.rect.x)
        self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
        if (self.rect.y > pantalla.get_height()):
            self.kill()

        #capturar arg 2 bala
        grupo_sprites_bala = args[2]
        grupo_sprites_todos = args[1]
        bala_colision = pygame.sprite.spritecollideany(self, grupo_sprites_bala, pygame.sprite.collide_mask)
        if bala_colision:
            self.kill()
            bala_colision.kill()


class Fondo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        # cargamos la imagen
        imagen = pygame.image.load("fondo.png")
        pantalla = pygame.display.get_surface()
        #transformar la imagen
        self.image = pygame.transform.scale(imagen, (700, 800))
        #pantalla
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height()))
        # creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizar la posición del rectangulo para que coincida con "posicion"
        self.rect.topleft = (0, 0)

    #def update(self, *args: any, **kwargs: any) -> None:
      #self.rect.y +=1
      #capturamos pantalla
      #pantalla = pygame.display.get_surface()
      #if self.rect.y >= pantalla.get_height():
          #self.rect.y = - pantalla.get_height()

class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image_original = pygame.image.load("balon.png")
        self.image = pygame.transform.scale(self.image_original, (20, 20))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion
        self.velocidad = 26

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.y -= self.velocidad