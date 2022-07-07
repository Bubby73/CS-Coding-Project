import pyglet
import math
import random

window = pyglet.window.Window(1200, 600)

key = pyglet.window.key

class Planet():
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

        self.circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=self.color)

    def draw(self):
        self.circle.draw()

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.circle.x = self.x
        self.circle.y = self.y

def new_planet():
    sun = Planet(planets[0], random.randint(0, 1200), random.randint(0, 600), random.randint(100, 1200), random.randint(0,360), random.randint(5,15))
    return sun

planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

sun = new_planet()
mercury = new_planet()
running = True
while running == True:
    pyglet.clock.tick()
    window.switch_to()
    window.dispatch_events()
    window.flip()
    
    window.clear()
    sun.draw()
    sun.update()
    mercury.draw()
    mercury.update()

    if sun.x > 1200 or sun.x < 0 or sun.y > 600 or sun.y < 0:
        sun = new_planet()
    if mercury.x > 1200 or mercury.x < 0 or mercury.y > 600 or mercury.y < 0:
        mercury = new_planet()

    #detect if escape key is pressed
    @window.event
    def on_key_press(symbol, modifiers):  
        global running    
        if symbol == pyglet.window.key.ESCAPE:
             running = False
