import pygame
import elementosSpace2
import random
import pygame_menu

#inicializamos el juego
pygame.init()

#creamos la pantalla
tamanyo = (800,600)
pantalla = pygame.display.set_mode(tamanyo) # = (800,600)

#creamos un relok
reloj = pygame.time.Clock()
FPS = 60

#creamos una fuente para la pausa
font = pygame.font.Font(None,30)

#booleano de control
running = [True]

##crear la nave
posicion = (200,200)
nave = elementosSpace2.Nave(posicion)
#nave = elementosspace.Nave((200,200))

#crear un grupo de sprites
grupo_sprites = pygame.sprite.Group(nave)
fondo = elementosSpace2.Fondo()
grupo_sprites.add(fondo)
grupo_sprites.add(elementosSpace2.Nave((300,100)))
grupo_sprites.add(elementosSpace2.Nave((400,100)))
grupo_sprites.add(elementosSpace2.Nave((500,100)))

enemigo = elementosSpace2.Enemigo((50,50))
grupo_sprites.add(enemigo)

nave = elementosSpace2.Nave((550,700))


#crear una variable que almacene la ultima vez que se creo un enemigo
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigo = 2000

def set_difficulty(value, difficulty):
    global frecuencia_creacion_enemigo
    frecuencia_creacion_enemigo = difficulty

def start_the_game():
    
    #booleano de control
    running = [True]

    global ultimo_enemigo_creado
    global reloj
    global frecuencia_creacion_enemigo
    global FPS
    
    nave = elementosSpace2.Nave((550,700))

    grupo_sprites_todos = pygame.sprite.Group()
    grupo_sprites_enemigos = pygame.sprite.Group()
    grupo_sprites_balas = pygame.sprite.Group()

    grupo_sprites_todos.add(elementosSpace2.Fondo((0,0)))
    grupo_sprites_todos.add(elementosSpace2.Fondo((0,-pantalla.get_height())))
    grupo_sprites_todos.add(nave)

    pausado = False

    
    #bucle principal
    while running[0]:
        #limitamos el bucle a framerate que hemos definido
        reloj.tick(FPS)
    
        #gestionar la salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #creacion de enemigos
        momento_actual = pygame.time.get_ticks()
        if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
            coordX = random.randint(0, pantalla.get_width())
            coordY = -200
            #creamos el enemigo
            enemigo = elementosSpace2.Enemigo((coordX,coordY))
            #lo añadimos a los dos grupos:todos y enemigos
            grupo_sprites_todos.add(enemigo)
            grupo_sprites_enemigos.add(enemigo)
            #actualizamos el momento del ultimo enemigo creado
            ultimo_enemigo_creado = momento_actual
            #grupo_sprites.add(elementosSpace2.Enemigo((random.randint(0,pantalla.get_width()),0)))
            

        #capturamos las teclas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            nave.disparar(grupo_sprites)
        if teclas[pygame.K_LSHIFT]:
            pausado = not pausado
        
        #capturamos las teclas
        #teclas = pygame.key.get_pressed()
        #if teclas[pygame.K_ESCAPE]:
       #running[0] = False
    
        #fondo blanco
        pantalla.fill((255,255,255))
    
        teclas = pygame.key.get_pressed()
        #segundo sprites
        if not pausado:
             #creacion de enemigos
            momento_actual = pygame.time.get_ticks()
            if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigo):
                coordX = random.randint(0, pantalla.get_width())
                coordY = -200
                #creamos el enemigo
                enemigo = elementosSpace2.Enemigo((coordX,coordY))
                #lo añadimos a los dos grupos:todos y enemigos
                grupo_sprites_todos.add(enemigo)
                grupo_sprites_enemigos.add(enemigo)
                #actualizamos el momento del ultimo enemigo creado
                ultimo_enemigo_creado = momento_actual
                #grupo_sprites.add(elementosSpace2.Enemigo((random.randint(0,pantalla.get_width()),0)))
             
            #actualizamos los sprites
            grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas)
        
    
        #dibujamos los sprites ne pantalla
        grupo_sprites_todos.draw(pantalla)

        #si pausado, escribirlo
        if pausado:
            texto = font.render("Pausa", True, "White")
            pantalla.blit(texto, (pantalla.get_width() / 2, pantalla.get_height()/2))

        #pintaremos
        grupo_sprites.update(teclas)
        grupo_sprites.draw(pantalla)

        #redibujar la pantalla
        pygame.display.flip()
        

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 200), ('Easy', 2000)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(pantalla)

#finalizamos el juego
pygame.quit()