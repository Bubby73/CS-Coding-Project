import pyglet
import math
import random
window = pyglet.window.Window(1200, 600)

class planet():
    def __init__(self, name, x, y, mass, direction, velocity):
        self.name = name
        self.mass = mass
        self.radius = mass / 10
        self.x = x
        self.y = y
        self.direction = direction
        self.velocity = velocity
        self.vx = math.sin(math.radians(self.direction)) * self.velocity
        self.vy = math.cos(math.radians(self.direction)) * self.velocity
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.planet = pyglet.shapes.Circle(self.x, self.y, self.radius, color=self.color)
        self.planet.draw()

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.planet.x = self.x
        self.planet.y = self.y
        self.planet.draw()

bodies = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
Sun = planet(bodies[0], random.randint(0,1200), random.randint(0, 600), random.randint(100, 1200), random.randint(0,360), random.randint(1,10))

def newSun(Sun):
    Sun = planet(bodies[0], random.randint(0, 1200), random.randint(0, 600), random.randint(100, 1200), random.randint(0,360), random.randint(5,15))
    return Sun



def update(dt):
    pyglet.clock.tick()
    window.clear()
    global Sun
    Sun.update()
    if Sun.x > 1200 or Sun.x < 0 or Sun.y > 600 or Sun.y < 0: 
        Sun = newSun(Sun)
       


pyglet.clock.schedule_interval(update, 1/120)






pyglet.app.run()

