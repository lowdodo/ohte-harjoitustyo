import pygame
from button import Button
from imagepath import imagepath

# later can be added new players, for now lets go with one

class NewPlayerView:
    def __init__(self, screen, handle_player_added) -> None:
        self._screen = screen 
        self._handle_player_added = handle_player_added

        self.add_button = Button(image=imagepath("button.png"), pos=(400, 320),
                                 text="Add Player", font=pygame.font.SysFont(None, 36))

    def render(self):
        """Renders the new player view on the screen."""
        self._screen.fill((0, 0, 0))

        self.add_button.update(self._screen)

        pygame.display.flip() 

    def handle_event(self, event):
        """Handles events for the new player view."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.add_button.check_for_input(mouse_pos):
                self._handle_player_added()
