"""
The main module for game.
"""

import sys
import pygame
from ui.ui import UI
from level import Level
from game_loop import GameLoop
from clock import Clock
from event_queue import EventQueue


def main():
    """Entry point to the game.

    Initialazes Pygame, sets up screen for the game, game loop and gandles exiting

    Attributes: 
        Pygame engine: Handles game window creation and event handling.
        EventQueue: Queue for handling game events.
        Level: Represents the current level on the game.
        UI: The user interface and interaction with the game.
        GameLoop: Controls the main game loop and updates the game.

    """
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Main menus")
    event_queue = EventQueue()
    clock = Clock()
    level = Level(screen, event_queue, current_level=2)
    ui = UI(screen, level.handle_play, level.handle_quit,
            event_queue, level.current_level)
    ui.start()

    game_loop = GameLoop(event_queue, clock, level)
    game_loop.start()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
