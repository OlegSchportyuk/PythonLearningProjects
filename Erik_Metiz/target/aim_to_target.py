import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from target import Target
from game_stats import GameStats
from button import Button


class Game():
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Aim to the target")

        # Создание экземпляра для хранения игровой статистики.
        self.stats = GameStats(self.settings)

        # Назначение цвета фона.
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()
        self.target = pygame.sprite.Group()

        self._create_target()

        # Создание кнопки Play.
        self.play_button = Button(self.screen, "Play")

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()

            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Сброс игровых настроек.
            self.settings.initialize_dynamic_settings()

            # Сброс игровой статистики.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Очистка мишени и снарядов.
            self.target.empty()
            self.bullets.empty()

            # Создание новой мишени и размещение корабля в центре.
            self._create_target()
            self.ship.center_ship()
            # Указатель мыши скрывается.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self._miss()
                self.bullets.remove(bullet)

        self._check_bullet_target_collisions()


    def _check_bullet_target_collisions(self):
        """Обработка коллизий снарядов с пришельцами."""
        # Удаление снарядов и мишени, участвующих в коллизиях.
        collisions = pygame.sprite.groupcollide(self.bullets, self.target, True, True)

        if not self.target:
            # Уничтожение существующих снарядов, повышение скорости и создание новой мишени.
            self.bullets.empty()
            self._create_target()
            self.settings.increase_speed()
            # Обновление попыток
            self.stats.attempts_left = 3

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw(self.screen)

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

    def _create_target(self):
        """Создание  мишени."""
        target = Target(self.screen, self.settings)
        self.target.add(target)

    def _check_target_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for target in self.target.sprites():
            if target.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Меняет направление мишени."""
        self.settings.target_direction *= -1

    def _update_target(self):
        """Обновляет позиции цели."""
        self._check_target_edges()
        self.target.update()

    def _miss(self):
        """Обрабатывает промахи."""
        if self.stats.attempts_left > 0:
            # Уменьшение attempts_left.
            self.stats.attempts_left -= 1
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

            # Очистка мишени и снарядов.
            self.target.empty()
            self.bullets.empty()

            # Создание новой мишени и размещение корабля в центре.
            self._create_target()
            self.ship.center_ship()

            # Пауза.
            sleep(0.5)


if __name__ == '__main__':
    #Создание экземпляра и запуск игры.
    game = Game()
    game.run_game()
