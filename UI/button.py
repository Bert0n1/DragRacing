
from typing import Callable
import pygame as pg
from App.GameObjects.gameObject import GameObject
from App.Sevices.event_service import Event
from UI.area import Area
from UI.textLabel import TextLabel


class TextButton(TextLabel):
    def __init__(self, text: str = None,
                parent: 'GameObject' = None,
                id: str = None,
                pos: pg.Vector2 = pg.Vector2(0,0),
                size:pg.Vector2 = pg.Vector2(100,100), 
                color: pg.Color = None,
                border_color: pg.Color = None,
                border_width: float = None):
        super().__init__(text, pos,size,color,
                         border_color,border_width,parent, id)
        e = Event(pg.MOUSEBUTTONDOWN)
        
        self._events.append(e)
        self._clicked = Event(f"Clicked{self.id}")
        e.subscribe(lambda **kwargs: self.on_collide(**kwargs))
        self._callback: Callable = lambda **kwargs:  None
        self._clicked.subscribe(lambda **kwargs: self.on_click(**kwargs))
    
    def on_click(self, **kwargs):
        self._callback(**kwargs)

    def on_collide(self, **kwargs):
        if self.check_collide(kwargs['pos']):
            self._clicked.invoke(**kwargs)

    def check_collide(self, point : tuple) -> bool:
        if ((self._rect.x <= point[0] <= (self._rect.x + self._rect.width))
            and (self._rect.y <= point[1] <= (self._rect.y + self._rect.height))):
            return True
        return False

    def connect(self, func: Callable):
        self._callback = func


