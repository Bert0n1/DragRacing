import pygame as pg
from App.GameObjects.gameObject import GameObject
from UI.area import Area


class TextLabel(Area):
    def __init__(self, pos : pg.Vector2,
                       size: pg.Vector2,
                       color: pg.Color = None,
                       border_width: float = None,
                       border_color: pg.Color = None,
                       text : str = None,
                       id:str = None,
                       parent: GameObject = None):
        
        super().__init__(pos, size, color, border_color, border_width,id, parent)
        self._font_size = 25
        self._padding = 0
        self._font_family = None
        self._text_color = pg.Color(0,0,0)
        self._text : str = text if text else ""
        self._font_render()
        self._text_render()

    def _font_render(self):
        self.font = pg.font.Font(self._font_family, self._font_size)
        self._text_render()

    def _text_render(self):
        x,y = self.rect.x, self.rect.y
        self.surface = self.font.render(self._text, True, self._text_color)
        self.rect = self.surface.get_rect()
        self.rect.w += 2 * self._padding
        self.rect.h += 2 * self._padding
        self.rect.x, self.rect.y = x,y

    def text_color(self, color : pg.Color):
        self._text_color = color
        self._text_render()

    def text_size(self, size: float):
        self._font_size = size
        self._font_render()

    def text_font(self, font_family):
        self._font_family = font_family
        self._font_render()

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text: str):
        self._text = text
        self._text_render()
    
    @property
    def padding(self):
        return self._padding
    
    @padding.setter
    def padding(self, value: float):
        self._padding = value
        self._text_render()



