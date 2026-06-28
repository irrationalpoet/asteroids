import pygame
from logger import log_state
import constants


def main() -> None:
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)



if __name__ == "__main__":
    main()
