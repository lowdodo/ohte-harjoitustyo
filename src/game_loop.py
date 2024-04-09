import pygame

class GameLoop:
    def __init__(self, renderer, event_queue, clock, child_sprite, petal_sprite):
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._child_sprite = child_sprite
        self._petal_sprite = petal_sprite

    def start(self):
        while True:
            if self._handle_events() == False:
                break
            self._update_sprites()
            if self._renderer:
                self._render()
            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._child_sprite.rect.x -= 6
                if event.key == pygame.K_RIGHT:
                    self._child_sprite.rect.x += 6
                if event.key == pygame.K_UP:
                     self._child_sprite.rect.y += 6
                if event.key == pygame.K_DOWN:
                    pass  # do we have to crouch?
            if self._petal_sprite:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._petal_sprite.rect.x = event.pos[0]
                    self._petal_sprite.rect.y = event.pos[1]
        return True
    
    def _update_sprites(self):
        self._child_sprite.update()
        if self._petal_sprite:
            self._petal_sprite.update()

    def _render(self):
        self._renderer.render()
