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

    # 检测边缘
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True

    # 更新
    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x