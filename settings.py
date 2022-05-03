
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 1200 # Параметры экрана
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Цвет фона
        # Настройки корабля
        self.ship_speed = 1.5