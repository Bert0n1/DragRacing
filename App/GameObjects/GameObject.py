from typing import Callable
import pygame as pg

from App.Sevices.event_service import Event, EventService


class GameObject():
    count = 0
    def __init__(self, parent: 'GameObject' = None,
                           id: str = None,
                          pos: pg.Vector2 = pg.Vector2(0,0),
                         size:pg.Vector2 = pg.Vector2(100,100)):
        
        self._rect = pg.Rect(pos.x, pos.y, size.x, size.y)
        self.id = id if id else f"GameObject{GameObject.count}"
        GameObject.count += 1
        self._events: list[Event] = list()
        self.__is_active = True
        self._parent: GameObject = parent
        self._children: dict[str, GameObject] = dict()
        if parent:
            self._parent.add_child(self)
    
    def add_child(self, other: "GameObject"):
        self._children[other.id] = other

    def create_event(self, id: str):
        e = Event(id)
        self._events.append(e)

    def get_child(self, id: str):
        if id in self._children:
            return self._children[id]
        
    @staticmethod
    def direct_tree_traversal(func: Callable) -> Callable:
        def wrapper(*args):
            value = func(*args)
            if value:
                return value
            for child in args[0]._children.values():
                value = child.direct_tree_traversal(func)(child, *args[1:])
                if value:
                    return value
        return wrapper

    @staticmethod
    def reverse_tree_traversal(func: Callable)-> Callable:
        def wrapper(*args):
            for child in args[0]._children.values():
                child.reverse_tree_traversal(func)(child)
            return func(*args)
        return wrapper

    @direct_tree_traversal
    def update(self):
        ...

    @direct_tree_traversal
    def hide(self):
        ...
        
    @direct_tree_traversal
    def draw(self, screen: pg.Surface):
        ...
    
    @property
    def is_active(self):
        return self.__is_active
    
    @is_active.setter
    @direct_tree_traversal
    def is_active(self, value: bool):
        self.__is_active = value
    


    @direct_tree_traversal
    def move(self, shift: pg.Vector2):
        self._rect.x += shift.x
        self._rect.y += shift.y

    def clear(self):
        self._children.clear()

    @direct_tree_traversal
    def search(self, id: str):
        if self.id == id:
            return self
    
    @direct_tree_traversal
    def event_handlle(self, service: EventService):
        for e in self._events:
            service.register_event(e.uid, e)


