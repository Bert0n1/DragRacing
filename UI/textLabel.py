import pygame as pg
from App.GameObjects.gameObject import GameObject
from UI.area import Area


class TextLabel(Area):
    def __init__(self, text : str,
                      pos: tuple[int|float, int|float],
                      size:tuple[int|float, int|float],
                      color: pg.Color = None,
                      border_color:pg.Color = None,
                      border_width: float =  None,
                      parent: 'GameObject' = None,
                      id: str = None):
        super().__init__(parent, id,pos, size, color,border_color, border_width)
        self.font_style = None
        self.font_size: int = 25
        self.font_color = pg.Color(0,0,0)
        self.text:str = text
        self.font_render()
        self.text_render()

    def text_render(self):
        x,y = self._rect.x, self._rect.y
        self.surface = self.font.render(self.text, True, self.font_color)
        self._rect = self.surface.get_rect()
        self._rect.x, self._rect.y = x,y

    def font_render(self):
        self.font = pg.font.Font(self.font_style, self.font_size)   
        
    def set_text_color(self, color : pg.Color):
        self.font_color = color
        self.text_render()

    def set_text_size(self, size: int):
        self.font_size = size
        self.font_render()

    def set_text_font(self, font):
        self.font_style = font
        self.font_render()
        
    def set_text(self, text: str):
        self.text = text
        self.text_render()



