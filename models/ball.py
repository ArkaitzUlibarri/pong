import pygame


class Ball(pygame.sprite.Sprite):
    color = (255, 0, 0)  # Rojo
    size = (10, 10)  # 10x10

    def __init__(self, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = pygame.Surface(Ball.size).convert()
        self.image.fill(Ball.color)
        self.reset()
        self.stop()

    def change_y(self):
        self.speed_y *= -1

    def change_x(self):
        self.speed_x *= -1

    def reset(self):
        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)

    def start(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    def isStopped(self):
        return (self.speed_x == 0 and self.speed_y == 0)
