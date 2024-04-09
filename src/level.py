#isnt used or working, but will be later,,,? stuff to be moved here so index and game_loop looks clear



# #own place for levels: 
# import pygame
# from sprites.child import Child
# from sprites.petal import Petal
# from game_loop import GameLoop 

# class Level:
#     def __init__(self, screen, event_queue, clock) -> None:
#         self.current_level = 1
#         self.screen = screen
#         self.event_queue = event_queue
#         self.clock = clock
#         self.all_sprites = pygame.sprite.Group()


#     def load_level(self, level_number):
#         if level_number == 1:
#             pass
#         elif level_number == 2:
#             pass
#         #.... more to come

#     def run_current_level(self, screen):
#         if self.current_level == 1:
#             self.load_level(1)
#             child_sprite = Child((50, 350))  
#             game_loop = GameLoop(self.screen, self.event_queue, self.clock, child_sprite, petal_sprite=None)
#             game_loop.start()

#         elif self.current_level == 2:
#             self.load_level(2)
#             child_sprite = Child((50, 350))  
#             petal_sprite = Petal((100, 450))
#             game_loop = GameLoop(self.renderer, self.event_queue, self.clock, child_sprite, petal_sprite)
#             game_loop.start()


#     def next_level(self):
#         self.current_level += 1

#     def update(self):
#         pass

