class Settings():
    """Класс для хранения всех настроек игры Aim to target."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.attempts_limit = 3

        # Параметры снаряда
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.target_speed = 1.0

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.target_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale

