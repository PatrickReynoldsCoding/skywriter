# class bullet

import pygame
from dataclasses import dataclass

@dataclass
class Bullet:
    direction: str
    x_cord: int
    y_cord: int
    speed: int = 50

class Bullets:
    bullets: list[Bullet] = []

    bullet_size = 5


    def shoot(self, win, direction, x_cord, y_cord):
        
        self.bullets.append(Bullet(direction, x_cord, y_cord))

        for bullet in self.bullets:
            if direction == "up":
                updated_location = bullet.y_cord - 30
                bullet.y_cord = updated_location
            if direction == "down":
                updated_location = bullet.y_cord + 30
                bullet.y_cord = updated_location
            if direction == "left":
                updated_location = bullet.x_cord - 30
                bullet.x_cord = updated_location
            if direction == "right":
                updated_location = bullet.x_cord + 30
                bullet.x_cord = updated_location
            pygame.draw.circle(win, (255, 255, 255), (bullet.x_cord, bullet.y_cord), self.bullet_size)

