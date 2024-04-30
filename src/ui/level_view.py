"""
Module for ui side of levels.
"""

import pygame
from button import Button
from imagepath import imagepath
from sprites.child import Child
from sprites.petal import Petal
import math


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
        self.player_name = ""

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_BACKSPACE:
                    self.player_name = self.player_name
                elif event.key == pygame.K_RETURN:
                    self._handle_play

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
        print("tämä on drawlevelin alussa, current level", self.current_level)
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

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            self._left = False
                        elif event.key == pygame.K_RIGHT:
                            self._right = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if petal_button.check_for_input(mouse_pos):
                            print("klikattiin petalia")
                            self._handle_play()
                            running = False

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
            print("päästiin if current 2")
            pygame.display.set_caption("level2")
            self._screen.fill((0, 0, 0))
            clock = pygame.time.Clock()
            text = pygame.font.SysFont(None, 25).render(
                "Can't you find me? You're almost there... but before that, answer me this:", True, (255, 255, 255))
            text_rect = text.get_rect(center=(500, 10))
            self._screen.blit(text, text_rect)

            text1 = pygame.font.SysFont(None, 25).render(
                "where is the flower that to bloom, needs no water and sun but mice and space?", True, (255, 255, 255))
            text1_rect = text1.get_rect(center= (500, 30))
            self._screen.blit(text1, text1_rect)

            
            pygame.draw.circle(self._screen, (200, 200, 200), (500, 300), 70)

            # correct positions for petals:
            circle_center = (500, 300)
            circle_radius = 70
            num_petals = 8
            positions = 2*math.pi / num_petals

            # targets for petals, chatgbt used for math formula:
            target_positions = []
            for target in range(num_petals):
                position = target * positions
                position_x = circle_center[0] + \
                    int(circle_radius * math.cos(position))
                position_y = circle_center[1] + \
                    int(circle_radius * math.sin(position))
                target_positions.append((position_x, position_y))

            print(target_positions)

            # chatgbt ends
            petal_drag = False
            petal_positions = [
                (200, 200), (430, 200), (730, 220), (210,
                                                     530), (924, 300), (30, 50), (20, 555), (10, 300)
            ]

            petals = [Petal(pos) for pos in petal_positions]

            for petal in petals:
                self._screen.blit(petal.image, petal.rect)

            self._screen.blit(text, text_rect)
            self._screen.blit(text1, text1_rect)

            pygame.display.update()

            running = True
            while running:
                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for petal in petals:
                            if petal.rect.collidepoint(mouse_pos):
                                print("saatiin klikki")
                                petal.click()
                                petal_drag = True

                    elif event.type == pygame.MOUSEBUTTONUP:
                        for petal in petals:
                            petal.release()
                            petal_drag = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        for petal in petals:
                            if petal.clicked:
                                petal.rotate(45)
                                self._screen.fill((0, 0, 0))
                                pygame.draw.circle(
                                    self._screen, (200, 200, 200), (500, 300), 70)
                                for petal in petals:
                                    self._screen.blit(petal.image, petal.rect)
                                    self._screen.blit(text, text_rect)
                                    self._screen.blit(text1, text1_rect)
                                    pygame.display.update()

                if petal_drag:
                    for petal in petals:
                        if petal.clicked:
                            petal.rect.center = mouse_pos
                            for other_petal in petals:
                                if other_petal != petal and petal.rect.colliderect(other_petal.rect):
                                    petal.rect.center = petal.prev_pos

                            self._screen.fill((0, 0, 0))
                            pygame.draw.circle(
                                self._screen, (200, 200, 200), (500, 300), 70)
                            for petal in petals:
                                self._screen.blit(petal.image, petal.rect)
                                self._screen.blit(text, text_rect)
                                self._screen.blit(text1, text1_rect)

                            pygame.display.update()

                for petal in petals:
                    petal.prev_pos = petal.rect.center
            if all(petal.rect.collidepoint(target_pos) for petal, target_pos in zip(petals, target_positions)):
                self._handle_play()
                print("kukka onnistui")
                running = False
            self._screen.fill((0, 0, 0))
            for petal in petals:
                self._screen.blit(petal.image, petal.rect)
                self._screen.blit(text, text_rect)
                self._screen.blit(text1, text1_rect)    


            pygame.display.flip()
            clock.tick(60)
# cat introduction
        if self.current_level == 3:
            pygame.display.set_caption("level3")
            self._screen.fill((0, 0, 0))
            clock = pygame.time.Clock()
            self.child_sprite.update()
            self._screen.blit(self.child_sprite.image, self.child_sprite.rect)

            # todo: hi darling, transition to name picking
            text = pygame.font.SysFont(None, 25).render(
                "There you are, darling. Now, whats your name my child?", True, (255, 255, 255))
            text_rect = text.get_rect(center=(640, 260))
            self._screen.blit(text, text_rect)

            name = pygame.font.SysFont(None, 30).render(
                self.player_name, True, (255, 255, 255))
            name_rect = name.get_rect(center=(640, 320))
            pygame.draw.rect(self._screen, (255, 255, 255), name_rect, 2)
            self._screen.blit(name, name_rect)

            pygame.display.flip()
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
