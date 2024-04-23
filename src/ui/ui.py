import pygame
from ui.choose_player import LoginView
from ui.level_view import LevelView
from ui.menu import MenuView
from ui.new_player import NewPlayerView


class UI:
    def __init__(self, screen, handle_play, handle_quit, event_queue, current_level) -> None:
        self._screen = screen
        self._current_view = None
        self._current_level = current_level
        self._handle_play = handle_play
        self._handle_quit = handle_quit
        self._event_queue = event_queue

    def start(self):

        # these are for manual testing
        print("menossa menuview")
        if not self._current_level:
            self._show_menu_view()
        else:
            self._show_level_view()
        # self._show_choose_player()
        # self._show_new_player_view()

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
            self._handle_play,
            self._handle_quit
        )

        self._current_view.render()

    def _show_menu_view(self):
        self._hide_current_view()
        print("nyt showmenuview.ui")
        self._current_view = MenuView(
            self._screen,
            self._handle_play,
            self._handle_quit,
            self._event_queue,
            self._show_level_view
        )
        self._current_view.render()

    def _show_level_view(self):
        print("päästiin showlevel")
        self._hide_current_view()
        self._current_view = LevelView(
            self._screen,
            self._handle_play,
            self._handle_quit,
            self._event_queue,
            self._current_level
        )

        self._current_view.render()
