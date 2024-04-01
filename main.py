from encodings import CodecRegistryError
import pygame
from models.display import Display
from models.input import Movement
from models.input import Actions

pygame.init()


player_width = 60
player_height = 60
movement_speed = 5

width_display = 1920
height_display = 1200


# class Movement:
#     x_cord: int
#     y_cord: int
#     movement_speed: int
#     display: Display
#     player_width: int
#     player_height: int

# instaciate bullet at player x and y cords
#     will not be able to do anything but LRUD directions
# bullet moves n amount in certain direction every x frame



display = Display(width=width_display, height=height_display)
movement = Movement(
    x_cord=width_display/2,
    y_cord=height_display/2,
    movement_speed=movement_speed,
    display=display,
    player_height=player_height,
    player_width=player_width
)
actions = Actions()


win = pygame.display.set_mode((display.width, display.height))
pygame.display.set_caption("Pynding of Isaac")

clock = pygame.time.Clock()


def main():

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


# try stuff here

        win.fill((50, 50, 50))

        # draw player
        pygame.draw.rect(
            win, (255, 0, 0),
            (movement.x_cord,
             movement.y_cord,
             player_width,
             player_height)
        )

        


        movement.update(pygame.key.get_pressed())
        actions.update(win, pygame.key.get_pressed(), movement)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
