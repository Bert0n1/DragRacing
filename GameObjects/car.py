from car import CarPhysics
from sprite import Sprite


class Car(Sprite):
    h = 0.001
    px_m_ratio = 100
    def __init__(self, left: float,
                        top: float,
                        width: float,
                        filename: str,
                        physics: CarPhysics):
        super().__init__(left, top, width, filename)
        self.physics = physics
        self.timer = 0
    
    
    def calc_move(self, fps:int) -> tuple[float| int, float| int]:
        self.physics.calc_speed(Car.h)
        self.timer += Car.h
        return (self.physics.speed * Car.px_m_ratio/fps, 0)