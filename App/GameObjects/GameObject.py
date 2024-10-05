from typing import Callable
import pygame as pg


class GameObject():
    count = 0
    def __init__(self, parent: "GameObject" = None,
                           id: str = None,
                          pos: pg.Vector2 = pg.Vector2(0,0),
                         size:pg.Vector2 = pg.Vector2(100,100)):
        
        self._rect = pg.Rect(pos.x, pos.y, size.x, size.y)
        self.id = id if id else f"GameObject{GameObject.count}"
        GameObject.count += 1

        self._parent: GameObject = parent
        self._children: dict[str, GameObject]
    
    @staticmethod
    def direct_tree_traversal(func: Callable, *args) -> Callable:
        def wrapper(*args):
            func(*args)
            for child in args[0]._children.values():
                child.direct_tree_traversal(func)
        return wrapper

    def reverse_tree_traversal(self, func):
        for child in self._children.values():
            child.direct_tree_traversal(func)
        self.func()

    @direct_tree_traversal
    def update(self):
        ...

    @direct_tree_traversal
    def hide(self):
        ...
        
    @direct_tree_traversal
    def draw(self):
        ...
    
    def clear(self):
        ...
