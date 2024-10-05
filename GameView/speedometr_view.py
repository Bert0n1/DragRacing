
import pygame as pg
from UI.area import Area
from UI.frame import UI_Frame
from UI.image import Image
from UI.textLabel import TextLabel
from sprite import Sprite


class Speedometr_view(UI_Frame):
    def __init__(self,
                image: Image,
                text_label: TextLabel,
                pos: tuple[int | float, int | float],
                size: tuple[int | float, int | float], 
                color: pg.Color = None,
                border_color: pg.Color = None,
                border_width: float = None):
        super().__init__(pos,size,color,border_color,border_width)
        self["speed_icon"] = image
        self["speed_value"] = text_label
    
    def update(self):
        super().update()

    def set_text(self, text: str):
        self["speed_value"].set_text(text)
    
