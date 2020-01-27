# Right so what happened with the first test was weird how can I get around it
# I can start in a similar manner but change things
# priority is getting a sim running well enough to show circular orbits
import math
from turtle import *


# I got a large amount of info from NASA links in README

# the formula we will be using is from Newtons Law of gravitation
# firstly some constants and stuff

G = 6.67e-11  # m^3 kg^-1 s^-2

# Radii of planets and sun
# For simplicity sun is of radius 0 and doesnt move
sun_r = 0
mercury_r = 57.9e+9
venus_r = 108.2e+9
earth_r = 149.6e+9
mars_r = 227.9e+9

# masses
sun_m = 1.99e+30
mercury_m = 0.33e+24
venus_m = 4.87e+24
earth_m = 5.97e+24
mars_m = 0.642e+24

# we know their average velocities
# all in m/s
sun_v = 0
mercury_v = 47.4e+3
venus_v = 35e+3
earth_v = 29e+3
mars_v = 24.1e+3

# all of our important data is here so whats next?
# hmmm
# ah yes we should prolly increase the tear count on this project and split up
# the velocities into x and y directions
# need a loop to compute the velocities

bodies_v = [mercury_v, venus_v, earth_v, mars_v]
bodies_r = [mercury_r, venus_r, earth_r, mars_r]
bodies_m = [mercury_m, venus_m, earth_m, mars_m]

posx, posy = 0, 0
mass = None

# how do i split up the velocities into x and y????

# I guess because of the bodies moving in a circle the
# x and y velocities are

# lets do it for one planet first


# def attraction(Body, Sun):
#     if body is Sun:
#         # need to stop objects atracting to themselves
#         raise ValueError("Attraction to itself" % body.name)
#     # all bodies will be taken from the centre of the solar system i.e.
#       the sun distance will be from the object to the sun always
#     sx, sy = Body.posx, Body.posy
#     d = math.sqrt(sx**2 + sy**2)
#
#     if d == 0:
#         raise ValueError("Abandon ship")
#
#     f = (G*sun_m*Body.mass)/(d**2)
#
#     theta = math.atan2(sx, sy)
#     fx = f*math.cos(theta)
#     fy = f*math.sin(theta)
#     return fx, fy
#
# # right i need to
