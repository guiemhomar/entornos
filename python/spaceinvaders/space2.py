import pygame
import elementosSpace2

#inicializamos el juego
pygame.init()

#creamos la pantalla
tamanyo = (800,600)
pantalla = pygame.display.set_mode(tamanyo) # = (800,600)

#creamos un relok
reloj = pygame.time.Clock()
FPS = 60

#booleano de control
running = True

#crear la nave
posicion = (200,200)
nave = elementosSpace2.Nave(posicion)
#nave = elementosspace.Nave((200,200))

#crear un grupo de sprites
grupo_sprites = pygame.sprite.Group(nave)
grupo_sprites.add(elementosSpace2.Nave((300,100)))
grupo_sprites.add(elementosSpace2.Nave((400,100)))
grupo_sprites.add(elementosSpace2.Nave((500,100)))


#bucle principal

while running:
    #limitamos el bucle a framerate que hemos definido
    reloj.tick(FPS)
    
    #gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fondo blanco
    pantalla.fill((255,255,255))
    
    teclas = pygame.key.get_pressed()
    #segundo sprites
    

    #pintaremos
    grupo_sprites.update(teclas)
    grupo_sprites.draw(pantalla)

    #redibujar la pantalla
    pygame.display.flip()

#finalizamos el juego
pygame.quit()