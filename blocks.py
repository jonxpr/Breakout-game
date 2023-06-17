import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y,width,height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("blue")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass  # You can add any necessary update logic for the brick here

