import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)

        self.prep_score()
        self.prep_total()
        self.prep_ships()
        self.prep_costs()
        self.prep_tutorial()
        self.prep_victory()

    def prep_tutorial(self):
        self.tutorial0_image = self.font.render('Instructions', True, self.text_color, self.settings.bg_color)

        self.tutorial0_rect = self.tutorial0_image.get_rect()
        self.tutorial0_rect.left = self.screen_rect.left + 670
        self.tutorial0_rect.top = 510

        self.tutorial1_image = self.font.render('Press arrow keys to move and space to shoot', True, self.text_color, self.settings.bg_color)

        self.tutorial1_rect = self.tutorial1_image.get_rect()
        self.tutorial1_rect.left = self.screen_rect.left + 470
        self.tutorial1_rect.top = 560

        self.tutorial2_image = self.font.render('Press x to quit any time, and number keys to purchase upgrades', True, self.text_color, self.settings.bg_color)

        self.tutorial2_rect = self.tutorial2_image.get_rect()
        self.tutorial2_rect.left = self.screen_rect.left + 350
        self.tutorial2_rect.top = 600

    def show_tutorial(self):
        self.screen.blit(self.tutorial0_image, self.tutorial0_rect)
        self.screen.blit(self.tutorial1_image, self.tutorial1_rect)
        self.screen.blit(self.tutorial2_image, self.tutorial2_rect)

    def prep_score(self):
        rounded_score = self.stats.score
        score_str = 'Points: ' + '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 800

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.total_image, self.total_rect)
        self.screen.blit(self.ship_speed_cost_image, self.ship_speed_cost_rect)
        self.screen.blit(self.bullet_speed_cost_image, self.bullet_speed_cost_rect)
        self.screen.blit(self.bullet_max_cost_image, self.bullet_max_cost_rect)
        self.screen.blit(self.ship_lives_cost_image, self.ship_lives_cost_rect)
        self.screen.blit(self.victory_cost_image, self.victory_cost_rect)
        self.ships.draw(self.screen)

    def prep_costs(self):
        self._prep_ship_speed_cost()
        self._prep_bullet_speed_cost()
        self._prep_bullet_max_cost()
        self._prep_ship_lives_cost()
        self._prep_victory_cost()

    def _prep_ship_speed_cost(self):
        rounded_ship_speed_cost = self.settings.ship_speed_cost
        ship_speed_cost_str = '1) Ship speed cost: ' + '{:,}'.format(rounded_ship_speed_cost)
        self.ship_speed_cost_image = self.font.render(ship_speed_cost_str, True, self.text_color, self.settings.bg_color)

        self.ship_speed_cost_rect = self.ship_speed_cost_image.get_rect()
        self.ship_speed_cost_rect.left = self.screen_rect.left + 20
        self.ship_speed_cost_rect.top = 20

    def _prep_bullet_speed_cost(self):
        rounded_bullet_speed_cost = self.settings.bullet_speed_cost
        bullet_speed_cost_str = '2) Bullet speed cost: ' + '{:,}'.format(rounded_bullet_speed_cost)
        self.bullet_speed_cost_image = self.font.render(bullet_speed_cost_str, True, self.text_color, self.settings.bg_color)

        self.bullet_speed_cost_rect = self.bullet_speed_cost_image.get_rect()
        self.bullet_speed_cost_rect.left = self.screen_rect.left + 20
        self.bullet_speed_cost_rect.top = 70

    def _prep_bullet_max_cost(self):
        rounded_bullet_max_cost= self.settings.bullet_max_cost
        bullet_max_cost_str = '3) Max bullets cost: ' + '{:,}'.format(rounded_bullet_max_cost)
        self.bullet_max_cost_image = self.font.render(bullet_max_cost_str, True, self.text_color, self.settings.bg_color)

        self.bullet_max_cost_rect = self.bullet_max_cost_image.get_rect()
        self.bullet_max_cost_rect.left = self.screen_rect.left + 20
        self.bullet_max_cost_rect.top = 120

    def _prep_ship_lives_cost(self):
        rounded_ship_lives_cost = self.settings.ship_lives_cost
        ship_lives_cost_str = '4) Ship lives cost: ' + '{:,}'.format(rounded_ship_lives_cost)
        self.ship_lives_cost_image = self.font.render(ship_lives_cost_str, True, self.text_color, self.settings.bg_color)

        self.ship_lives_cost_rect = self.ship_lives_cost_image.get_rect()
        self.ship_lives_cost_rect.left = self.screen_rect.left + 20
        self.ship_lives_cost_rect.top = 170

    def _prep_victory_cost(self):
        rounded_victory_cost = self.settings.victory_cost
        victory_cost_str = '5) Victory cost: ' + '{:,}'.format(rounded_victory_cost)
        self.victory_cost_image = self.font.render(victory_cost_str, True, self.text_color, self.settings.bg_color)

        self.victory_cost_rect = self.victory_cost_image.get_rect()
        self.victory_cost_rect.left = self.screen_rect.left + 20
        self.victory_cost_rect.top = 220

    def prep_total(self):
        total = self.stats.total
        total_str  = 'Total score: ' + '{:,}'.format(total)

        self.total_image = self.font.render(total_str, True, self.text_color, self.settings.bg_color)

        self.total_rect = self.total_image.get_rect()
        self.total_rect.left = 20
        self.total_rect.top = 850

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10
            ship.rect.y = 270 + ship_number * ( ship.rect.height + 10)
            self.ships.add(ship)

    def prep_victory(self):
        self.victory_image = self.font.render('You have managed to win the game by building the super duper laser that definitely exists', True, self.text_color, self.settings.bg_color)

        self.victory_rect = self.victory_image.get_rect()
        self.victory_rect.centerx = self.screen_rect.centerx
        self.victory_rect.top = 500

        self.victory1_image = self.font.render('Press x to take a victory lap.', True, self.text_color, self.settings.bg_color)

        self.victory1_rect = self.victory1_image.get_rect()
        self.victory1_rect.centerx = self.screen_rect.centerx
        self.victory1_rect.top = 550

    def show_victory(self):
        self.screen.blit(self.victory_image, self.victory_rect)
        self.screen.blit(self.victory1_image, self.victory1_rect)