"""
Module for ui side of levels.
"""

import pygame
from button import Button
from imagepath import imagepath
from sprites.child import Child
from sprites.petal import Petal
from repositories.player_repository import PlayerRepository
from database_connection import get_database_connection
from initialize_database import initialize_database
from players.player import Player
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

        self._player_repository = PlayerRepository(get_database_connection())
        self._player = None

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
        pygame.draw.circle(self._screen, color=(255, 255, 255), center=(100, 80), radius=30)
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
                            pygame.draw.circle(self._screen, color=(255, 255, 255), center=(100, 80), radius=30)
                            self._screen.blit(
                                self.child_sprite.image, self.child_sprite.rect)
                            pygame.display.update()
                        self._handle_play()
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
                for event in self._event_queue.get():
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

                if self._left:
                    self.child_sprite.rect.x -= 6
                if self._right:
                    self.child_sprite.rect.x += 6

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

            last_clicked = None

            running = True
            while running:
                for event in self._event_queue.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if not petal_drag:
                            clicked_petal = None
                            for petal in petals:
                                if petal.rect.collidepoint(mouse_pos) and not petal.clicked:
                                    clicked_petal = petal
                                    break
                            if clicked_petal:
                                if not last_clicked or last_clicked == clicked_petal:
                                    print("saatiin klikki")
                                    clicked_petal.click()
                                    last_clicked = clicked_petal
                                    petal_drag = True

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if last_clicked:
                            last_clicked.release()
                            last_clicked = None
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

            play_next = Button(image=imagepath("nextbutton.png"),
                            pos=(900, 350), text=None, font=None)

            play_next.update(self._screen)
            pygame.display.flip()
            # name = pygame.font.SysFont(None, 30).render(
            #     self.player_name, True, (255, 255, 255))
            # name_rect = name.get_rect(center=(640, 320))
            # pygame.draw.rect(self._screen, (255, 255, 255), name_rect, 2)
            # self._screen.blit(name, name_rect)???

            running = True
            while running:
                for event in self._event_queue.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_next.check_for_input(mouse_pos):
                            while self.child_sprite.rect.x <= 1000:
                                self.child_sprite.rect.x += 1
                                self._screen.fill((0, 0, 0))
                                self._screen.blit(text, text_rect)
                                self._screen.blit(
                                    self.child_sprite.image, self.child_sprite.rect)
                                pygame.display.update()
                            print("päästiin lvl3 loopin loppuun")
                            self._handle_play()
                            running = False

            pygame.display.flip()
