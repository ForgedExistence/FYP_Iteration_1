# all info is on README
# lets start by making a class system so the data
# can be used easily

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation



class Body:
    solar_sys = []
    s_day = 24*60**2

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


# Sun = Body(1.99e+30, "Sun", 0, 0)
Body(0.33e+24, "Mercury", 47.4e+3, 0.387)
Body(4.87e+24, "Venus", 35e+3, 0.723)
Body(5.97e+24, "Earth", 29e+3, 1)
Body(0.642e+24, "Mars", 24.1e+3, 1.523)

input()

for i in Body.solar_sys:
    print(i)
# # Time for fun
# Use matplotlib
# Look up planetary motion online
#v=rw where v= velocity r= radius w= angular velocity

# What I want to do is change the coords using the angular velocity
# I will make a def and for each time t change the angle of the
# orbit

#Sun
# time = 24*60**2
# theta = 2
# radius = 0
# fig = plt.figure()
# ax = plt.axes(xlim = (-3, 3), ylim = (-3, 3))
# patch = plt.Circle((.1, -.1), 0.075, fc='y')
#
#
# def init():
#     patch.center = (0, 0)
#     ax.add_patch(patch)
#     return patch,
# def animate(i):
#     posx, posy = patch.center
#     posx = radius * np.cos(theta * time * i)
#     posy = radius * np.sin(theta * time * i)
#     patch.center = (posx, posy)
#
#     return patch,
# anim = animation.FuncAnimation(fig, animate,
#                                init_func=init,
#                                frames=360,
#                                interval=20,
#                                blit=True)
time = 24*60**2
theta = 2
radius = 0.387
fig = plt.figure()
ax = plt.axes(xlim = (-3, 3), ylim = (-3, 3))
patch = plt.Circle((.1, -.10), 0.075, fc='b')


def init():
    patch.center = (0, 0)
    ax.add_patch(patch)
    return patch,
def animate(i):
    posx, posy = patch.center
    posx = radius * np.cos(theta * time * i)
    posy = radius * np.sin(theta * time * i)
    patch.center = (posx, posy)

    return patch,
anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=20,
                               blit=True)
plt.show()
