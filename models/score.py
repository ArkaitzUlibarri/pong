import pygame


class Score(pygame.sprite.Sprite):
    color = (255, 255, 255)  # Blanco

    def __init__(self, font, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.font = font
        self.pos = pos
        self.score = 0
        self.update()

    def score_up(self):
        self.score += 1

    def update(self):
        self.image = self.font.render(str(self.score), 0, Score.color)
        self.rect = self.image.get_rect(center=self.pos)
