import pygame as pg

class Area():
    def __init__(self, pos: tuple[int|float, int|float],
                      size:tuple[int|float, int|float],
                      color: pg.Color = None,
                      border_color:pg.Color = None,
                      border_width: float =  None):
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])
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
                pg.draw.rect(surface, self.color, self.rect)
            surface.blit(self.surface, self.rect)
            if self.border_width > 0:
                pg.draw.rect(surface, self.border_color, self.rect, width=self.border_width)

    def move(self, pos: pg.Vector2):
        self.rect.x = pos.x
        self.rect.y = pos.y
        
    def update(self):
        ...