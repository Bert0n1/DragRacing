
import pygame as pg

from GameObjects.car import Car
from GameView.speedometr_view import Speedometr_view
from UI.area import Area
from UI.image import Image
from UI.progress_bar import Progress_bar
from UI.textLabel import TextLabel
from background import BackgroundHandller
from car import Body, CarPhysics, Engine, Transmission, Wheels
from sprite import Sprite

list_bckgrounds = ["D:/Coding/Python/DragRacing/sprites/garage.jpg",
                   "D:/Coding/Python/DragRacing/sprites/race.png"]

class Application():
    def __init__(self, size: tuple[int | float, int | float], fps : int):
        pg.init()
        self.screen = pg.display.set_mode(size)
        self.screen.fill((255,255,0))
        self.fps = fps
        self.clock = pg.time.Clock()
        self.background = BackgroundHandller(size, list_bckgrounds)

    def start(self):
        engine = Engine(300 * 2.5, 6000, 150)
        body = Body(2.2, 0.3, 1000)
        transmission = Transmission([3.5, 2.5, 1.8, 1.4, 1.0], 70, 0.85)
        suspension = None
        wheels = Wheels(17, 0.8, 100)
        car = CarPhysics(engine, body, transmission, suspension, wheels)
        self.car = Car(50,100, 200,"D:\Coding\Python\DragRacing\sprites\car.png",car)

        engine = Engine(250 * 2.5, 6000, 150)
        body = Body(2.2, 0.3, 1100)
        transmission = Transmission([3.5, 2.5, 1.8, 1.4, 1.0], 70, 0.85)
        suspension = None
        wheels = Wheels(17, 0.8, 100)
        car = CarPhysics(engine, body, transmission, suspension, wheels)
        self.car2 = Car(50,200, 200,"D:\Coding\Python\DragRacing\sprites\car.png",car)

        self.background.switch_back(1)
        self.progress_bar = Progress_bar((50, 400), (400, 50), (255,255,255), 10000)

        text_label = TextLabel("привет", (120, 0), (200,200), (255,0,0))
        text_label.set_text_color((255,255,255))

        speed_image = Image(filename="D:\Coding\Python\DragRacing\sprites\speedometr.png",pos=(0,0),size=(100,100), color=(0,0,0))

        self.speed_view = Speedometr_view(speed_image,text_label, pos=(50, 0), size=(400, 300))
        self.speed_view.background(False)
        self.speed_view.border_width = 5
        self.speed_view.border_color = (0,0,255)
        self.progress_bar2 = Progress_bar((50, 500), (400, 50), (255,255,255), 10000, fill_color=(0,0,255))
    def main_loop(self):
        while True:
            for e in pg.event.get():
                match e.type:
                    case pg.QUIT:
                        pg.quit()
                        return
            speed = self.car.calc_move(self.fps)
            speed2 = self.car2.calc_move(self.fps)[0]
            rel_speed = speed2 - speed[0]
            self.progress_bar.add_value(speed[0])
            self.progress_bar2.add_value(speed2)
            self.progress_bar.update()
            self.progress_bar2.update()
            self.background.scroll(speed)
            self.screen.fill((0,0,0))
            self.background.fill(self.screen)
            self.car.draw(self.screen)
            self.car2.move(rel_speed, 0)
            self.car2.draw(self.screen)
            self.progress_bar.draw(self.screen)
            self.progress_bar2.draw(self.screen)
            self.speed_view.set_text(f"{str(int(speed[0]))} km/h")
            self.speed_view.update()
            self.speed_view.draw(self.screen)
            pg.display.update()
            self.clock.tick(self.fps)

