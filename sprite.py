import pygame as pg

from pygame import Surface


class Sprite():
    def __init__(self, left: float,
                        top: float,
                        width: float,
                        filename: str):
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.scale(width)
        self.rect.x = left
        self.rect.y = top

    def scale(self, width: float):
        ratio = self.image.get_width() / self.image.get_height()
        self.image = pg.transform.scale(self.image, (width, width / ratio))

    def flip(self, flip_x : bool, flip_y: bool):
        self.image = pg.transform.flip(self.image, flip_x, flip_y)

    def move(self,x: float, y: float) -> None:
        """
        This method move sprite to point with coordinats x,y
        """
        self.rect.x += x
        self.rect.y += y

    def draw(self,surface : Surface) -> None:
        """
        """
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Car(Sprite):
    def __init__(self):
        ...

