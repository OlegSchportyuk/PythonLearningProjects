import pygame

class Rocket():
    """Класс для управления ракетой."""

    def __init__(self, screen, settings):
        """Инициализирует ракету и задает ее начальную позицию."""
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        # Загружает изображение ракеты и получает прямоугольник.
        self.image = pygame.image.load('images/rocket1.png')
        self.rect = self.image.get_rect()
        # Каждая новая ракета появляется у нижнего края экрана.
        self.rect.center = self.screen_rect.center

        # Сохранение вещественной координаты центра ракеты.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию ракеты с учетом флагов."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Обновление атрибута rect на основании self.x и self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Рисует ракету в текущей позиции."""
        self.screen.blit(self.image, self.rect)