# name picking
        if self.current_level == 4:
            pygame.display.set_caption("level4")
            self._screen.fill((0, 0, 0))
            clock = pygame.time.Clock()

            confirm_button = Button(image=imagepath("nextbutton.png"),
                            pos=(900, 550), text=None, font=None)
            
            prev_button = Button(image=imagepath("previousbutton.png"),
                            pos = (840, 550), text= None, font=None)
            base_font = pygame.font.Font(None, 32)
            player_name = ""
            input_rect = pygame.Rect(200, 200, 140, 32)
            color_active = pygame.Color('lightskyblue3') 
            color_passive = pygame.Color((245, 245, 240)) 
            color = color_passive 

            active = False
            initialize_database()
            user_text = ""
            text = pygame.font.SysFont(None, 25).render(
                "Now then, what is your name dear?", True, (255, 255, 255))
            text_rect = text.get_rect(center=(500, 10))
            self._screen.blit(text, text_rect)
            confirm_button.update(self._screen)
            prev_button.update(self._screen)
            pygame.display.flip()
            # Confirming name
            confirmed = False
            confirmed_twice = False
            running = True
            while running:
                for event in self._event_queue.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if input_rect.collidepoint(mouse_pos):
                            active = True
                        else:
                            active = False

                        if confirm_button.rect.collidepoint(mouse_pos) and not confirmed:
                            confirmed = True
                            self._screen.fill((0,0,0))
                            text1 = pygame.font.SysFont(None, 25).render(f"{user_text}, really?", True, (255, 255, 255))
                            self._screen.blit(text1, (100, 50))
                            confirm_button.update(self._screen)
                            prev_button.update(self._screen)
                            pygame.display.flip()
                        
                        elif confirm_button.rect.collidepoint(mouse_pos) and confirmed:
                            self._screen.fill((0,0,0))
                            confirm_button.update(self._screen)
                            prev_button.update(self._screen)
                            if confirmed_twice:
                                player_name = user_text
                                player = self._player_repository.name_the_player(player_name)
                                self._handle_play()
                            else:
                                confirmed_twice = True
                                text2 = pygame.font.SysFont(None, 25).render(f"{user_text}, reeeeeeally? My dear, who named you!", True, (255, 255, 255))
                                self._screen.blit(text2, (120, 80))
                                confirm_button.update(self._screen)
                                prev_button.update(self._screen)
                                pygame.display.flip()

                        elif prev_button.rect.collidepoint(mouse_pos):
                            confirmed = False
                            confirmed_twice = False
                            self._screen.fill((0,0,0))                            
                            text2 = pygame.font.SysFont(None, 25).render("Well what then? Silly thing", True, (255, 255, 255))
                            self._screen.blit(text2, (100, 50))
                            confirm_button.update(self._screen)
                            prev_button.update(self._screen)
                


                    if event.type == pygame.KEYDOWN: #for typing, looked example from here: https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/?ref=next_article
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1] 
                        else:
                            user_text += event.unicode
                if active:
                    color = color_active
                else:
                    color = color_passive
                pygame.draw.rect(self._screen, color, input_rect)
                text_surface = base_font.render(user_text, True, (255, 255, 255))
                self._screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                input_rect.w = max(100, text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(60)      



        if self.current_level == 5:
            pygame.display.set_caption("level5")
            self._screen.fill((0, 0, 0))
            clock = pygame.time.Clock()

            self._screen.blit(self.child_sprite.image, self.child_sprite.rect)
            self._screen.blit(self.petal_sprite.image, self.petal_sprite.rect)

            petal_button = Button(image=imagepath("petal.png"),
                                  pos=((750, 510)), text=None, font=None
                                  )
            petal_button.update(self._screen)
            pygame.display.update()

            running = True
            while running:
                for event in self._event_queue.get():
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

            # todo interaction with name, transition to further away

# 1st riddle
        if self.current_level == 6:
            self._screen.fill((0,0,0))
            text = pygame.font.SysFont(None, 35).render(
                "Moon is just a mirror for Sun to admire herself", True, (255, 255, 255))
            text_rect = text.get_rect(center=(500, 80))
            self._screen.blit(text, text_rect)

            mirror_button = Button(image=imagepath("mirror.png"),
                                  pos=((750, 510)), text=None, font=None
                                  )
            mirror_button.update(self._screen)
            mirror_broken = imagepath("brokenmirror.png")
            pygame.display.update()

            running = True
            while running:
                for event in self._event_queue.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mirror_button.rect.collidepoint(mouse_pos):
                            self._screen.fill((0,0,0))
                            mirror_broken.get_rect(750, 510)
                            text1 = pygame.font.SysFont(None, 35).render(
                                "Oh. You broke it.", True, (255, 255, 255))
                            text1_rect = text.get_rect(center=(500, 80))
                            self._screen.blit(text1, text1_rect)
                            #todo: make delayed transition to next level
                            self._handle_play()


                            

        if self.current_level == 7:
            self._screen.fill((0,0,0))
            text = pygame.font.SysFont(None, 35).render(
                "You should run now, for she will be bitter and angry", True, (255, 255, 255))
            text_rect = text.get_rect(center=(500, 80))
            
            text1 = pygame.font.SysFont(None, 35).render(
                "Raindrops are her tears, falling all the way to our world ", True, (255, 255, 255))
            text1_rect = text1.get_rect(center=(500, 80))
            self._screen.blit(text, text_rect)
            self._screen.blit(text1, text1_rect)

            



    def render(self):
        if self.current_level == 0:
            self.draw_prescreen()
        else:
            self.draw_level()

