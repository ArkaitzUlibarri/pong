import pygame


class Pad(pygame.sprite.Sprite):
    color = (255, 255, 255)  # Blanco
    size = (15, 45)  # 15*45

    def __init__(self, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(self.size).convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=pos)
        self.max_speed = 5
        self.stop()

    def move_up(self):
        self.speed = self.max_speed * -1

    def move_down(self):
        self.speed = self.max_speed * 1

    def stop(self):
        self.speed = 0

    def update(self):
        self.rect.move_ip(0, self.speed)
