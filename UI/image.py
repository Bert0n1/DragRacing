import pygame as pg

from UI.area import Area

class Image(Area):
    def __init__(self,
                filename: str,
                pos: tuple[int | float, int | float],
                size: tuple[int | float, int | float], 
                color: pg.Color = None,
                border_color: pg.Color = None,
                border_width: float = None):
        super().__init__(pos,size,color,border_color,border_width)
        self.image = pg.image.load(filename).convert_alpha()
        self.__buffer_img = self.image.copy()
        coeff = size[0]/self.image.get_size()[0]
        self.image_render()
        self.scale(coeff)
    

    def image_render(self):
        x,y = self.rect.x, self.rect.y
        self.surface = self.image.convert_alpha()
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = x,y

    def set_size(self, size: pg.Vector2):
        self.image = pg.transform.scale(self.__buffer_img, size)
        self.image_render()
        
    def scale(self, coeff: float):
        new_size = pg.Vector2(self.rect.width * coeff, self.rect.height * coeff)
        self.set_size(new_size)

    def flip(self, flip_x : bool, flip_y: bool):
        self.image = pg.transform.flip(self.__buffer_img, flip_x, flip_y)
    
    def set_image(self, filename: str):
        self.image = pg.image.load(filename).convert_alpha()
        self.__buffer_img = self.image.copy()
        rect_x = self.rect.x
        rect_y = self.rect.y
        width = self.rect.width
        height = self.rect.height
        self.rect = self.image.get_rect()
        self.scale(width)
        self.rect.x = rect_x
        self.rect.y = rect_y 
