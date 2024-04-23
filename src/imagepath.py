import os
import pygame

dirname = os.path.dirname(__file__)


def imagepath(filename):
    """Brings png-file for other code to use.
    
    Args:
        filename: name of the file that is searched.
    """
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )
