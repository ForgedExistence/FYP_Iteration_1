# all info is on README
# lets start by making a class system so the data
# can be used easily

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation




# What I want to do is change the coords using the angular velocity
# I will make a def and for each time t change the angle of the
# orbit
AU = 149.6e9
time = 24*60**2
#
theta_mercury = 0.07073160621761658
theta_venus = 0.027948243992606283
theta_earth = 0.016748663101604278
theta_mars = 0.009136638876700307

# radii in Astronomical units
radius_sun = 0
radius_mercury = 0.387

radius_venus = 0.723
radius_earth = 1
radius_mars = 1.523
#
fig = plt.figure()
ax = plt.axes(xlim=(-3, 3), ylim=(-3, 3))
patch_sun = plt.Circle((.1, -.1), 0.075, fc='y')
patch_mercury = plt.Circle((.1, -.1), 0.075, fc='k')
patch_venus = plt.Circle((.1, -.1), 0.075, fc='c')
patch_earth = plt.Circle((.1, -.1), 0.075, fc='g')
patch_mars = plt.Circle((.1, -.1), 0.075, fc='r')
line_mer, = ax.plot([], [], lw=1, color='k')
line_v, = ax.plot([], [], lw=1, color='c')
line_e, = ax.plot([], [], lw=1, color='g')
line_mar, = ax.plot([], [], lw=1, color='r')

def init():
    patch_sun.center = (0, 0)
    ax.add_patch(patch_sun)

    patch_mercury.center = (0, 0)
    ax.add_patch(patch_mercury)
    line_mer.set_data([], [])
    line_v.set_data([], [])
    line_e.set_data([], [])
    line_mar.set_data([], [])

    patch_venus.center = (0, 0)
    ax.add_patch(patch_venus)

    patch_earth.center = (0, 0)
    ax.add_patch(patch_earth)

    patch_mars.center = (0, 0)
    ax.add_patch(patch_mars)

    return patch_sun, patch_mercury, patch_venus, patch_earth, patch_mars, line_mer, line_v, line_e, line_mar,
xdata_mer, ydata_mer = [], []
xdata_v, ydata_v = [], []
xdata_e, ydata_e = [], []
xdata_mar, ydata_mar = [], []

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


    posx_venus = -radius_venus * np.cos(-theta_venus * i)
    posy_venus = -radius_venus * np.sin(-theta_venus * i)

    posx_earth = radius_earth * np.cos(theta_earth * i)
    posy_earth = radius_earth * np.sin(theta_earth * i)

    posx_mars = -radius_mars * np.cos(-theta_mars * i)
    posy_mars = -radius_mars * np.sin(-theta_mars * i)

    xdata_mer.append(posx_mercury)
    ydata_mer.append(posy_mercury)

    xdata_v.append(posx_venus)
    ydata_v.append(posy_venus)

    xdata_e.append(posx_earth)
    ydata_e.append(posy_earth)

    xdata_mar.append(posx_mars)
    ydata_mar.append(posy_mars)


    patch_sun.center = (posx_sun, posy_sun)
    patch_mercury.center = (posx_mercury, posy_mercury)
    patch_venus.center = (posx_venus, posy_venus)
    patch_earth.center = (posx_earth, posy_earth)
    patch_mars.center = (posx_mars, posy_mars)
    line_mer.set_data(xdata_mer, ydata_mer)
    line_v.set_data(xdata_v, ydata_v)
    line_e.set_data(xdata_e, ydata_e)
    line_mar.set_data(xdata_mar, ydata_mar)


    return patch_sun, patch_mercury, patch_venus, patch_earth, patch_mars,  line_mer, line_v, line_e, line_mar,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100000, interval=30, blit=True)
ax.set_xlabel("Distance (AU)")
ax.set_ylabel("Distance (AU)")
plt.show()

score_mars = 0
score_venus = 0
score_mercury = 0
i = 0
while i <= 20000:

    posx_mercury = radius_mercury * np.cos(theta_mercury * i)
    posy_mercury = radius_mercury * np.sin(theta_mercury * i)

    posx_venus = radius_venus * np.cos(-theta_venus * i)
    posy_venus = radius_venus * np.sin(-theta_venus * i)

    posx_earth = radius_earth * np.cos(theta_earth * i)
    posy_earth = radius_earth * np.sin(theta_earth * i)

    posx_mars = radius_mars * np.cos(-theta_mars * i)
    posy_mars = radius_mars * np.sin(-theta_mars * i)

    diff_pos1x = posx_mars - posx_earth
    diff_pos1y = posy_mars - posy_earth
    diff_pos2x = posx_venus - posx_earth
    diff_pos2y = posy_venus - posy_earth
    diff_pos3x = posx_mercury - posx_earth
    diff_pos3y = posy_mercury - posy_earth

    d1 = np.sqrt(diff_pos1x**2 + diff_pos1y**2)
    d2 = np.sqrt(diff_pos2x**2 + diff_pos2y**2)
    d3 = np.sqrt(diff_pos3x**2 + diff_pos3y**2)
    i += 1

    if d1 < d2 < d3:
        score_mars += 1
    elif d2 < d3:
        score_venus += 1
    else:
        score_mercury += 1
print("Number of days each planet is closest to Earth")
print("Mars    |    Venus     |  Mercury")
print(score_mars, "    |   ", score_venus, "     |   ", score_mercury)
