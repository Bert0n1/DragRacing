import pygame as pg

from App.GameObjects.gameObject import GameObject

class Area(GameObject):
    def __init__(self,parent: 'GameObject' = None,
                      id: str = None, pos: pg.Vector2 = pg.Vector2(0,0),
                      size:pg.Vector2 = pg.Vector2(100,100),
                      color: pg.Color = None,
                      border_color: pg.Color = None,
                      border_width: float =  None):
        super().__init__(parent,id,pos,size)
        self.color = color if color else (0,0,0)
        self.border_color = border_color if border_color else (255,0,0)
        self.border_width = border_width if border_width else 3
        self.surface = pg.Surface(size)
        self.is_background = False
        self.is_active = True

    def background(self, value: bool):
        self.is_background = value

    def draw(self, surface: pg.Surface):
        if self.is_active:
            if self.is_background:
                pg.draw.rect(surface, self.color, self._rect)
            surface.blit(self.surface, self._rect)
            if self.border_width > 0:
                pg.draw.rect(surface, self.border_color, self._rect, width=self.border_width)
            super().draw(surface)
        
    def update(self):
        super().update()