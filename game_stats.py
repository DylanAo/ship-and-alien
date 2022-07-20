# 游戏信息
class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.rest_stats()
        self.game_active = False

    def rest_stats(self):
        self.ship_left = self.ai_settings.ship_limit