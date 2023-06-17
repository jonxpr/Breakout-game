import pygame
from pygame.locals import *
from paddle import Paddle
from ball import Ball
from blocks import Block

class Game:
    def __init__(self):
        pygame.init()
        self.key_action = {
            "left": False,
            "right": False
        }
        self.screen_width = 1080
        self.screen_height = 720
        self.num_rows = 8
        self.num_columns = 5
        self.block_width = self.screen_width/self.num_columns
        self.block_height = (self.screen_height*0.4)/self.num_rows
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.paddle = Paddle(self.screen_width, self.screen_height,self.key_action)
        self.blocks = pygame.sprite.Group()
        self.create_bricks()
        self.ball = Ball(self.screen_width, self.screen_height,self.paddle,self.blocks)



    def create_bricks(self):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                block_x = column * (self.block_width + 3) + 2
                block_y = row * (self.block_height + 3) + 50
                block = Block(block_x, block_y,self.block_width,self.block_height)
                self.blocks.add(block)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.key_action["left"] = True
                elif event.key == K_RIGHT:
                    self.key_action["right"] = True
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    self.key_action["left"] = False
                elif event.key == K_RIGHT:
                    self.key_action["right"] = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle.draw(self.screen)
        self.blocks.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.paddle.move()
            self.ball.move()
            self.draw()
            self.clock.tick(240)

        pygame.quit()

# Entry point
if __name__ == "__main__":
    game = Game()
    game.run()