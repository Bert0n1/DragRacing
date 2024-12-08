
from App.GameObjects.gameObject import GameObject

import pygame as pg

from App.Sevices.event_service import EventService

class Scene():
    count = 0
    def __init__(self, id):
        self.id = id if id else f"Scene{Scene.count}"
        Scene.count += 1
        self.objects: dict[str, GameObject] = dict()
    

    def add_object(self, obj: GameObject):
        i = 0
        tmp_id = obj.id
        while obj.id in self.objects:
            obj.id = f"{tmp_id}{i}"
            i +=1
        self.objects[obj.id] = obj

    def delete_object(self, id: str):
        for obj in self.objects.values():
            finded_obj: GameObject = obj.search(id)
            if finded_obj:
                finded_obj.clear()
                return
            
    def search_object(self, id:str):
         for obj in self.objects.values():
            finded_obj: GameObject = obj.search(id)
            if finded_obj:
                return finded_obj
            
    def update(self):
        for obj in self.objects.values():
            obj.update()
    
    def draw(self,  screen: pg.Surface):
        for obj in self.objects.values():
            obj.draw(screen)
    
    def clear(self):
        for obj in self.objects.values():
            obj.clear()

    def event_handlle(self, service: EventService):
        for obj in self.objects.values():
            obj.event_handlle(service)


