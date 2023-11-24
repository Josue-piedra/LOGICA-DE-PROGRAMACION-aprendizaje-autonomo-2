import pygame
import sys

pygame.init()

#Tamaño de la pantalla 
screen_width = 800
screen_height = 600

window_size = (screen_width, screen_height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pong")

#Imagen de fondo
image_path = r"C:\Users\Josue\OneDrive\Desktop\LOGICA DE PROGRAMACION - 1-SI-ELMD-A - 220242\Material\Imagenes\Fondos\JPG\Fondo.jpg"
background_image = pygame.image.load(image_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

#Tamaño de la pantalla donde se vera el juego
game_area_width = 690
game_area_height = 490

game_area_x = (screen_width - game_area_width) // 2
game_area_y = (screen_height - game_area_height) // 2

#Imagenes de botonos para el juego
button_normal = pygame.image.load(r"C:\Users\Josue\OneDrive\Desktop\LOGICA DE PROGRAMACION - 1-SI-ELMD-A - 220242\Material\Imagenes\Botones\PNG\Boton 1.png")
button_hover = pygame.image.load(r"C:\Users\Josue\OneDrive\Desktop\LOGICA DE PROGRAMACION - 1-SI-ELMD-A - 220242\Material\Imagenes\Botones\PNG\Boton2.png")
button_rect = button_normal.get_rect()

#animacion del los botones
animation_duration = 300
start_time = pygame.time.get_ticks()
animation_active = False

#Condiciones del para las diferentesfunciones del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                print("¡Comming soon!")
                start_time = pygame.time.get_ticks()
                animation_active = True

    if animation_active:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        alpha = min(255, elapsed_time / animation_duration * 255)
        button_hover.set_alpha(alpha)

        screen.blit(background_image, (0, 0))
        screen.blit(button_hover, button_rect)
        pygame.display.flip()

        if elapsed_time >= animation_duration:
            animation_active = False
    else:
        screen.blit(background_image, (0, 0))
        screen.blit(button_normal, button_rect)
        pygame.display.flip()

    pygame.time.Clock().tick(60)

