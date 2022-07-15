import pygame
from pygame.sprite import Sprite


class Bullet (Sprite):
    def __init__(self, ai_settings, screen, ship):
        # 飞船处创建子弹对象
        super().__init__()
        self.screen = screen
        self.color = ai_settings.bullet_color  # 子弹颜色
        self.speed_factor = ai_settings.bullet_speed_factor  # 子弹速度

        # 创建子弹
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)  # （0，0）c处创建子弹同时创建图像
        # 放到飞船所在地方
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)  # 小数储存子弹位置

    # 子弹向上
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    # 画子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Bullet_right(Bullet):
    def __init__(self, ai_settings, screen, ship):
        super().__init__(ai_settings, screen, ship)
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x
