import pygame
from level import Level
from button import Button
from imagepath import imagepath
from sprites.child import Child
from sprites.petal import Petal
from game_loop import GameLoop


class LevelView:
    def __init__(self, screen, current_level, level_instance) -> None:
        self._screen = screen
        self.font = pygame.font.SysFont(None, 30)
        self.NEXTbutton = imagepath("nextbutton.png")
        self.NEXTbutton_rect = self.NEXTbutton.get_rect(center=(400, 300))
        self.BUTTON = imagepath("nextbutton.png")
        self.BUTTON_rect = self.BUTTON.get_rect(center=(400, 300))
        self.current_level = current_level
        self._level_instance = level_instance

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.NEXTbutton_rect.collidepoint(event.pos):
                    self.handle_next_level()

    def draw_prescreen(self):
        self._screen.fill((0, 0, 0))
        text = pygame.font.SysFont(None, 25).render(
            "What's that? Oh, a child.... come here", True, (255, 255, 255))
        text_rect = text.get_rect(center=(640, 260))
        self._screen.blit(text, text_rect)
        child_sprite = Child((50, 350))

        self._screen.blit(self.NEXTbutton, self.NEXTbutton_rect)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_NEXT = Button(image=imagepath("nextbutton.png"),
                           pos=(800, 500), text=None, font=None)
        PLAY_NEXT.update(self._screen)

        if self.NEXTbutton_rect.collidepoint(PLAY_MOUSE_POS):
            while child_sprite.rect.x <= 1000:
                child_sprite.rect.x += 1
                self._screen.fill((0, 0, 0))
                self._screen.blit(text, text_rect)
                self._screen.blit(child_sprite.image, child_sprite.rect)
                pygame.display.update()

            # Start level1
            self.draw_level()

    def draw_level(self):
        if self.current_level == 1:
            pygame.display.set_caption("level1")
            self._screen.fill((0, 0, 0))
            child_sprite = Child((50, 350))
            petal_sprite = Petal((800, 450))
            clock = pygame.time.Clock()
            self._screen.blit(child_sprite.image, child_sprite.rect)
            self._screen.blit(petal_sprite.image, petal_sprite.rect)
            game_loop = GameLoop(event_queue=pygame.event,
                                 clock=clock, level=self._level_instance)
            pygame.display.update()
            game_loop.start()
            pygame.draw.rect(self._screen)

    def render(self):
        if self.current_level == 0:
            self.draw_prescreen()
        elif self.current_level == 1:
            self.draw_level()

    def run(self):
        while True:
            self.handle_events()
            self.draw_prescreen()
            self.render()
            pygame.display.flip()
