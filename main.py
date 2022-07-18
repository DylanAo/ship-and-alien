import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    # 基础设置
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.game_name)
    ship = Ship(ai_settings, screen)  # 创建飞船
    bullets = Group()  # 创建子弹组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)

    # 主循环
    while True:
        # 监视窗口
        gf.check_events(ai_settings, screen, ship, bullets)  # 响应
        if stats.game_active:
            ship.update()  # 更新飞船
            gf.update_bullet(ai_settings, screen, ship, aliens, bullets)  # 更新子弹
            gf.update_alien(ai_settings, stats, screen, ship, aliens, bullets)  # 更新外星人
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # 更新屏幕


run_game()

