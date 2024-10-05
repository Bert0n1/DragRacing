
import enum


class Drive(enum.Enum):
    fwd = 0
    rwd = 1
    awd = 2

class Wheels():
    def __init__(self, rims, tyres, m, friction_coefficient_static=0.8, friction_coefficient_kinetic=0.7):
        self.rims = rims
        self.tyres = tyres
        self.m = m
        self.friction_coefficient_static = friction_coefficient_static  # Коэффициент трения покоя
        self.friction_coefficient_kinetic = friction_coefficient_kinetic  # Коэффициент трения скольжения

    def get_clutch(self, force, is_moving=False):
        """
        Рассчитывает силу сцепления шин с дорогой, учитывая трение покоя или скольжения.
        """
        # В данном примере, force - это сила, приложенная к шинам.
        # μ - коэффициент сцепления шин с дорогой (вы должны задать его значение)
        # Сила трения = μ * сила нормальной реакции
        if is_moving:  # Если объект уже движется
            return self.friction_coefficient_kinetic * force  # Сила трения скольжения
        else:  # Если объект в покое
            return self.friction_coefficient_static * force  # Сила трения покоя

class Transmission():
    def __init__(self, gr, m, ef):
        self.gr = gr
        self.m = m
        self.ef = ef
        self.broadcast = 0

    def get_gr(self):
        return self.gr[self.broadcast]

    def shift_up(self):
        su = self.broadcast + 1
        if su < len(self.gr):
            self.broadcast = su

class Body():
    def __init__(self, farea, dragcoef, m):
        self.farea = farea
        self.dragcoef = dragcoef
        self.m = m
    def calc_resistance(self, speed, airdensity):
        return 0.5 * airdensity * speed ** 2 * self.farea * self.dragcoef 


class Engine():
    k = 9550
    def __init__(self, torque, rpm, m):
        self.torque = torque
        self.rpm = rpm
        self.m = m

    def hp(self):
        return self.torque * self.rpm / 5252
    def calc_power(self):
        return self.torque * self.rpm * 60 / Engine.k


class CarPhysics():
    def __init__(self, engine: Engine, body: Body, transmission: Transmission, suspension, wheels: Wheels):
        self.engine = engine
        self.body = body
        self.transmission = transmission
        self.suspension = suspension
        self.wheels = wheels
        self.speed: float = 0.01
    def m_car(self):
        return self.engine.m + self.body.m + self.transmission.m  + self.wheels.m
    def calc_speed(self, h, airdensity=1.225):
        k1 = self.calc_acceleration(self.speed, airdensity)
        k2 = self.calc_acceleration(self.speed + 0.5 * h * k1, airdensity)
        k3 = self.calc_acceleration(self.speed + 0.5 * h * k2, airdensity)
        k4 = self.calc_acceleration(self.speed + h * k3, airdensity)

        self.speed += h * (k1 + 2*k2 + 2*k3 + k4) / 6

    def calc_acceleration(self, speed, airdensity=1.225):
        if speed > 0:
            is_moving = True
        else:
            is_moving = False
        Fr = self.wheels.get_clutch(self.m_car() * 9.8, is_moving) + self.body.calc_resistance(speed, airdensity)

        N = self.engine.calc_power() * self.transmission.ef * self.transmission.get_gr()
        Ft =  N / speed
        F = Ft - Fr
        a = F / self.m_car()
        return a




if __name__ == "__main__":
    engine = Engine(300 * 2.5, 6000, 150)
    body = Body(2.2, 0.3, 1000)
    transmission = Transmission([3.5, 2.5, 1.8, 1.4, 1.0], 70, 0.85)
    suspension = None
    wheels = Wheels(17, 0.8, 100)
    

    car = CarPhysics(engine, body, transmission, suspension, wheels)


    t = 0
    h = 0.001
    distance = 0
    speed = 0.01
    time_sec = 0
    import time
    import os
    while True:
        
        car.calc_speed(t, h)
        t += h
        time_sec += h
        speed = car.speed * 3.6
        distance += speed * h
        print(f"time: {time_sec}")
        print(f"distance: {distance}")
        print(f"speed {speed}")
        time.sleep(1)
