class Settings:
    """全部设置"""
    def __init__(self):
        # 基础设置
        self.screen_width = 1200  # 窗口宽
        self.screen_height = 700  # 窗口长
        self.bg_color = (230, 230, 230)  # 窗口颜色-白
        self.ship_speed_factor_lr = 1  # 飞船左右移动速度
        self.ship_speed_factor_ud = 1  # 飞船上下移动速度
        self.game_name = "Fire in space"  # 窗口名称
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
