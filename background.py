
from pygame import Surface
from sprite import Sprite


class BackgroundHandller():
    def __init__(self, size : tuple[int,int], backgrounds: list[str]):
        self.backgrounds = []
        for path in backgrounds:
            self.backgrounds.append(Sprite(0,0,size[0],path))
        self.pathes: list = backgrounds
        self.cur_index:int
        self.size = size
        self.cur_background : Sprite
        self.switch_back(0)
        
    def fill(self, screen: Surface):
        screen.blit(self.cur_background.image, (self.cur_background.rect.x,self.cur_background.rect.y))
        screen.blit(self.buffer.image, (self.buffer.rect.x,self.buffer.rect.y))

    def switch_back(self, index: int):
        self.cur_background = self.backgrounds[index]
        self.cur_index = index
        self.buffer = Sprite(self.size[0] + self.cur_background.rect.x, 0,
                             self.size[0], self.pathes[index])

    def scroll(self, vec2 : tuple[float, float]):
        self.cur_background.move(-vec2[0], -vec2[1])
        self.buffer.move(-vec2[0], -vec2[1])
        if self.buffer.rect.x + self.size[0] <= 0:
            self.buffer.rect.x = self.size[0] + self.cur_background.rect.x
        if self.cur_background.rect.x + self.size[0] <= 0:
            self.cur_background.rect.x = self.size[0] + self.buffer.rect.x



