import pygame
from logger import log_state
import constants
from player import Player


def main() -> None:
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0
    
    player: Player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)

        screen.fill(color="black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
