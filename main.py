import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 基础设置
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.game_name)
    ship = Ship(ai_settings, screen)  # 创建飞船
    bullets = Group()
    bullets_right = Group()

    # 主循环
    while True:
        # 监视窗口
        gf.check_events(ai_settings, screen, ship, bullets, bullets_right)  # 响应
        # 更新
        ship.update()  # 更新飞船
        gf.update_bullet(bullets, bullets_right, ai_settings)  # 更新子弹
        gf.update_screen(ai_settings, screen, ship, bullets, bullets_right)  # 更新屏幕


run_game()

