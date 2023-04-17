import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Класс, представляющий одну звезду."""

    def __init__(self, screen, settings):
        """Инициализирует звезду и задает ее начальную позицию."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Загрузка изображения звезды и назначение атрибута rect.
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Каждая новая звезда появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции звезды.
        self.x = float(self.rect.x)