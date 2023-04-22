import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    """Класс, представляющий одну мишень ."""

    def __init__(self, screen, settings):
        """Инициализирует мишень и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Загрузка изображения мишени и назначение атрибута rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждая новая мишень в правом верхнем углу экрана.
        self.rect.right = self.screen.get_rect().right
        self.rect.y = self.rect.height

        # Сохранение точной вертикальной позиции мишени.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает мишень вверх или вниз."""
        self.y += (self.settings.target_speed * self.settings.target_direction)
        self.rect.y = self.y

    def check_edges(self):
        """Возвращает True, если мишень находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True