import pygame
from pygame.sprite import AbstractGroup
from imagepath import imagepath

#petals for flower, level 1 stuff

#reference from sokoban 

class Petal(pygame.sprite.Sprite):
    def __init__(self, pos = (0, 0)):
        super().__init__()
        self.image = imagepath("petal.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


# later method for updating the image when in different areas of map and or moving
        





