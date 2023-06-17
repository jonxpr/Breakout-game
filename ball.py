import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height,paddle,blocks):
        super().__init__()
        self.blocks = blocks
        self.paddle = paddle
        self.radius = 10
        self.color = (255, 255, 255)
        self.delta_x = 1
        self.delta_y = 1
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = (self.screen_width // 2, self.screen_height //2 + 30)

    def check_collision_paddle(self):
        if pygame.Rect.colliderect(self.paddle.rect,self.rect):
            self.delta_y = -1*self.delta_y


    def check_collision_sides(self):
        if self.rect.right >= self.screen_width or self.rect.left <= 0:
            self.delta_x = -1*self.delta_x

        if self.rect.top <= 0:
            self.delta_y = -1*self.delta_y
        if self.rect.bottom >= self.screen_height:
            self.reset()

    def check_collision_blocks(self):
        r = pygame.sprite.spritecollide(self, self.blocks, True)
        if r:
            self.delta_y = -1 * self.delta_y

    def move(self):
        self.check_collision_sides()
        self.check_collision_paddle()
        self.check_collision_blocks()
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y


    def reset(self):
        self.rect.center = (self.screen_width // 2 + 300, self.screen_height //2 + 50)
        self.delta_y = 1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.rect.center, self.radius)