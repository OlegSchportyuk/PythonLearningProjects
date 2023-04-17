import sys
import pygame
from settings import Settings
from star import Star

class Stars():
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Stars")
        # Назначение цвета фона.
        self.bg_color = (230, 230, 230)

        self.stars = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            #self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

    def _create_fleet(self):
        """Создание звезд."""
        star = Star(self.screen, self.settings)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - star_width
        number_stars_x = available_space_x // (2 * star_width)

        """Определяет количество рядов, помещающихся на экране."""
        available_space_y = (self.settings.screen_height - (2 * star_height))
        number_rows = available_space_y // (2* star_height)

        # Создание первого ряда звезд.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Создание звезды и размещение ее в ряду."""
        star = Star(self.screen, self.settings)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    #def _check_fleet_edges(self):
    #    """Реагирует на достижение пришельцем края экрана."""
    #    for alien in self.aliens.sprites():
    #        if alien.check_edges():
    #            self._change_fleet_direction()
    #            break

    #def _change_fleet_direction(self):
    #    """Опускает весь флот и меняет направление флота."""
    #    for alien in self.aliens.sprites():
    #        alien.rect.y += self.settings.fleet_drop_speed
    #    self.settings.fleet_direction *= -1

    #def _update_aliens(self):
    #    """Обновляет позиции всех пришельцев во флоте."""
    #    self._check_fleet_edges()
    #    self.aliens.update()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    stars = Stars()
    stars.run_game()

