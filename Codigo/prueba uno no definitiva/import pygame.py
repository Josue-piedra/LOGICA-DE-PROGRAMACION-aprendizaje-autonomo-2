import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Rutas relativas para las fuentes
title_font_path = r"C:\Users\Josue\OneDrive\Desktop\LOGICA-DE-PROGRAMACION-aprendizaje-autonomo-2\Material\Fuente\ARCADE_N.TTF"
button_font_path = None  # O proporciona la ruta correcta si es necesario
title_font = pygame.font.Font(title_font_path, 80)
button_font = pygame.font.Font(button_font_path, 36)
title_font_in = pygame.font.Font(title_font_path, 40)
# Colores
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
    screen.fill(BLACK)
    show_text_with_outline(title_font, "Pong Game", WIDTH // 2, HEIGHT // 4 - 20, WHITE)

    play_button, play_hovered = create_button(button_font, "Jugar", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, RED, BLACK, WHITE, BLACK)
    instructions_button, instructions_hovered = create_button(button_font, "Instrucciones", WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 50, RED, BLACK, WHITE, BLACK)

    return play_button, instructions_button, play_hovered, instructions_hovered

# Función para la pantalla de instrucciones
def instructions_screen():
    screen.fill(BLACK)
    show_text_with_outline(title_font_in, "Instrucciones", WIDTH // 2, HEIGHT // 8, WHITE)

    instructions = [
        "Bienvenido al juego de Pong",
        "",
        " - Usa las teclas deflecha arriba y abajo para mover la paleta",
        "   del jugador 1 (izquierda).",
        " - Usa las teclas 'W' y 'S' para mover la paleta del jugador 2 (derecha).",
        " - Golpea la pelota con la paleta para evitar que alcance tu lado.",
        " - Gana puntos cada vez que la pelota pasa al lado opuesto.",
        " - El juego termina cuando un jugador alcanza 5 puntos.",
        "",
        "¡Buena suerte y diviértete!",
    ]

    for i, line in enumerate(instructions):
        show_text_with_outline(button_font, line, WIDTH // 2, HEIGHT // 4 + i * 30, WHITE)

    back_button, back_hovered = create_button(button_font, "Volver", WIDTH // 2 - 100, HEIGHT - 100, 200, 50, RED, BLACK, WHITE, BLACK)

    return back_button, back_hovered

# Configuración de las paletas y la pelota
paddle_width, paddle_height = 20, 100
ball_size = 20
paddle_speed = 5
ball_speed = 5

# Puntuación
score_player1 = 0
score_player2 = 0

# Función principal del juego
def pong_game(clock):
    global score_player1, score_player2

    # Inicialización de las paletas y la pelota
    player1 = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
    player2 = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
    ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
    ball_direction = [random.choice([1, -1]), random.uniform(-1, 1)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento de las paletas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.top > 0:
            player1.y -= paddle_speed
        if keys[pygame.K_s] and player1.bottom < HEIGHT:
            player1.y += paddle_speed

        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= paddle_speed
        if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
            player2.y += paddle_speed

        # Movimiento de la pelota
        ball.x += int(ball_speed * ball_direction[0])
        ball.y += int(ball_speed * ball_direction[1])

        # Colisiones con las paredes
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_direction[1] *= -1

        # Colisiones con las paletas
        if player1.colliderect(ball) or player2.colliderect(ball):
            ball_direction[0] *= -1

        # Anotación de puntos
        if ball.left <= 0:
            score_player2 += 1
            check_game_over(clock)
            reset_game(player1, player2, ball, ball_direction)
        elif ball.right >= WIDTH:
            score_player1 += 1
            check_game_over(clock)
            reset_game(player1, player2, ball, ball_direction)

        # Dibujar en la pantalla
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player1)
        pygame.draw.rect(screen, WHITE, player2)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Dibujar línea central
        pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

        # Dibujar puntuación
        font = pygame.font.Font(None, 36)
        score_display = font.render(f"{score_player1} - {score_player2}", True, WHITE)
        screen.blit(score_display, (WIDTH // 2 - score_display.get_width() // 2, 20))

        pygame.display.flip()
        clock.tick(60)

# Función para reiniciar el juego después de anotar un punto
def reset_game(player1, player2, ball):
    ball_direction = [random.choice([1, -1]), random.uniform(-1, 1)]
    ball.x = WIDTH // 2 - ball_size // 2
    ball.y = HEIGHT // 2 - ball_size // 2
    player1.y = HEIGHT // 2 - paddle_height // 2
    player2.y = HEIGHT // 2 - paddle_height // 2

# Función para verificar si el juego ha terminado
def check_game_over(clock=None):
    if score_player1 == 5 or score_player2 == 5:
        victory_result = victory_screen("Jugador 1" if score_player1 == 5 else "Jugador 2", clock)
        if victory_result == "play":
            reset_game(player1, player2, ball)
            pong_game(clock)
        elif victory_result == "quit":
            pygame.quit()
            sys.exit()
        elif victory_result == "return":
            start_screen()

# Función para la pantalla de victoria
def victory_screen(winner, clock):
    font = pygame.font.Font(None, 48)
    text = font.render(f"{winner} gana!", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    play_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 50, 150, 50)
    return_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 120, 150, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return "play"
                elif return_button.collidepoint(event.pos):
                    return "return"

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, play_button)
        pygame.draw.rect(screen, WHITE, return_button)
        pygame.draw.rect(screen, BLACK, play_button.inflate(-5, -5))
        pygame.draw.rect(screen, BLACK, return_button.inflate(-5, -5))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        play_text = font.render("Jugar", True, WHITE)
        return_text = font.render("Volver", True, WHITE)
        screen.blit(play_text, (WIDTH // 2 - play_text.get_width() // 2, HEIGHT // 2 + 65))
        screen.blit(return_text, (WIDTH // 2 - return_text.get_width() // 2, HEIGHT // 2 + 135))

        pygame.display.flip()
        clock.tick(60)
        
# Configuración de las paletas y la pelota
paddle_width, paddle_height = 20, 100
ball_size = 20
paddle_speed = 5
ball_speed = 5

# Puntuación
score_player1 = 0
score_player2 = 0

# Configuración inicial
running = True

# Bucle principal del juego
while running:
    play_button, instructions_button, play_hovered, instructions_hovered = start_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if play_button.collidepoint(x, y):
                print("¡Comienza el juego!")
                running = False
                clock = pygame.time.Clock()  # Inicializar el reloj
                pong_game(clock)  # Pasar el reloj como argumento a pong_game
            elif instructions_button.collidepoint(x, y):
                instructions_screen()

    pygame.display.flip()

# Salir del programa
pygame.quit()
sys.exit()