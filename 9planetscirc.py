import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# testing my knowledge of python decided to use this to compute the
# angular velocity

# What I want to do is change the coords using the angular velocity
# I will make a def and for each time t change the angle of the
# orbit
AU = 149.6
# time = 24*60**2
#
theta_mercury = 0.07073160621761658
theta_venus = 0.027948243992606283
theta_earth = 0.016748663101604278
theta_mars = 0.009136638876700307
theta_j = 0.0014536861032622655
theta_s = 0.0005846389954656436
theta_u = 0.00020453263707571803
theta_n = 0.00010379301906520433
theta_p = 6.875253961804145e-05


# radii in Astronomical units
radius_sun = 0
radius_mercury = 0.387
radius_venus = 0.723
radius_earth = 1
radius_mars = 1.523
r_j = 778.6 / AU
r_s = 1433.5 / AU
r_u = 2872.5 / AU
r_n = 4495.1 / AU
r_p = 5906.4 / AU
#
fig = plt.figure()
ax = plt.axes(xlim=(-40, 40), ylim=(-40, 40))
patch_sun = plt.Circle((.1, -.1), 1, fc='y')
patch_mercury = plt.Circle((.1, -.1), 1, fc='k')
patch_venus = plt.Circle((.1, -.1), 1, fc='c')
patch_earth = plt.Circle((.1, -.1), 1, fc='g')
patch_mars = plt.Circle((.1, -.1), 1, fc='r')
patch_j = plt.Circle((.1, -.1), 1, fc='orange')
patch_s = plt.Circle((.1, -.1), 1, fc='gold')
patch_u = plt.Circle((.1, -.1), 1, fc='blue')
patch_n = plt.Circle((.1, -.1), 1, fc='navy')
patch_p = plt.Circle((.1, -.1), 1, fc='black')


line_mer, = ax.plot([], [], lw=1, color='k')
line_v, = ax.plot([], [], lw=1, color='c')
line_e, = ax.plot([], [], lw=1, color='g')
line_mar, = ax.plot([], [], lw=1, color='r')
line_j, = ax.plot([], [], lw=1, color='orange')
line_s, = ax.plot([], [], lw=1, color='gold')
line_u, = ax.plot([], [], lw=1, color='blue')
line_n, = ax.plot([], [], lw=1, color='navy')
line_p, = ax.plot([], [], lw=1, color='black')


def init():
    line_mer.set_data([], [])
    line_v.set_data([], [])
    line_e.set_data([], [])
    line_mar.set_data([], [])
    line_j.set_data([], [])
    line_s.set_data([], [])
    line_u.set_data([], [])
    line_n.set_data([], [])
    line_p.set_data([], [])

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

    patch_j.center = (0, 0)
    ax.add_patch(patch_j)

    patch_s.center = (0, 0)
    ax.add_patch(patch_s)

    patch_u.center = (0, 0)
    ax.add_patch(patch_u)

    patch_n.center = (0, 0)
    ax.add_patch(patch_n)

    patch_p.center = (0, 0)
    ax.add_patch(patch_p)

    return (patch_sun, patch_mercury, patch_venus, patch_earth, patch_mars,
            patch_j, patch_s, patch_u, patch_n, patch_p, line_mer, line_v,
            line_e, line_mar, line_j, line_s, line_u, line_n, line_p)


xdata_mer, ydata_mer = [], []
xdata_v, ydata_v = [], []
xdata_e, ydata_e = [], []
xdata_mar, ydata_mar = [], []
xdata_j, ydata_j = [], []
xdata_s, ydata_s = [], []
xdata_u, ydata_u = [], []
xdata_n, ydata_n = [], []
xdata_p, ydata_p = [], []


