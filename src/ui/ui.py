import pygame
from ui.choose_player import LoginView
from ui.level_view import LevelView
from ui.menu import MenuView
from ui.new_player import NewPlayerView
from level import Level

class UI:
    def __init__(self, screen, current_level, handle_play, handle_quit) -> None:
        self._screen = screen
        self._current_view = None
        self._current_level = current_level
        self._handle_play = handle_play
        self._handle_quit = handle_quit


    def start(self):

        # these are for manual testing
        self._show_menu_view()
        # level_number = self._current_level
        # self._show_level_view(level_number)
        # self._show_choose_player()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
    
    def _show_choose_player(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._screen,
            self._show_new_player_view
        )

        self._current_view.render()

    def _show_new_player_view(self):
        self._hide_current_view()
        self._current_view = NewPlayerView(
            self._screen,
            self._show_menu_view
        )

        self._current_view.render()

    def _show_menu_view(self):
        self._hide_current_view()
        self._current_view = MenuView(
            self._screen,
            self._handle_play,
            self._handle_quit
        )

        self._current_view.render()

    def _show_level_view(self, level_number):
        self._hide_current_view()
        level_instance = Level(self._screen, pygame.event, level_number)
        self._current_view = LevelView(
            self._screen,
            self._current_level,
            level_instance
        )

        self._current_view.render()


