import pygame
from dataclasses import dataclass

from models.display import Display
from models.game_objects import Bullets

@dataclass
class Movement:
    x_cord: int
    y_cord: int
    movement_speed: int
    display: Display
    player_width: int
    player_height: int
    

    def update(self, keys):

        if keys[pygame.K_a] and self.left_check_out_of_bounds():
            self.x_cord -= self.movement_speed
        if  keys[pygame.K_d] and self.right_check_out_of_bounds():
            self.x_cord += self.movement_speed
        if keys[pygame.K_w] and self.top_check_out_of_bounds():
            self.y_cord -= self.movement_speed
        if keys[pygame.K_s] and self.bottom_check_out_of_bounds():
            self.y_cord += self.movement_speed 

    def bottom_check_out_of_bounds(self):
        return self.y_cord < self.display.height - self.player_height - self.movement_speed

    def top_check_out_of_bounds(self):
        return self.y_cord > self.movement_speed

    def right_check_out_of_bounds(self):
        return self.x_cord < self.display.width - self.player_width - self.movement_speed

    def left_check_out_of_bounds(self):
        return self.x_cord > self.movement_speed   
    


@dataclass
class Actions:
    
    bullets: Bullets = Bullets()

    def update(self, win, keys, movement):

        if keys[pygame.K_d]:
            self.bullets.shoot(win, "left", (movement.x_cord + (movement.player_width/2)), movement.y_cord)
        if keys[pygame.K_a]:
            self.bullets.shoot(win, "right", (movement.x_cord + (movement.player_width/2)), movement.y_cord)
        if keys[pygame.K_s]:
            self.bullets.shoot(win, "up", (movement.x_cord + (movement.player_width/2)), movement.y_cord)
        if keys[pygame.K_w]:
            self.bullets.shoot(win, "down", (movement.x_cord + (movement.player_width/2)), movement.y_cord) 
