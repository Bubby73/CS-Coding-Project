import pyglet
import math
import random
numObjects = 3
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
        
            



planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#new planet
def new_planet():
        planet = Planet(random.choice(planets), random.randint(0, 1200), random.randint(0, 600), random.randint(50, 1000), random.randint(0, 360), random.randint(1, 10))
        return planet

objects = []

for i in range(0, numObjects):
    objects.append(new_planet())


running = True
while running == True:
    pyglet.clock.tick()
    window.switch_to()
    window.dispatch_events()
    window.flip()
    
    window.clear()
    for planet in objects:
        if planet.x > 1200 or planet.x < 0 or planet.y > 600 or planet.y < 0:
            objects.remove(planet)
            planet = new_planet()
            objects.append(planet)
            
        planet.update()
        planet.draw()

    #detect if escape key is pressed
    @window.event
    def on_key_press(symbol, modifiers):  
        global running    
        if symbol == pyglet.window.key.ESCAPE:
             running = False