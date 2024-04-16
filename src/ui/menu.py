import pygame
from imagepath import imagepath
from button import Button


class MenuView:
    def __init__(self, screen, handle_play, handle_quit) -> None:
        self._screen = screen
        self._handle_play = handle_play
        self._handle_quit = handle_quit

        self._PLAY_BUTTON = Button(image=imagepath("button.png"), pos=(500, 250),
                                   text="PLAY", font=pygame.font.SysFont(None, 75))
        self._QUIT_BUTTON = Button(image=imagepath("button.png"), pos=(500, 400),
                                   text="QUIT", font=pygame.font.SysFont(None, 75))

    def render(self):
        self._screen.fill((0, 0, 0))

        MENU_TEXT = pygame.font.SysFont(None, 100).render(
            "MAIN MENU", True, (255, 255, 255))
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        self._screen.blit(MENU_TEXT, MENU_RECT)

        for button in [self._PLAY_BUTTON, self._QUIT_BUTTON]:
            button.update(self._screen)

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            if self._PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                self.next_level()
            elif self._QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                self._handle_quit()

    def next_level(self):
        return True
