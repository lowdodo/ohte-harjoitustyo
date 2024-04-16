import sys
import pygame
from ui.ui import UI
from level import Level
from game_loop import GameLoop
from clock import Clock
from event_queue import EventQueue


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Main menu")
    event_queue = EventQueue()
    clock = Clock()
    level = Level(screen, event_queue, level_number=0)
    ui = UI(screen, level.current_level, handle_play, handle_quit)
    ui.start()

    game_loop = GameLoop(event_queue, clock, level)
    game_loop.start()

    pygame.quit()
    sys.exit()


def handle_play(level):
    level.run_prescreen()


def handle_quit():
    sys.exit()


if __name__ == "__main__":
    main()
