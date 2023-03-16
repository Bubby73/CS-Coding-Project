import pyglet
import math
import random
numObjects = 3
pygletWindowsize = 1200, 600
window = pyglet.window.Window(pygletWindowsize[0], pygletWindowsize[1])
print(type(pygletWindowsize))

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

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.circle.x = self.x
        self.circle.y = self.y
        self.circle.draw() # draw the planet       
            



planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#new planet
def newplanet():
        planet = Planet(random.choice(planets), random.randint(0, 1200), random.randint(0, 600), random.randint(50, 1000), random.randint(0, 360), random.randint(1, 5))
        return planet

numObjects = 3

objects = [] # list of objects

for i in range(0, numObjects): 
    objects.append(newplanet()) # add new planet to list


running = True
while running == True:
    pyglet.clock.tick()
    window.switch_to()
    window.dispatch_events()
    window.flip()
    
    window.clear()
    for planet in objects: # for each planet in the list
        if planet.x > pygletWindowsize[0] or planet.x < 0 or planet.y > pygletWindowsize[1] or planet.y < 0: # if the planet goes off the screen
            objects.remove(planet) # remove the planet from the list 
            planet = newplanet() # create a new planet
            objects.append(planet) # add the new planet to the list
        planet.update() 
     

    #detect if escape key is pressed
    @window.event
    def on_key_press(symbol, modifiers):  
        global running    
        if symbol == pyglet.window.key.ESCAPE:
             running = False