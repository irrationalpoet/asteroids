from typing import override
from pygame import Vector2, Surface, draw
import circleshape
from constants import PLAYER_RADIUS, LINE_WIDTH

class Player(circleshape.CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0

    def triangle(self) -> list[Vector2]:
        forward: Vector2 = Vector2(0,1).rotate(self.rotation)
        right: Vector2 = Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a: Vector2 = self.position + forward * self.radius
        b: Vector2 = self.position - forward * self.radius - right
        c: Vector2 = self.position - forward * self.radius + right
        return [a, b, c]
    
    @override
    def draw(self, screen: Surface) -> None:
        color: str = "white"
        points: list[Vector2] = self.triangle()
        width: int = LINE_WIDTH
        draw.polygon(screen, color, points, width)

