import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载图像成为矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 设置位置为最下方中间
        self.center_x = float(self.screen_rect.centerx)  # 中心x
        self.bottom_y = float(self.screen_rect.bottom)  # 底部y
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # 飞船运动
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor_lr
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor_lr
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom_y += self.ai_settings.ship_speed_factor_ud
        if self.moving_up and self.rect.top > 0:
            self.bottom_y -= self.ai_settings.ship_speed_factor_ud
        # 更新对象
        self.rect.centerx = self.center_x
        self.rect.bottom = self.bottom_y

    # 绘制飞船
    def blitme(self):
        self.screen.blit(self.image, self.rect)
