class Button():
    """Class representing buttons in the game.

    Attributes:
        image: Surface of the button.
        rect: Physical part of the button.
        text: Possible text on the button.
        font: The font of the possible text.
    """

    def __init__(self, image, pos, text, font):
        """Constructor to creata a new button.

        Attributes:
            image: Surface of the button.
            rect: Physical part of the button.
            text: Possible text on the button.
            font: The font of the possible text.
        """
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.text = text
        self.font = font

    def render_text(self):
        """Renders the text on top of the button's surface.

        Returns:
            Tupple of the text wanted on the screen and the rect for it.
        """
        if self.text:
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)

            return text_surface, text_rect

    def update(self, screen):
        """Updates the buttons image to the screen, and possible text

        Args:
            screen: Screen that shows to the player.
        """
        screen.blit(self.image, self.rect)
        if self.text:
            text_surface, text_rect = self.render_text()
            screen.blit(text_surface, text_rect)

    def check_for_input(self, pos):
        """Checks if the position given is within the rect of the button

        Args: 
            pos: position of the button pressed

        """
        return self.rect.collidepoint(pos)
