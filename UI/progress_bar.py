import pygame as pg
from UI.area import Area

class Progress_bar():
    def __init__(self, pos: tuple[int | float, int | float],
                       size: tuple[int | float, int | float],
                       main_color: pg.Color,
                       max_value: int | float = 100,
                       fill_color: pg.Color = None,
                       border_color: pg.Color = None,
                       border_width: float = None ):
        self.main_area = Area(pos, size, main_color, border_color, border_width)
        fill_color = fill_color if fill_color else pg.Color(255,0,0)
        self.fill_area = Area(pos, size, fill_color, border_color, border_width)
        self.value = 0
        self.fill_area.background(True)
        self.main_area.background(True)
        self.max_value = max_value
        self.is_complete = False
    def draw(self, surface : pg.Surface):
        self.main_area.draw(surface)
        self.fill_area.draw(surface)
    
    def set_value(self, new_value: float):
        self.value = new_value

    def add_value(self, amount: float):
        self.value += amount

    def set_max_value(self, new_value: float):
        self.max_value = new_value

    def set_fill_color(self, color: pg.Color):
        self.fill_area.color = color

    def set_background_color(self, color: pg.Color):
        self.main_area.color = color

    def update(self):
        if self.is_complete and self.value < self.max_value:
            fill_width = (self.value / self.max_value) * self.main_area.rect.width
            self.fill_area.rect.width = fill_width
        else:
            self.fill_area.rect.width = self.main_area.rect.width
            self.is_complete = True