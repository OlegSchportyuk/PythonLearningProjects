class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 650
        self.bg_color = (30, 130, 130)

        # Настройки ракеты
        self.rocket_speed = 1.5