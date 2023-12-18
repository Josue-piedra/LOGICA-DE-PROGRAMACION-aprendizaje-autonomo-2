import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Configuración de las paletas y la pelota
paddle_width, paddle_height = 20, 100
ball_size = 20
paddle_speed = 5
ball_speed = 5

# Puntuación
score_player1 = 0
score_player2 = 0

# Instrucciones
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

# Función principal del juego
def pong_game():
    global score_player1, score_player2

    # Inicialización de las paletas y la pelota
    player1 = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
    player2 = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
    ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
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
        if keys[pygame.K_s] and player1.bottom < height:
            player1.y += paddle_speed

        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= paddle_speed
        if keys[pygame.K_DOWN] and player2.bottom < height:
            player2.y += paddle_speed

        # Movimiento de la pelota
        ball.x += int(ball_speed * ball_direction[0])
        ball.y += int(ball_speed * ball_direction[1])

        # Colisiones con las paredes
        if ball.top <= 0 or ball.bottom >= height:
            ball_direction[1] *= -1

        # Colisiones con las paletas
        if player1.colliderect(ball) or player2.colliderect(ball):
            ball_direction[0] *= -1

        # Anotación de puntos
        if ball.left <= 0:
            score_player2 += 1
            check_game_over()
            reset_game(player1, player2, ball, ball_direction)
        elif ball.right >= width:
            score_player1 += 1
            check_game_over()
            reset_game(player1, player2, ball, ball_direction)

        # Dibujar en la pantalla
        screen.fill(black)
        pygame.draw.rect(screen, white, player1)
        pygame.draw.rect(screen, white, player2)
        pygame.draw.ellipse(screen, white, ball)

        # Dibujar línea central
        pygame.draw.line(screen, white, (width // 2, 0), (width // 2, height), 2)

        # Dibujar puntuación
        font = pygame.font.Font(None, 36)
        score_display = font.render(f"{score_player1} - {score_player2}", True, white)
        screen.blit(score_display, (width // 2 - score_display.get_width() // 2, 20))

        pygame.display.flip()
        clock.tick(60)

# Función para reiniciar el juego después de anotar un punto
def reset_game(player1, player2, ball, ball_direction):
    global ball_speed

    ball_direction = [random.choice([1, -1]), random.uniform(-1, 1)]
    ball.x = width // 2 - ball_size // 2
    ball.y = height // 2 - ball_size // 2
    player1.y = height // 2 - paddle_height // 2
    player2.y = height // 2 - paddle_height // 2


# Función para verificar si el juego ha terminado
def check_game_over():
    global score_player1, score_player2, ball_speed

    if score_player1 == 5 or score_player2 == 5:
        victory_result = victory_screen("Jugador 1" if score_player1 == 5 else "Jugador 2")
        if victory_result == "play":
            score_player1 = 0
            score_player2 = 0
            ball_speed = 5
            pong_game()
        elif victory_result == "quit":
            pygame.quit()
            sys.exit()
        elif victory_result == "return":
            start_screen()

# Pantalla de inicio
def start_screen():
    global score_player1, score_player2

    score_player1 = 0
    score_player2 = 0

    font = pygame.font.Font(r"C:\Users\Josue\OneDrive\Desktop\LOGICA-DE-PROGRAMACION-aprendizaje-autonomo-2\Material\Fuente\ARCADE_N.TTF", 80)
    text = font.render("Pong Game", True, white)
    text_rect = text.get_rect(center=(width // 2, height // 2 - 50))

    play_button = pygame.Rect(width // 2 - 75, height // 2 + 50, 150, 50)
    instructions_button = pygame.Rect(width // 2 - 100, height // 2 + 120, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and play_button.collidepoint(event.pos):
                pong_game()
            elif event.type == pygame.MOUSEBUTTONDOWN and instructions_button.collidepoint(event.pos):
                instructions_screen()

        screen.fill(black)
        pygame.draw.rect(screen, white, play_button)
        pygame.draw.rect(screen, white, instructions_button)
        pygame.draw.rect(screen, black, play_button.inflate(-5, -5))
        pygame.draw.rect(screen, black, instructions_button.inflate(-5, -5))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        play_text = font.render("Jugar", True, white)
        instructions_text = font.render("Instrucciones", True, white)
        screen.blit(play_text, (width // 2 - play_text.get_width() // 2, height // 2 + 65))
        screen.blit(instructions_text, (width // 2 - instructions_text.get_width() // 2, height // 2 + 135))

        pygame.display.flip()
        clock.tick(60)

# Pantalla de instrucciones
def instructions_screen():
    font = pygame.font.Font(None, 24)
    text_objects = [font.render(line, True, white) for line in instructions]
    text_rects = [text_object.get_rect(center=(width // 2, y)) for y, text_object in zip(range(50, height - 50, 30), text_objects)]

    return_button = pygame.Rect(width // 2 - 75, height - 80, 150, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and return_button.collidepoint(event.pos):
                start_screen()

        screen.fill(black)
        for text_object, rect in zip(text_objects, text_rects):
            screen.blit(text_object, rect)

        pygame.draw.rect(screen, white, return_button)
        pygame.draw.rect(screen, black, return_button.inflate(-5, -5))
        return_text = font.render("Volver", True, white)
        screen.blit(return_text, (width // 2 - return_text.get_width() // 2, height - 70))

        pygame.display.flip()
        clock.tick(60)

# Función para la pantalla de victoria
def victory_screen(winner):
    font = pygame.font.Font(None, 48)
    text = font.render(f"{winner} gana!", True, white)
    text_rect = text.get_rect(center=(width // 2, height // 2 - 50))
    play_button = pygame.Rect(width // 2 - 75, height // 2 + 50, 150, 50)
    return_button = pygame.Rect(width // 2 - 75, height // 2 + 120, 150, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return "play"
                elif return_button.collidepoint(event.pos):
                    return "return"

        screen.fill(black)
        pygame.draw.rect(screen, white, play_button)
        pygame.draw.rect(screen, white, return_button)
        pygame.draw.rect(screen, black, play_button.inflate(-5, -5))
        pygame.draw.rect(screen, black, return_button.inflate(-5, -5))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        play_text = font.render("Jugar", True, white)
        return_text = font.render("Volver", True, white)
        screen.blit(play_text, (width // 2 - play_text.get_width() // 2, height // 2 + 65))
        screen.blit(return_text, (width // 2 - return_text.get_width() // 2, height // 2 + 135))

        pygame.display.flip()
        clock.tick(60)

# Pantalla de inicio
start_screen()
pygame.quit()
sys.exit()
