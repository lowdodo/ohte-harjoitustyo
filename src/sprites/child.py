import pygame
from pygame.sprite import AbstractGroup
from imagepath import imagepath

#this is our main guy we love them, tiny little fella
#for now just a guy, maybe later moves. 

#reference from HY sokoban reference game https://github.com/ohjelmistotekniikka-hy/pygame-sokoban/tree/main

class Child(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        super().__init__()
        self.image = imagepath("child.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

# later method for updating the image when in different areas of map and or moving
        





