# all info is on README
# lets start by making a class system so the data
# can be used easily


class Body:
    solar_sys = []

    def __init__(self, mass, name, velocity, radius):
        self.mass = mass
        self.name = name
        self.velocity = velocity
        self.radius = radius
        self.id = len(Body.solar_sys)
        Body.solar_sys.append(self)

    def __repr__(self):
        my_rep = f"""
        Body name: {self.name}
        Bodyid: {self.id}
        Body mass: {self.mass}
        Body velocity: {self.velocity}
        Body radius: {self.radius}
        --------------
        """
        return my_rep


Body(1.99e+30, "Sun", 0, 0)
Body(0.33e+24, "Mercury", 47.4e+3, 57.9e+9)
Body(4.87e+24, "Venus", 35e+3, 108.2e+9)
Body(5.97e+24, "Earth", 29e+3, 149.6e+9)
Body(0.642e+24, "Mars", 24.1e+3, 227.9e+9)

input()
for i in Body.solar_sys:
    print(i)
