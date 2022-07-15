import sys
import pygame
from bullet import Bullet


# 响应键盘和鼠标
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        # 关闭窗口
        if event.type == pygame.QUIT:
            sys.exit()
        # 左右移动
        elif event.type == pygame.KEYDOWN:
           check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


# 键盘按下
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


# 键盘抬起
def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False


# 屏幕相关
def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # 绘制飞船
    pygame.display.flip()  # 绘制窗口


#  子弹相关
def update_bullet(bullets):
    bullets.update()  # 子弹向上移动
    # 删除消失子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


#  发射子弹
def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship)  # 创建子弹
    bullets.add(new_bullet)  # 加入编组
    new_bullet_right = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet_right)