import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

fig = plt.figure()
ax = plt.axes(xlim=(-300e9, 300e9), ylim=(-300e9, 300e9))


class Body:
    solar_sys = []
    s_day = 24*60**2
    i = 0

    def __init__(self, mass, name, velocity, radius):
        self.mass = mass
        self.name = name
        self.velocity = velocity
        self.radius = radius
        self.id = len(Body.solar_sys)
        self.angular_v = self.velocity/self.radius
        Body.solar_sys.append(self)
        self.theta = self.get_theta()

    def __repr__(self):
        my_rep = f"""
        Body name: {self.name}
        Body ID: {self.id}
        Body mass: {self.mass}
        Body velocity: {self.velocity}
        Body radius: {self.radius}
        Body angular_v: {self.angular_v}
        Body theta: {self.theta}
        --------------
        """
        return my_rep

    def get_theta(self):
        theta = (self.velocity*Body.s_day)/self.radius
        return theta



Body(0.33e+24, "Mercury", 47.4e+3, 57.9e9)
Body(4.87e+24, "Venus", 35e+3, 108.2e9)
Body(5.97e+24, "Earth", 29e+3, 149.6e9)
Body(0.642e+24, "Mars", 24.1e+3, 227.9e9)
Body(1896e+24, "Jupitier", 13.1e+3, 778.6e9)
Body(568e+24, "Saturn", 9.7e+3, 1433.5e9)
Body(86.8e+24, "Uranus", 6.8e+3, 2872.5e9)
Body(102e+24, "Neptune", 5.4e+3, 4495.1e9)
Body(0.0146e+24, "Pluto", 4.7e+3, 5906.4e9)

for i in Body.solar_sys:
    print(i)
