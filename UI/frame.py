
import pygame as pg
from UI.area import Area


class UI_Frame(Area):
    def __init__(self,
                pos: tuple[int | float, int | float],
                size: tuple[int | float, int | float], 
                color: pg.Color = None,
                border_color: pg.Color = None,
                border_width: float = None):
        super().__init__(pos,size,color,border_color,border_width)
        self.components : dict[str, Area] = dict()
    
    def add_component(self, component: Area, key: str):
        self.components[key] = component

    def remove_component(self, key: str):
        del self.components[key]

    def get_component(self, key: str) -> Area:
        if key in self.components:
            return self.components[key]
    
    def __getitem__(self, key) -> Area:
        return self.get_component(key)

    def __setitem__(self, key, component: Area):
        component.move(pg.Vector2(component.rect.x + self.rect.x, component.rect.y + self.rect.y))
        self.add_component(component, key)

    def draw(self, surface: pg.Surface):
        super().draw(surface)
        for c in self.components:
            self.components[c].draw(surface)
    
    def move(self, pos: pg.Vector2):
        super().move(pos)
        for c in self.components:
            self.components[c].move(pg.Vector2(self.components[c].rect.x + pos.x,self.components[c].rect.y + pos.y ))

    def update(self):
        super().update()
        for c in self.components:
            self.components[c].update()