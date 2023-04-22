class GameStats():
    """Отслеживание статистики для игры Aim to target."""

    def __init__(self, settings):
        """Инициализирует статистику."""
        self.settings = settings
        self.reset_stats()
        # Игра Aim to target запускается в неактивном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.attempts_left = self.settings.attempts_limit
