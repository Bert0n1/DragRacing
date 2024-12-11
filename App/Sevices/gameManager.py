from UI.button import  TextButton
import logging
from App.GameObjects.gameObject import GameObject
from App.Sevices.event_service import EventService
from App.Sevices.scene_service import SceneService
from App.Sevices.window import Window
import pygame as pg

class GameManager():
    def __init__(self):
        self.scene_service = SceneService()
        self.main_window = Window()
        self.event_service = EventService()

    def start(self):
        logging.basicConfig(filename='game_manager.log', level=logging.INFO)
        self.scene_service.create_scene("start_menu")
        self.scene_service.set_active_scene("start_menu")
        
        btn = TextButton(pg.Vector2(400,20), 
                                   pg.Vector2(400,200),
                                   (0,0,0),
                                   1,(255,255,255),
                                   "Save")
        btn.text_color((255,255,255))
        btn.text_size(35)
        btn.padding = 10
        btn.callback = lambda **kwargs: print("Click")
        self.scene_service.current_scene.add_object(btn)

        self.event_handlle()    


    def set_window_size(self, size: pg.Vector2):
        self.main_window.size = size

    def add_object(self, obj: GameObject, scene_id: str):
        scene = self.scene_service[scene_id]
        if scene:
            scene.add_object(obj)
    
    def add_scene(self, id: str):
        self.scene_service.create_scene(id)

    def event_handlle(self):
        self.scene_service.current_scene.event_handlle(self.event_service)
        

    def update(self):
        self.scene_service.current_scene.update()
        self.scene_service.current_scene.draw(self.main_window.screen)
        self.main_window.update()
        self.event_service.proccess_system_events()