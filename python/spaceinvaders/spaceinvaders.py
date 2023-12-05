import pygame
import elementos

pygame.init()
pantalla = pygame.display.set_mode((800,600))

salir = False

clock = pygame.time.Clock()
FPS = 60

nave = elementos.Nave()


while not salir:
    clock.tick(FPS)
   
    #gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
 
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        nave.moverIzquierda()
    if teclas[pygame.K_RIGHT]:
        nave.moverDerecha()
    
    

    #gestionar cambios
    pantalla.fill((255,255,255))

    nave.fondo()
    nave.Messi()
    nave.cr7()

    #redibujar el juego
    pygame.display.flip()

pygame.quit()