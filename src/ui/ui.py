"""
Module for the main ui side.
"""
from ui.level_view import LevelView
from ui.menu import MenuView


class UI:
    """
    Class for main part of UI, relates to specific ui views.

    Attributes:
        _screen = view.
        _current_view = what is displayed at the moment.
        _current_level = keeps track of current level.
        _handle_play = function for changing the level.
        _handle_quit = function for quiting the game.
        _event_queue = keeps list of events after call.

    """

    def __init__(self, screen, handle_play, handle_quit, event_queue, current_level) -> None:
        self._screen = screen
        self._current_view = None
        self._current_level = current_level
        self._handle_play = handle_play
        self._handle_quit = handle_quit
        self._event_queue = event_queue

    def start(self):
        if not self._current_level:
            self._show_menu_view()
        else:
            self._show_level_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

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
