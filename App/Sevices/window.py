import logging
import pygame as pg

class Window():
    def __init__(self, size: pg.Vector2 = None):
        self.__size = size if size else pg.Vector2(500,500)
        self.__screen = pg.display.set_mode(self.__size)
        self.__init()

    @property
    def size(self, size: pg.Vector2):
        self.__size = size
        self.__screen = pg.display.set_mode(self.__size)
        logging.info(f"[Window]: size has been changed. New size ({size.x, size.y})")

    @property
    def screen(self):
        return self.__screen
    
    def __init(self):
        self.display = pg.display
        self.display.init()

    def update(self):
        self.display.update()




