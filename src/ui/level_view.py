import pygame
from button import Button
from imagepath import imagepath
from sprites.child import Child
from sprites.petal import Petal


class LevelView:
    def __init__(self, screen, handle_play, handle_quit, event_queue, current_level) -> None:
        self._screen = screen
        self._handle_play = handle_play
        self._handle_quit = handle_quit

        self.font = pygame.font.SysFont(None, 30)
        self.current_level = current_level

        self._event_queue = event_queue

        self.child_sprite = Child((50, 350))
        self.petal_sprite = Petal((750, 510))
        # all sprites chatcgbtltä:
        self.all_sprites = pygame.sprite.Group()
        # chatbgt loppuu
        self._left = False
        self._right = False
        self._petal_moves = False

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             if self.NEXTbutton_rect.collidepoint(event.pos):
    #                 self.handle_next_level()

    def draw_prescreen(self):
        print("päästiin drawpre uilevel")
        pygame.display.set_caption("prescreen")
        self._screen.fill((0, 0, 0))
        text = pygame.font.SysFont(None, 25).render(
            "What's that? Oh, a child.... come here", True, (255, 255, 255))
        text_rect = text.get_rect(center=(640, 260))
        self._screen.blit(text, text_rect)
        self.child_sprite.update()
        self._screen.blit(self.child_sprite.image, self.child_sprite.rect)

        pygame.display.flip()

        play_next = Button(image=imagepath("nextbutton.png"),
                           pos=(900, 350), text=None, font=None)

        play_next.update(self._screen)
        pygame.display.flip()
        running = True
        while running:
            for event in self._event_queue.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_next.check_for_input(mouse_pos):
                        while self.child_sprite.rect.x <= 1000:
                            self.child_sprite.rect.x += 1
                            self._screen.fill((0, 0, 0))
                            self._screen.blit(text, text_rect)
                            self._screen.blit(
                                self.child_sprite.image, self.child_sprite.rect)
                            pygame.display.update()
                        print("päästiin drawpre loopin loppuun")
                        # Start level1
                        self._handle_play()
                        print("nyt olemme prescreen whilen lopsssa")
                        running = False

    def draw_level(self):
        print("ui levelview draw levle alussa")
        print("tämä on drawlevelin current level", self.current_level)
        if self.current_level == 1:
            pygame.display.set_caption("level1")
            self._screen.fill((0, 0, 0))
            clock = pygame.time.Clock()

            self._screen.blit(self.child_sprite.image, self.child_sprite.rect)
            self._screen.blit(self.petal_sprite.image, self.petal_sprite.rect)

            petal_button = Button(image=imagepath("petal.png"),
                                  pos=((750, 510)), text=None, font=None
                                  )
            petal_button.update(self._screen)
            pygame.display.update()

            # todo: when petal is clicked, it takes you to new level
            running = True
            while running:
                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self._left = True
                        elif event.key == pygame.K_RIGHT:
                            self._right = True
                        elif petal_button.check_for_input(mouse_pos):
                            self._handle_play()

                        # elif event.key == pygame.K_UP:
                        #     up = True
                        # # elif event.key == pygame.K_DOWN:
                        # #     self.child_sprite.rect.y += 6
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            self._left = False
                        elif event.key == pygame.K_RIGHT:
                            self._right = False

                # moving smoothly
                if self._left:
                    self.child_sprite.rect.x -= 6
                if self._right:
                    self.child_sprite.rect.x += 6
                # if up:
                #     self.child_sprite.rect.y -= 2

                # not going past the screen:
                if self.child_sprite.rect.left < 0:
                    self.child_sprite.rect.left = 0
                elif self.child_sprite.rect.right > 1000:
                    self.child_sprite.rect.right = 1000

                self._screen.fill((0, 0, 0))
                self._screen.blit(self.child_sprite.image,
                                  self.child_sprite.rect)
                self._screen.blit(self.petal_sprite.image,
                                  self.petal_sprite.rect)
                pygame.display.update()
                clock.tick(60)

            if self.current_level == 2:
                pygame.display.set_caption("level2")
                self._screen.fill((0, 0, 0))
                clock = pygame.time.Clock()
                running = True
                while running:
                    for event in pygame.event.get():
                        mouse_pos = pygame.mouse.get_pos()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self._petal_moves = True

                        if event.type == pygame.MOUSEBUTTONUP:
                            self._petal_moves = False

                if self._petal_moves:
                    self.petal_sprite.rect = mouse_pos

                    # todo: flower puzzle, transition to eyes, then to lvl 3

# cat introduction
            if self.current_level == 3:
                pygame.display.set_caption("level3")
                self._screen.fill((0, 0, 0))
                clock = pygame.time.Clock()
                # todo: hi darling, transition to name picking
                text = pygame.font.SysFont(None, 25).render(
                    "There you are, darling. Now, whats your name my child?", True, (255, 255, 255))
                text_rect = text.get_rect(center=(640, 260))
                self._screen.blit(text, text_rect)

# name picking
            if self.current_level == 4:
                pass
                # todo name picking

            if self.current_level == 5:
                pass
                # todo interaction with name, transition to further away

# 1st riddle
            if self.current_level == 6:
                # todo first riddle
                pass

    def render(self):
        if self.current_level == 0:
            self.draw_prescreen()
        else:
            self.draw_level()

    # def run(self):
    #     while True:
    #         self.handle_events()
    #         self.draw_prescreen()
    #         self.render()
    #         pygame.display.flip()
