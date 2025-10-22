import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class my_sprite(pygame.sprite.Sprite):
    def __init__(self, image_fname: str, loc: tuple[int, int] = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.rendering = pygame.image.load(image_fname)
        self.image = self.rendering
        self.image_fname = image_fname
        self.width = self.rendering.get_width()
        self.height = self.rendering.get_height()
        self.loc = loc

    def get_image(self) -> pygame.Surface:
        return self.rendering

    def get_width(self) -> int:
        return self.rendering.get_width()

    def get_height(self) -> int:
        return self.rendering.get_height()

    def __eq__(self, other):
        if not isinstance(other, my_sprite):
            return False
        return (
            self.get_width() == other.get_width()
            and self.get_height() == other.get_height()
            and self.loc == other.loc
        )

    def __repr__(self):
        return f"my_sprite(loc={self.loc}, size=({self.width}x{self.height}))"

    def __str__(self):
        return f"Sprite at {self.loc} ({self.width}x{self.height})"
