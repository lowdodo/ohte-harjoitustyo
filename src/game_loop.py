import pygame


class GameLoop:
    def __init__(self, event_queue, clock, level):
        self._event_queue = event_queue
        self._clock = clock
        self._level = level

    def start(self):
        running = True
        while True:
            if self._handle_events() == False:
                break

            running = self._handle_events()
            self._level.update()
            self._clock.tick(60)
            
    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_child(x = -6, y = 0)
                if event.key == pygame.K_RIGHT:
                    self._level.move_child(x = 6, y = 0)
                if event.key == pygame.K_UP:
                    self._level.move_child(x = 0, y = -6)
                if event.key == pygame.K_DOWN:
                    pass  # do we have to crouch?
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._level.move_petal(x = event.pos[0])
                    self._level.move_petal(y = event.pos[1])

        self._level.child_sprite.update()
        self._level.petal_sprite.update()
        return True
    
