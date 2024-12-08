
import logging
from App.GameObjects.scene import Scene
import pygame as pg

class SceneService():
    def __init__(self):
        self.scenes: dict[str, Scene] = dict()
        self.current_scene: Scene 

    def __getitem__(self, scene_id:str) -> Scene:
        if scene_id in self.scenes:
            return self.scenes[scene_id]
        logging.error(f"[SceneService]: scene with id {scene_id} does not exists")
    
    def create_scene(self, id:str):
        new_scene = Scene(id)
        self.scenes[id] = new_scene
        logging.info(f"[SceneService]: scene with id {id} has been created")

    def clear_scene(self, id: str):
        if id in self.scenes:
            self.scenes.clear()
            logging.info(f"[SceneService]: scene with id {id} has been cleared")
        else:
            logging.error(f"[SceneService]: scene with id {id} does not exists")

    def delete_scene(self, id: str):
        if id in self.scenes:
            self.scenes.clear()
            del self.scenes[id]
            logging.info(f"[SceneService]: scene with id {id} has been deleted")
        else:
            logging.error(f"[SceneService]: scene with id {id} does not exists")
    
    def set_active_scene(self, id: str):
        if id in self.scenes:
            self.current_scene = self.scenes[id]
            logging.info(f"[SceneService]: scene with id {id} is active")
        else:
            logging.error(f"[SceneService]: scene with id {id} does not exists")
    
    def update(self):
        if self.current_scene:
            self.current_scene.update()
    
    def draw(self, screen: pg.Surface):
        if self.current_scene:
            self.current_scene.draw(screen)