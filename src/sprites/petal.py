"""
Module for petal-sprite.
"""

import pygame
from pygame.sprite import AbstractGroup
from imagepath import imagepath

# reference from sokoban


class Petal(pygame.sprite.Sprite):
    """
    Class to initialise the petals for the game

    Attributes:
        image = image of the petal
        rect = movement for the petal.
        clicked = keeps track of if petal is moving or not.
    """

    def __init__(self, pos=(0, 0)):
        super().__init__()
        self.image = imagepath("petal.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.clicked = False

    def click(self):
        self.clicked = True

    def release(self):
        self.clicked = False

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        # code from chatgbt to help move the acative rect area of rotated image:
        self.rect = self.image.get_rect(center=self.rect.center)
        # chatbgt ends
