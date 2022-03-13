import sys, pygame, random
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from asteroid import Asteroid
from game_stats import gameStats
from button import Button
from score import Scoreboard

class asteroidAttack:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.stats = gameStats(self)
        self.sb = Scoreboard(self)

        pygame.display.set_caption('Asteroid Attack')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()

        self._create_asteroids()

        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active and self.stats.tutorialized:
                self.ship.update()
                self._update_bullets()
                self._update_asteroids()
            elif self.stats.game_active:
                self.display_tutorial()
            self._update_screen()
            if self.stats.game_victory:
                self.stats.game_active = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.asteroids.draw(self.screen)
        self.sb.show_score()

        if not self.stats.tutorialized:
            self.sb.show_tutorial()

        if not self.stats.game_active and not self.stats.game_victory:
            self.play_button.draw_button()

        if self.stats.game_victory:
            self.sb.show_victory()

        pygame.display.flip()

    def _update_asteroids(self):
        self.asteroids.update()

        if pygame.sprite.spritecollideany(self.ship, self.asteroids):
            self._ship_hit()
        self._check_asteroids_bottom()

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_collissions()

    def _create_asteroids(self):
        for asteroid_number in range(self.settings.asteroid_max):
            asteroid = Asteroid(self)
            asteroid_width, asteroid_height = asteroid.rect.size
            asteroid.x = random.randint(250,self.settings.screen_width - 100)
            asteroid.rect.y = 50
            asteroid.rect.x = asteroid.x
            self.asteroids.add(asteroid)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            pygame.mouse.set_visible(False)

            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            self.sb.prep_score()
            self.sb.prep_ships()

            self.asteroids.empty()
            self.bullets.empty()

            self._create_asteroids()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_x:
            running=False
            pygame.quit()
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_1:
            if self.stats.score >= self.settings.ship_speed_cost:
                self.stats.score -= self.settings.ship_speed_cost
                self.settings.increase_ship_speed()
        if event.key == pygame.K_2:
            if self.stats.score >= self.settings.bullet_speed_cost:
                self.stats.score -= self.settings.bullet_speed_cost
                self.settings.increase_bullet_speed()
        if event.key == pygame.K_3:
            if self.stats.score >= self.settings.bullet_max_cost:
                self.stats.score -= self.settings.bullet_max_cost
                self.settings.increase_bullet_allowed()
        if event.key == pygame.K_4:
            if self.stats.score >= self.settings.ship_lives_cost:
                self.stats.score -= self.settings.ship_lives_cost
                self.stats.purchase_ships()
                self.sb.prep_ships()
        if event.key == pygame.K_5:
            if self.stats.score >= self.settings.victory_cost:
                self.stats.score -= self.settings.victory_cost
                self.stats.win_game()
        self.sb.prep_score()
        self.sb.prep_costs()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_bullet_collissions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.asteroids, True, True)

        if collisions:
            for asteroids in collisions.values():
                self.stats.score += self.settings.asteroid_points * len(asteroids)
                self.stats.total += self.settings.asteroid_points * len(asteroids)
            self.sb.prep_score()
            self.sb.prep_total()

        if not self.asteroids:
            self.bullets.empty()
            self.settings.increase_speed()
            self._create_asteroids()
            sleep(.5)

    def _check_asteroids_bottom(self):
        screen_rect = self.screen.get_rect()
        for asteroid in self.asteroids.sprites():
            if asteroid.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.asteroids.empty()
            self.bullets.empty()

            self._create_asteroids()
            self.ship.center_ship()

            self.sb.prep_ships()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def display_tutorial(self):
        sleep(1)
        self.stats.tutorialized = True

if __name__ == '__main__':
    ai = asteroidAttack()
    ai.run_game()