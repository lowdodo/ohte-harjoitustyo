class Button():
    def __init__(self, image, pos, text, font):
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.text = text
        self.font = font

    def render_text(self):
        if self.text:
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            
            return text_surface, text_rect

    def update(self, screen):
        screen.blit(self.image, self.rect)
        if self.text:
            text_surface, text_rect = self.render_text()
            screen.blit(text_surface, text_rect)

    def check_for_input(self, position):
        return self.rect.collidepoint(position)
