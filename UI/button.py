
from typing import Callable
import pygame as pg
from App.GameObjects.gameObject import GameObject
from App.Sevices.event_service import Event
from UI.area import Area
from UI.textLabel import TextLabel


class TextButton(TextLabel):
    def __init__(self, pos : pg.Vector2,
                   size: pg.Vector2,
                   color: pg.Color = None,
                   border_width: float = None,
                   border_color: pg.Color = None,
                   text : str = None,
                   id:str = None,
                   parent: GameObject = None):
        super().__init__(pos,size,color,border_width,
                         border_color,text,
                         id,parent)
        self._event = Event(pg.MOUSEBUTTONDOWN)
        self._clicked = Event(f"Clicked{hash(self.id)}")
        self._callback : Callable = lambda **kwargs: None
        self._event.subscribe(self.onCollide)
        self._clicked.subscribe(lambda **kwargs: self.on_click(**kwargs))
        
    def onCollide(self, pos:pg.Vector2, **kwargs):
        if self.checkCollide(pos):
            self._clicked.invoke(**kwargs)
    
    def on_click(self, **kwargs):
        self._callback(**kwargs)

    @property
    def clicked(self):
        return self._clicked
    
    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, func: Callable):
        self._callback = func
    
    def update(self):
        return super().update()
              

        
