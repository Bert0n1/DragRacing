import pygame as pg

from App.Sevices.gameManager import GameManager

class App():
    MAX_FPS = 240

    def __init__(self):
        self.__init()
        self.__fps: int
        self.__clock = pg.time.Clock()
        self.__is_running = True
        self.game_manager = GameManager()
        self.game_manager.event_service.system_subcribe(pg.QUIT, self.stop)
    
    def start(self):
        self.game_manager.start()
        while self.__is_running:
            self.game_manager.update()
            self.__clock.tick(self.__fps)
    
    def stop(self):
        self.__is_running = False
    

    def set_fps(self, fps: int):
        if fps >= App.MAX_FPS:
            raise Exception("Too much frames per seconds")
        self.__fps = fps
    
    def __init(self):
        pg.init()
