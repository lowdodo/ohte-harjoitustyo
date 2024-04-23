import pygame
from imagepath import imagepath
from button import Button


class LoginView:
    def __init__(self, screen, handle_show_new_player_view) -> None:
        self._screen = screen
        self.handle_show_create_user_view = handle_show_new_player_view
        self.font = pygame.font.SysFont(None, 24)
        self.selected_player = None

        self._player1_button = Button(imagepath("button.png"), pos=(500, 200),
                                      text="PLAYER 1", font=pygame.font.SysFont(None, 75))

        self._new_player_button = Button(imagepath("button.png"), pos=(500, 300),
                                        text="NEW PLAYER", font=pygame.font.SysFont(None, 75))

        self._quit_button = Button(image=imagepath("button.png"), pos=(500, 400),
                                   text="QUIT", font=pygame.font.SysFont(None, 75))

    def render(self):
        self._screen.fill((0, 0, 0))
        # self.screen.blit(self.player_label, self.player_label_rect)

        for button in [self._player1_button, self._new_player_button, self._quit_button]:
            button.update(self._screen)

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.player_button1.rect.collidepoint(event.pos):
                self.handle_player("Player 1")
            elif self.new_player_button.rect.collidepoint(event.pos):
                self.handle_show_create_user_view()

    def handle_player(self, player_name):
        self.selected_player = player_name