def animate(i):

    posx_sun, posy_sun = patch_sun.center
    posx_mercury, posy_mercury = patch_mercury.center
    posx_venus, posy_venus = patch_venus.center
    posx_earth, posy_earth = patch_earth.center
    posx_mars, posy_mars = patch_mars.center
    posx_j, posy_j = patch_j.center
    posx_s, posy_s = patch_s.center
    posx_u, posy_u = patch_u.center
    posx_n, posy_n = patch_n.center
    posx_p, posy_p = patch_p.center

    posx_sun = radius_sun
    posy_sun = radius_sun

    posx_mercury = radius_mercury * np.cos(theta_mercury * i)
    posy_mercury = radius_mercury * np.sin(theta_mercury * i)

    posx_venus = radius_venus * np.cos(theta_venus * i)
    posy_venus = radius_venus * np.sin(theta_venus * i)

    posx_earth = radius_earth * np.cos(theta_earth * i)
    posy_earth = radius_earth * np.sin(theta_earth * i)

    posx_mars = radius_mars * np.cos(theta_mars * i)
    posy_mars = radius_mars * np.sin(theta_mars * i)

    posx_j = r_j * np.cos(theta_j * i)
    posy_j = r_j * np.sin(theta_j * i)

    posx_s = r_s * np.cos(theta_s * i)
    posy_s = r_s * np.sin(theta_s * i)

    posx_u = r_u * np.cos(theta_u * i)
    posy_u = r_u * np.sin(theta_u * i)

    posx_n = r_n * np.cos(theta_n * i)
    posy_n = r_n * np.sin(theta_n * i)

    posx_p = r_p * np.cos(theta_p * i)
    posy_p = r_p * np.sin(theta_p * i)


    xdata_mer.append(posx_mercury)
    ydata_mer.append(posy_mercury)

    xdata_v.append(posx_venus)
    ydata_v.append(posy_venus)

    xdata_e.append(posx_earth)
    ydata_e.append(posy_earth)

    xdata_mar.append(posx_mars)
    ydata_mar.append(posy_mars)

    xdata_j.append(posx_j)
    ydata_j.append(posy_j)

    xdata_s.append(posx_s)
    ydata_s.append(posy_s)

    xdata_u.append(posx_u)
    ydata_u.append(posy_u)

    xdata_n.append(posx_n)
    ydata_n.append(posy_n)

    xdata_p.append(posx_p)
    ydata_p.append(posy_p)

    patch_sun.center = (posx_sun, posy_sun)
    patch_mercury.center = (posx_mercury, posy_mercury)
    patch_venus.center = (posx_venus, posy_venus)
    patch_earth.center = (posx_earth, posy_earth)
    patch_mars.center = (posx_mars, posy_mars)
    patch_j.center = (posx_j, posy_j)
    patch_s.center = (posx_s, posy_s)
    patch_u.center = (posx_u, posy_u)
    patch_n.center = (posx_n, posy_n)
    patch_p.center = (posx_p, posy_p)

    line_mer.set_data(xdata_mer, ydata_mer)
    line_v.set_data(xdata_v, ydata_v)
    line_e.set_data(xdata_e, ydata_e)
    line_mar.set_data(xdata_mar, ydata_mar)
    line_j.set_data(xdata_j, ydata_j)
    line_s.set_data(xdata_s, ydata_s)
    line_u.set_data(xdata_u, ydata_u)
    line_n.set_data(xdata_n, ydata_n)
    line_p.set_data(xdata_p, ydata_p)

    return (patch_sun, patch_mercury, patch_venus, patch_earth, patch_mars,
            patch_j, patch_s, patch_u, patch_n, patch_p, line_mer, line_v,
            line_e, line_mar, line_j, line_s, line_u, line_n, line_p)


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100000,
                               interval=1e-40, blit=True)
ax.set_xlabel("Distance (AU)")
ax.set_ylabel("Distance (AU)")
plt.show()

