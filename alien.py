import pygame
from pygame.sprite import Sprite


class Aline(Sprite):
    def __init__(self, ai_settings, screen):
        super(Aline, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载图像，设置rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # 起始位置右上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 准确位置
        self.x = float(self.rect.x)

    # 绘制图像
    def bltime(self):
        self.screen.blit(self.image, self.rect)