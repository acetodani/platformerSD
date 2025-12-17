import sys
import pygame

WIDTH, HEIGHT = 800, 800
FPS = 60
BG_COLOR = (30, 30, 40)
WHITE = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PlatformerSD")
    clock = pygame.time.Clock()
    
    square_rect = pygame.Rect(100, 100, 50, 50) 


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(BG_COLOR)

        # TODO: draw game objects here

        pygame.draw.rect(screen, WHITE, square_rect, 0) 
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()