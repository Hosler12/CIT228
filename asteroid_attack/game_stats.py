class gameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.game_victory = False
        self.tutorialized = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.total = 0
        self.current_points = 1
        self.score = 0

    def purchase_ships(self):
        self.ships_left += 1
        self.settings.ship_lives_cost = int(self.settings.ship_lives_cost * self.settings.cost_scale)

    def win_game(self):
        self.game_victory = True