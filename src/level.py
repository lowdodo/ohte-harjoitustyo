# isnt used or working, but will be later,,,? stuff to be moved here so index and game_loop looks clear

# #own place for levels, needs to be connected to ui:
import pygame
from sprites.child import Child
from sprites.petal import Petal
from ui.menu import MenuView


class Level:
    def __init__(self, screen, event_queue, level_number) -> None:
        self.current_level = level_number
        self.screen = screen
        self.event_queue = event_queue
        self.child_sprite = Child()
        self.petal_sprite = Petal()

    def start_level(self, level_view):
        if self.current_level == 0:
            menu_view = MenuView(
                self.screen, self.handle_play, self.handle_quit)
            self.run_menu(menu_view)
        elif self.current_level == 1:
            self.run_prescreen(level_view)
        else:
            self.run_level(level_view, self.current_level)

    def run_menu(self, menu_view):
        running = True
        while running:
            for event in self.event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                else:
                    # should move to next level
                    menu_view.handle_event(event)
                    if menu_view.next_level():
                        running = False

        self.run_prescreen()

    def run_prescreen(self, level_view):
        running = True
        while running:
            level_view.handle_events()
            level_view.draw_prescreen()
            pygame.display.flip()

            for event in self.event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if level_view.NEXTbutton_rect.collidepoint(event.pos):
                        self.next_level()

    def run_level(self, level_view, current_level):
        running = True
        while running:
            level_view.handle_events()
            level_view.draw_level(current_level)
            pygame.display.flip()

            for event in self.event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if level_view.NEXTbutton_rect.collidepoint(event.pos):
                        self.next_level()

    def next_level(self):
        self.current_level += 1

    def update(self):
        if self.child_sprite:
            self.child_sprite.update()

    def move_child(self, x, y):
        self.child_sprite.rect.move_ip(x, y)

    def handle_play(self):
        self.current_level += 1
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def handle_quit(self):
        pygame.quit()
        quit()
