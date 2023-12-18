import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Fuente estilo arcade para el título y botones
title_font = pygame.font.Font(r"C:\Users\Josue\OneDrive\Desktop\LOGICA-DE-PROGRAMACION-aprendizaje-autonomo-2\Material\Fuente\ARCADE_N.TTF", 80)
button_font = pygame.font.Font(None, 36)
title_font_in = pygame.font.Font(r"C:\Users\Josue\OneDrive\Desktop\LOGICA-DE-PROGRAMACION-aprendizaje-autonomo-2\Material\Fuente\ARCADE_N.TTF", 40)
# Colores
GRAY = (169, 169, 169)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Función para mostrar texto en la pantalla con contorno
def show_text_with_outline(font, text, x, y, color=WHITE, outline_color=BLACK):
    text_surface = font.render(text, True, color)
    outline_surface = font.render(text, True, outline_color)

    text_rect = text_surface.get_rect(center=(x, y))
    outline_rect = outline_surface.get_rect(center=(x, y))

    screen.blit(outline_surface, outline_rect.move(2, 2))  # Desplazar para crear el contorno
    screen.blit(text_surface, text_rect)

# Función para crear un botón
def create_button(font, text, x, y, width, height, base_color, hover_color, text_color, border_color, action=None):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, base_color, button_rect, border_radius=10)
    pygame.draw.rect(screen, border_color, button_rect, width=2, border_radius=10)

    show_text_with_outline(font, text, x + width // 2, y + height // 2, text_color)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    is_button_hovered = button_rect.collidepoint(mouse_x, mouse_y)

    if is_button_hovered:
        pygame.draw.rect(screen, hover_color, button_rect, border_radius=10)

    return button_rect, is_button_hovered

# Función para la pantalla de inicio
def start_screen():
    screen.fill(GRAY) 
    # Mostrar título 
    show_text_with_outline(title_font, "Pong Game", WIDTH // 2, HEIGHT // 4 - 20, WHITE)

    # Mostrar botones "Jugar" e "Instrucciones"
    play_button, play_hovered = create_button(button_font, "Jugar", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, RED, BLACK, WHITE, BLACK)
    instructions_button, instructions_hovered = create_button(button_font, "Instrucciones", WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 50, RED, BLACK, WHITE, BLACK)

    return play_button, instructions_button, play_hovered, instructions_hovered

# Función para la pantalla de instrucciones
def instructions_screen():
    screen.fill(GRAY)  # Fondo gris
    show_text_with_outline(title_font_in, "Instrucciones", WIDTH // 2, HEIGHT // 8, WHITE)

    # Mostrar las instrucciones en esta pantalla
    instructions = [
        "Bienvenido al juego de Pong",
        "",
        " - Usa las teclas de flecha arriba y abajo para mover las paletas.",
        " - Golpea la pelota con tu paleta y evita que tu oponente lo haga.",
        " - ¡Gana puntos cada vez que la pelota pasa a tu oponente!"
    ]

    for i, line in enumerate(instructions):
        show_text_with_outline(button_font, line, WIDTH // 2, HEIGHT // 4 + i * 30, WHITE)

    # Mostrar botón para regresar a la pantalla anterior
    back_button, back_hovered = create_button(button_font, "Volver", WIDTH // 2 - 100, HEIGHT - 100, 200, 50, RED, BLACK, WHITE, BLACK)

    return back_button, back_hovered

# Bucle principal
current_screen = "start_screen"
running = True
while running:
    if current_screen == "start_screen":
        play_button, instructions_button, play_hovered, instructions_hovered = start_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Verificar clic en el botón de Jugar
                if play_button.collidepoint(x, y):
                    print("¡Comienza el juego!")
                    running = False
                # Verificar clic en el botón de Instrucciones
                elif instructions_button.collidepoint(x, y):
                    current_screen = "instructions_screen"

    elif current_screen == "instructions_screen":
        back_button, back_hovered = instructions_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Verificar clic en el botón de Volver
                if back_button.collidepoint(x, y):
                    current_screen = "start_screen"

    pygame.display.flip()

# Salir del programa
pygame.quit()
sys.exit()
