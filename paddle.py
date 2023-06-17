import pygame

class Paddle:
    def __init__(self, screen_width, screen_height,key_moves):
        self.key_moves = key_moves
        self.width = 100
        self.height = 20
        self.color = (255, 255, 255)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = (screen_width // 2, screen_height - 20)

    def move(self):
        if self.key_moves["left"]:
            self.rect.x -= 2
            if self.rect.left < 0:
                self.rect.left = 0
        if self.key_moves["right"]:
            self.rect.x += 2
            if self.rect.right > self.screen_width:
                self.rect.right = self.screen_width



    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)