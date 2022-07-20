import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
import time
from game_stats import GameStats
from button import Button


def run_game(flag, start_time):
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
    play_button = Button(ai_settings, screen, 'Play')

    # 主循环
    while True:
        # 监视窗口
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)  # 响应
        # 创建外星人
        if flag:
            gf.create_fleet(ai_settings, screen, ship, aliens)
            start_time = time.time()
            flag = False
        else:
            end_time = time.time()
            if end_time - start_time >= 5:
                flag = True
        # 更新
        if stats.game_active:
            ship.update()  # 更新飞船
            gf.update_bullet(ai_settings, screen, ship, aliens, bullets)  # 更新子弹
            gf.update_alien(ai_settings, stats, screen, ship, aliens, bullets)  # 更新外星人
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)  # 更新屏幕


run_game(True, time.time())

