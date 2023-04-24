class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, settings):
        """Инициализирует статистику."""
        self.settings = settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
        # Рекорд не должен сбрасываться.
        self.high_score = self.open_high_score()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def open_high_score(self):
        """Возвращает значение рекорда из файла 'high_score.txt', если такой существует, иначе возвращает 0."""
        try:
            with open('high_score.txt') as f:
                record = int(f.read())
                return record
        except FileNotFoundError:
            return 0
