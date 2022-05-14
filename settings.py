
class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""

        self.screen_width = 1200  # Параметры экрана
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Цвет фона

        self.ship_speed = 1.5  # Настройки корабля
        self.ship_limit = 3 

        self.bullet_speed = 1.5  # Параметры снаряда
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        self.alien_speed = 1.0  # Настройки пришельцев
        self.fleet_drop_speed = 10
        self.fleet_direction = 1   # 1 обозначает движение вправо; а -1 - влево.