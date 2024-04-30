"""
Module for levels to function.
"""
import pygame
from sprites.child import Child
from sprites.petal import Petal
from ui.menu import MenuView
from ui.level_view import LevelView


class Level:
    def __init__(self, screen, event_queue, current_level) -> None:
        self.current_level = current_level
        self.screen = screen
        self.event_queue = event_queue
        self.child_sprite = Child()
        self.petal_sprite = Petal()

    def start_level(self, current_level):
        print("TÄmä on current level=", self.current_level)
        if self.current_level is None:
            menu_view = MenuView(
                self.screen, self.handle_play, self.handle_quit, self.event_queue)
            print("level.py event_queue", self.event_queue)
            self.run_menu(menu_view)
        elif self.current_level == 0:
            level_view = LevelView(self.screen, self.handle_play,
                                   self.handle_quit, self.event_queue, self.current_level
                                   )
            self.run_prescreen(level_view)
        else:
            level_view = LevelView(self.screen, self.handle_play,
                                   self.handle_quit, self.event_queue, self.current_level
                                   )
            self.run_level(level_view, current_level)

    def run_menu(self, menu_view):
        print("nyt run menussa")
        running = True
        while running:
            for event in self.event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # else:
                #     print("level run menu else")
                #     # should move to next level
                #     menu_view.handle_event()
                running = False

        self.start_level()

    def run_prescreen(self, level_view):
        print("nyt runprescreen level")
        level_view.draw_prescreen()
        running = True
        while running:
            for event in self.event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                else:
                    # should move to next level
                    print("ollaan level prescreen elsesä levelwie")
                    self.handle_play()
                    running = False

    def run_level(self, level_view, current_level):
        running = True

        while running:
            pygame.display.flip()
            level_view.handle_event()
            level_view.draw_level()

            for event in self.event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def update(self):
        if self.child_sprite:
            self.child_sprite.update()

    def move_child(self, x, y):
        self.child_sprite.rect.move_ip(x, y)

    def handle_play(self):
        print("olemme handle playssa levelis")
        if self.current_level is None:
            print("current levle oli none")
            self.current_level = 0
            print("onko yhä?", self.current_level)
        else:
            print("current level ei ollut none")
            self.current_level += 1
        self.start_level(self.current_level)

    def handle_quit(self):
        pygame.quit()
        quit()
