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
Body(0.33e+24, "Mercury", 47.4e+3, 57.9e9)
Body(4.87e+24, "Venus", 35e+3, 108.2e9)
Body(5.97e+24, "Earth", 29e+3, 149.6e9)
Body(0.642e+24, "Mars", 24.1e+3, 227.9e9)

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
AU = 149.6e9
#Sun
time = 24*60**2

theta_mercury = 0.07073160621761658
theta_venus = 0.027948243992606283
theta_earth = 0.016748663101604278
theta_mars = 0.009136638876700307
#radii
radius_sun = 0
radius_mercury = 0.387
radius_venus = 0.723
radius_earth = 1
radius_mars = 1.523



fig = plt.figure()
ax = plt.axes(xlim = (-3, 3), ylim = (-3, 3))
patch_sun = plt.Circle((.1, -.1), 0.075, fc='y')
patch_mercury = plt.Circle((.1, -.1), 0.075, fc='k')
patch_venus = plt.Circle((.1, -.1), 0.075, fc='c')
patch_earth = plt.Circle((.1, -.1), 0.075, fc='g')
patch_mars = plt.Circle((.1, -.1), 0.075, fc='r')

def init():
    patch_sun.center = (0, 0)
    ax.add_patch(patch_sun)

    patch_mercury.center = (0, 0)
    ax.add_patch(patch_mercury)

    patch_venus.center = (0, 0)
    ax.add_patch(patch_venus)

    patch_earth.center = (0, 0)
    ax.add_patch(patch_earth)

    patch_mars.center = (0, 0)
    ax.add_patch(patch_mars)


    return patch_sun, patch_mercury,patch_venus, patch_earth, patch_mars,


score_mars = 0
score_venus = 0
score_mercury = 0
def animate(i):

    posx_sun, posy_sun = patch_sun.center
    posx_mercury, posy_mercury = patch_mercury.center
    posx_venus, posy_venus = patch_venus.center
    posx_earth, posy_earth = patch_earth.center
    posx_mars, posy_mars = patch_mars.center


    posx_sun = radius_sun
    posy_sun = radius_sun

    posx_mercury = radius_mercury * np.cos(theta_mercury * i)
    posy_mercury = radius_mercury * np.sin(theta_mercury * i)
    pos_mercury = np.sqrt(posx_mercury**2+posy_mercury**2)

    posx_venus = radius_venus * np.cos(theta_venus * i)
    posy_venus = radius_venus * np.sin(theta_venus * i)
    pos_venus = np.sqrt(posx_venus**2+posy_venus**2)

    posx_earth = radius_earth * np.cos(theta_earth * i)
    posy_earth = radius_earth * np.sin(theta_earth * i)
    pos_earth = np.sqrt(posx_earth**2+posy_earth**2)

    posx_mars = radius_mars * np.cos(theta_mars * i)
    posy_mars = radius_mars * np.sin(theta_mars * i)
    pos_mars = np.sqrt(posx_mars**2+posy_mars**2)

    diff_pos1x = posx_mars - posx_earth
    diff_pos1y = posy_mars - posy_earth
    diff_pos2x = posx_venus - posx_earth
    diff_pos2y = posy_venus - posy_earth
    diff_pos3x = posx_mercury - posx_earth
    diff_pos3y = posy_mercury - posy_earth

    d1 = np.sqrt(diff_pos1x**2 + diff_pos1y**2)
    d2 = np.sqrt(diff_pos2x**2 + diff_pos2y**2)
    d3 = np.sqrt(diff_pos3x**2 + diff_pos3y**2)



    if d1 < d2 < d3:
        score_mars += 1
    elif d2 < d3:
        score_venus += 1
    else:
        score_mercury += 1


    patch_sun.center = (posx_sun, posy_sun)
    patch_mercury.center = (posx_mercury, posy_mercury)
    patch_venus.center = (posx_venus, posy_venus)
    patch_earth.center = (posx_earth, posy_earth)
    patch_mars.center = (posx_mars, posy_mars)




    return patch_sun, patch_mercury,patch_venus, patch_earth, patch_mars, score_mars, score_venus, score_mercury,
print("Mercury is closest this number of days: ", score_mercury, )
print("Venus is closest this number of days: ", score_venus, )
print("Mars is closest this number of days: ", score_mars, )

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=1000,
                               interval=20,
                               blit=True)

plt.show()
