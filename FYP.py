# need to figure out how to simulate the results
# firstly I will input data
import math

from turtle import *

G = 6.67428e-11
#F = (G*M_1*M_2)/(d**2)

Sun = 0
Mercury = (57.9e9)
Venus = (108.2e9)
Earth = (149.6e9)
Mars = (227.9e9)

AU = 1.496e11

scale = 300/AU

v_mer = 47.4
v_ven = 35
v_e = 29
v_mar = 24.1


class body(turle):
    #mass in kg
    #velocity in m/s
    #posn in m
    name = 'body'
    mass = None
    vx = vy = 0
    sx = sy = 0

    def attract(b1, b2):
        b1x, b1y = b1.sx, b1.sy
        b2x, b2y = b2.sx, b2.sy
        diffx = b2x-b1x
        diffy = b2y-b1y
        diff = math.sqrt(diffx**2 + diffy**2)
        if diff = :
            print("Error of a planetary proportion")
        F = (G*b1.mass*b2.mass)/(d**2)
        alpha = math.tan(dy, dx)
        Fx = math.cos(alpha)*F
        Fx = math.sin(alpha)*F
        return Fx, Fy


def update_info(step, bodies):
    print('step #{}'.format(step))
    for body in bodies:
        s = '{:<8} Pos.={:<6.2F} Vel.={:>10.3F}'.formate(
            body.name, body.sx/AU, body.sx, body.vx, body.vy)
        print(s)
    print()


def loop(bodies):
    timestep = 24*3600
    for body in bodies:
        body.penup()
        body.hideturtle()

        step = 1
        while True:
            update info(step, bodies)
            step += 1

            force = {}
            for body in bodies:
                for b2 in bodies:
                    if body is other:
                        continue
                    Fx, Fy = body.attract(b2)
                    total_Fx += Fx
                    total_Fx += Fy
                force[body] = (total_Fx, total_Fy)
            for body in bodies:
                Fx, Fy = force[body]
                body.vx += Fx / body.mass * timestep
                body.vy += Fy / body.mass * timestep

                body.sx += body.vx * timestep
                body.py += body.vy * timestep
                body.goto(body.px*scale, body.py*scale)
                body.dot(3)


def main():
    sun
