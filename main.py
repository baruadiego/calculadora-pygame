import pygame

def main():
    """
    Función principal que ejecuta el juego del AHORCADO.

    Inicializa la ventana de Pygame, ejecuta el menú principal, el juego, la pantalla para ingresar el nickname,
    y guarda el puntaje del jugador en un archivo JSON.
    """
    SCREEN_WIDTH = 320
    SCREEN_HEIGHT = 470
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("CALCULADORA")
    pygame.init()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))
        pygame.display.update()
    
main()