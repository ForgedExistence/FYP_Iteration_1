import matplotlib.pyplot as plt
# from matplotlib import animation
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

    def get_animation(self):
        self.patch = plt.Circle((.1, -.1), 4879e3, fc='k')
        self.line = ax.plot([], [], lw=4879e3, color='k')
        self.xdata, self.ydata = [], []

        def init():
            self.patch.center = (0, 0)
            ax.add_patch(self.patch)
            self.line.set_data([], [])
            return self.patch, self.line,

        def animate(i):
            self.posx, self.posy = self.patch.center
            self.posx = self.radius * np.cos(self.theta * i)
            self.posy = self.radius * np.sin(self.theta * i)
            self.xdata.append(self.posx)
            self.ydata.append(self.posy)
            self.patch.center(self.posx, self.posy)
            self.line.set_data(self.xdata, self.ydata)

            return self.patch, self.line,

    def score_count(self, other):
        self.score = 0
        while i <= 10000:
            self.posx = self.radius * np.cos(self.theta * i)
            self.posy = self.radius * np.sin(self.theta * i)
            other.posx = self.radius * np.cos(other.theta * i)
            other.posy = self.radius * np.sin(other.theta * i)
            diffx = self.posx - other.posx
            diffy = self.posy - other.posy

            d = np.sqrt(diffx**2 + diffy**2)
        return d

# Sun = Body(1.99e+30, "Sun", 0, 0)


Body(0.33e+24, "Mercury", 47.4e+3, 57.9e9)
Body(4.87e+24, "Venus", 35e+3, 108.2e9)
Body(5.97e+24, "Earth", 29e+3, 149.6e9)
Body(0.642e+24, "Mars", 24.1e+3, 227.9e9)

ax.set_xlabel("Distance (AU)")
ax.set_ylabel("Distance (AU)")
for i in Body.solar_sys:
    print(i)
