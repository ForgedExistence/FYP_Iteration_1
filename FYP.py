# need to figure out how to simulate the results
# firstly I will input data
import math

from turtle import *

G = 6.67428e-11
#F = (G*M_1*M_2)/(d**2)

Sun = 0
Mercury = (57.9e+9)
Venus = (108.2e+9)
Earth = (149.6e+9)
Mars = (227.9e+9)

AU = 1.496e+11

scale = 250/AU

v_mer = 47.4
v_ven = 35
v_e = 29
v_mar = 24.1


m_sun = 1.988500e+30
m_mercury = 0.330e+24
m_venus = 4.87e+24
m_earth = 5.97e+24
m_mars = 0.642e+24


class body(Turtle):
    #mass in kg
    #velocity in m/s
    #posn in m
    name = 'Body'
    mass = None
    vx = vy = 0
    sx = sy = 0

    def attract(b1, b2):
        if b1 is b2:
            raise ValueError("attraction of object %r to itself requested" % b1.name)
        b1x, b1y = b1.sx, b1.sy
        b2x, b2y = b2.sx, b2.sy
        diffx = b2x-b1x
        diffy = b2y-b1y
        diff = math.sqrt(diffx**2 + diffy**2)
        if diff == 0:
            print("Error of a planetary proportion")
        F = (G*b1.mass*b2.mass)/(diff**2)
        alpha = math.atan2(diffy, diffx)
        Fx = math.cos(alpha)*F
        Fy = math.sin(alpha)*F
        return Fx, Fy


def update_info(step, bodies):
    print('step #{}'.format(step))
    for body in bodies:
        s = '{:<8} Pos.={:>6.2F}{:>6.2F} Vel.={:>10.3F}{:>10.3F}'.format(
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
            update_info(step, bodies)
            step += 1

            force = {}
            for body in bodies:
                total_Fx = total_Fy = 0.0
                for b2 in bodies:
                    if body is b2:
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
                body.sy += body.vy * timestep
                body.goto(body.sx*scale, body.sy*scale)
                body.dot(5)


def main():
    sun = body()
    sun.name = 'Sun'
    sun.mass = m_sun
    sun.pencolor('yellow')

    mercury = body()
    mercury.name = 'Mercury'
    mercury.mass = m_mercury
    mercury.sx = Mercury
    mercury.vy = v_mer*1000
    mercury.pencolor('brown')

    venus = body()
    venus.name = 'Venus'
    venus.mass = m_venus
    venus.sx = Venus
    venus.vy = v_ven*1000
    venus.pencolor('orange')

    earth = body()
    earth.name = 'Earth'
    earth.mass = m_earth
    earth.sx = Earth
    earth.vy = v_e
    earth.pencolor('green')

    mars = body()
    mars.name = 'Mars'
    mars.mass = m_mars
    mars.sx = Mars
    mars.vy = v_mar
    mars.pencolor('red')

    loop([mercury, venus, earth, mars])


if __name__ == '__main__':
    main()
