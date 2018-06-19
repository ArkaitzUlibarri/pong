import os, sys, pygame
import random
from random import randint
from pad import Pad
from ball import Ball
from score import Score
import datetime
import tkinter

def main():
    pygame.init()

    size = width, height = 800, 600

    screen = pygame.display.set_mode(size) #crear el canvas dónde vamos a dibujar los diferentes objetos del videojuego
    pygame.display.set_caption('Pong') #cambiar el título de la ventana

    # Background
    try:
        basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = os.path.join(basepath,'assets','graphics','background.png')
        background = pygame.image.load(filename) #carga la imagen de fondo desde el disco duro
        background = background.convert() #realizamos una conversión del formato de los pixeles a canvas

    except pygame.error as e:
        raise SystemExit(str(e))

    # Ball and Pads
    pad_left = Pad((width/6, height/4))
    pad_right = Pad((5*width/6, 3*height/4))
    ball = Ball((width/2, height/2))

    # Scoreboard
    if not pygame.font:
        raise SystemExit('Pygame does not support fonts')

    try:
        filename = os.path.join(basepath,'assets','fonts','wendy.ttf')
        font = pygame.font.Font(filename, 90)

    except pygame.error as e:
        raise SystemExit(str(e))

    left_score = Score(font, (width/3, height/8))
    right_score = Score(font, (2*width/3, height/8))

    #Group elements
    sprites = pygame.sprite.Group(pad_left, pad_right, ball, left_score, right_score)

    #Declarar reloj
    clock = pygame.time.Clock()
    fps = 60
    pygame.key.set_repeat(1, 1000 // fps) #continua registrando eventos del teclado mientras mantenemos presionada una determinada tecla

    #Limitar el movimiento de la bola
    top = pygame.Rect(0, 0, width, 5)
    bottom = pygame.Rect(0, height-5, width, 5)
    left = pygame.Rect(0, 0, 5, height)
    right = pygame.Rect(width-5, 0, 5, height)

    while 1:

        # Ejecuta el siguiente frame
        clock.tick(fps) 

        #Parar raquetas
        pad_left.stop()
        pad_right.stop()

        #Event Handling
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            pad_left.move_up()

        if keys[pygame.K_s]:
            pad_left.move_down()

        if keys[pygame.K_UP]:
            pad_right.move_up()

        if keys[pygame.K_DOWN]:
            pad_right.move_down()

        if keys[pygame.K_SPACE] and ball.isStopped():
            ball.start( random.choice([-1,1]) * randint(1, 4), random.choice([-1,1]) * randint(1, 4))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #Detectar colisiones
        if ball.rect.colliderect(top) or ball.rect.colliderect(bottom):
            ball.change_y()
        elif (ball.rect.colliderect(pad_left.rect) or ball.rect.colliderect(pad_right.rect)):
            ball.change_x()
        elif ball.rect.colliderect(left):
            right_score.score_up()
            ball.reset()
            ball.stop()
        elif ball.rect.colliderect(right):
            left_score.score_up()
            ball.reset()
            ball.stop()
            
        #Limitamos el movimiento de las raquetas dentro del rectangulo
        screen_rect = screen.get_rect().inflate(0, -10)
        pad_left.rect.clamp_ip(screen_rect)
        pad_right.rect.clamp_ip(screen_rect)

        sprites.update() #actualice y dibuje en pantalla todos los sprites
        screen.blit(background, (0, 0)) #copia los pixeles contenidos en la imagen de fondo sobre el canvas
        sprites.draw(screen)
        pygame.display.flip() #hacer un cambio de buffers

#Llamamos al main cuando se invoca el archivo como un programa
if __name__ == '__main__':
    os.system("cls")    # Clear console
    print ("Start: "+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    main()
    print ("End: "+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))