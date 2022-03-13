class Settings:
    def __init__(self):
        self.screen_width = 1500
        self.screen_height = 900
        self.bg_color = (255,255,255)

        self.ship_limit = 2

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        self.scale = 1.1
        self.cost_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.0
        self.bullets_allowed = 3

        self.bullet_speed = 1.0

        self.asteroid_speed = 0.15
        self.asteroid_points = 1
        self.asteroid_max = 2

        self.ship_speed_cost = 2
        self.bullet_speed_cost = 2
        self.bullet_max_cost = 10
        self.ship_lives_cost = 50
        self.victory_cost = 100

    def increase_speed(self):
        self.asteroid_speed *= self.scale
        self.asteroid_max += 1
        self.asteroid_points = int(self.asteroid_points * self.scale + 1)

    def increase_ship_speed(self):
        self.ship_speed *= self.scale
        self.ship_speed_cost = int(self.ship_speed_cost * self.cost_scale)

    def increase_bullet_speed(self):
        self.bullet_speed *= self.scale
        self.bullet_speed_cost = int(self.bullet_speed_cost * self.cost_scale)

    def increase_bullet_allowed(self):
        self.bullets_allowed += 1
        self.bullet_max_cost = int(self.bullet_max_cost * self.cost_scale)