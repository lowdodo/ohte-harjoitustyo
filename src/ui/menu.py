"""
Module for the ui side of menu.
"""

import pygame
from imagepath import imagepath
from button import Button


class MenuView:
    """Class that creates the menu

    Attributes:
        _screen: The surface of the game.
        _handle_play: The function to handle the click of Play-button.
        _handle_quit: The function to handle the click of Quit-button.
        _event_queue: Gueue to handle events.
        _show_level_view: The function to switch to the level view.
        _play_button: The button for starting the game.
        _quit_button: The button for quitting the game.
        """

    def __init__(self, screen, handle_play, handle_quit, event_queue, show_level_view) -> None:
        """Constructor for menu

        Args:
            screen: The surface of the game
            handle_play: The function to handle the click of Play-button.
            handle_quit: The function to handle the click of Quit-button.
            event_queue: Gueue to handle events
            show_level_view: The function to switch to the level view.
        """
        self._screen = screen
        self._handle_play = handle_play
        self._handle_quit = handle_quit
        self._event_queue = event_queue
        self._show_level_view = show_level_view

        self._play_button = Button(image=imagepath("button.png"), pos=(500, 250),
                                   text="PLAY", font=pygame.font.SysFont(None, 75))
        self._quit_button = Button(image=imagepath("button.png"), pos=(500, 400),
                                   text="QUIT", font=pygame.font.SysFont(None, 75))

    def render(self):
        """Renders the buttons to the surface

        """
        self._screen.fill((0, 0, 0))

        menu_text = pygame.font.SysFont(None, 100).render(
            "MAIN MENU", True, (255, 255, 255))
        menu_rect = menu_text.get_rect(center=(500, 100))

        self._screen.blit(menu_text, menu_rect)

        for button in [self._play_button, self._quit_button]:
            button.update(self._screen)

        pygame.display.flip()
        self.handle_event()

    def handle_event(self):
        """Handles events like mouseinteraction

        Either quits the game or takes to new level.
        """
        running = True
        while running:
            for event in self._event_queue.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self._play_button.check_for_input(mouse_pos):
                        self._handle_play()
                        print("nyt menu handle playssa")

                    elif self._quit_button.check_for_input(mouse_pos):
                        self._handle_quit()
                        running = False
