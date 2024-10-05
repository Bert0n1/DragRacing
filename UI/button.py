
import pygame as pg
from UI.area import Area


class Buton(Area):
    def __init__(self,
                pos: tuple[int | float, int | float],
                size: tuple[int | float, int | float], 
                color: pg.Color = None,
                border_color: pg.Color = None,
                border_width: float = None):
        super().__init__(pos,size,color,border_color,border_width)
        self.view: Area = Area(pos,size,color, border_color,border_color)
        self.__func :  callable
    def draw(self):
        ...
    
    def update(self):
        ...
    
    def click(self):
        ...
        
    def connect(self, func: callable):
        ...