score_neptune = 0
score_uranus = 0
score_saturn = 0
score_jupiter = 0
score_mars = 0
score_earth = 0
score_venus = 0
score_mercury = 0
i = 0
while i <= 100000:

    posx_mercury = radius_mercury * np.cos(theta_mercury * i)
    posy_mercury = radius_mercury * np.sin(theta_mercury * i)

    posx_venus = radius_venus * np.cos(theta_venus * i)
    posy_venus = radius_venus * np.sin(theta_venus * i)

    posx_earth = radius_earth * np.cos(theta_earth * i)
    posy_earth = radius_earth * np.sin(theta_earth * i)

    posx_mars = radius_mars * np.cos(theta_mars * i)
    posy_mars = radius_mars * np.sin(theta_mars * i)

    posx_j = r_j * np.cos(theta_j * i)
    posy_j = r_j * np.sin(theta_j * i)

    posx_s = r_s * np.cos(theta_s * i)
    posy_s = r_s * np.sin(theta_s * i)

    posx_u = r_u * np.cos(theta_u * i)
    posy_u = r_u * np.sin(theta_u * i)

    posx_n = r_n * np.cos(theta_n * i)
    posy_n = r_n * np.sin(theta_n * i)

    posx_p = r_p * np.cos(theta_p * i)
    posy_p = r_p * np.sin(theta_p * i)

    diff_pos1x = posx_mercury - posx_p
    diff_pos1y = posy_mercury - posy_p
    diff_pos2x = posx_venus - posx_p
    diff_pos2y = posy_venus - posy_p
    diff_pos3x = posx_earth - posx_p
    diff_pos3y = posy_earth - posy_p
    diff_pos4x = posx_mars - posx_p
    diff_pos4y = posy_mars - posy_p
    diff_pos5x = posx_j - posx_p
    diff_pos5y = posy_j - posy_p
    diff_pos6x = posx_s - posx_p
    diff_pos6y = posy_s - posy_p
    diff_pos7x = posx_u - posx_p
    diff_pos7y = posy_u - posy_p
    diff_pos8x = posx_n - posx_p
    diff_pos8y = posy_n - posy_p

    d1 = np.sqrt(diff_pos1x**2 + diff_pos1y**2)
    d2 = np.sqrt(diff_pos2x**2 + diff_pos2y**2)
    d3 = np.sqrt(diff_pos3x**2 + diff_pos3y**2)
    d4 = np.sqrt(diff_pos4x**2 + diff_pos4y**2)
    d5 = np.sqrt(diff_pos5x**2 + diff_pos5y**2)
    d6 = np.sqrt(diff_pos6x**2 + diff_pos6y**2)
    d7 = np.sqrt(diff_pos7x**2 + diff_pos7y**2)
    d8 = np.sqrt(diff_pos8x**2 + diff_pos8y**2)

    if d8 < d1 and d8 < d2 and d8 < d3 and d8 < d4 and d8 < d5 and d8 < d6 and d8 < d7:
        score_neptune += 1
    elif d7 < d1 and d7 < d2 and d7 < d3 and d7 < d4 and d7 < d5 and d7 < d6:
        score_uranus += 1
    elif d6 < d1 and d6 < d2 and d6 < d3 and d6 < d4 and d6 < d5:
        score_saturn += 1
    elif d5 < d1 and d5 < d2 and d5 < d3 and d5 < d4:
        score_jupiter += 1
    elif d4 < d1 and d4 < d2 and d4 < d3:
        score_mars += 1
    elif d3 < d1 and d3 < d2:
        score_earth += 1
    elif d2 < d1:
        score_venus += 1
    else:
        score_mercury += 1
    i += 1
print("Number of days each planet is closest to Earth")
print("Mercury    |    Venus    |    Earth    |     Mars    |  Jupiter  |  Saturn   |  Uranus   |  Neptune")
# print(score_mercury, "      |   ", score_venus, "       |   ", score_earth, "   |    ", score_mars, " | ", score_jupiter, " | ", score_saturn, "  |       ", score_uranus, "         | ", score_neptune)
print(score_mercury, "     |   ", score_venus, "   |   ", score_earth, "   |    ", score_mars, "  | ", score_jupiter, "  | ", score_saturn, "  |  ", score_uranus, " | ", score_neptune)
