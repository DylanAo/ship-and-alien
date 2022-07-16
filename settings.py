class Settings:
    """全部设置"""
    def __init__(self):
        # 基础设置
        self.screen_width = 600  # 窗口宽
        self.screen_height = 700  # 窗口长
        self.bg_color = (230, 230, 230)  # 窗口颜色-白
        self.ship_speed_factor_lr = 0.5  # 飞船左右移动速度
        self.ship_speed_factor_ud = 0.5  # 飞船上下移动速度
        self.game_name = "Fire in space"  # 窗口名称
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
