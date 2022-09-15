from turtle import circle
from unittest import runner 
import pyglet
import math
import random
from pyglet import clock 

window = pyglet.window.Window(1200, 600)
window.set_caption("View Window")
key = pyglet.window.key
objects = []
planet_image = pyglet.image.load("planet.png")
batch = pyglet.graphics.Batch()

class Planet():
    def __init__(self, name, x, y, mass, direction, velocity):
        self.name = name
        self.mass = mass
        self.radius = mass / 300
        self.x = x 
        self.y = y 
        self.direction = direction
        self.velocity = velocity 
        self.vx = math.sin(math.radians(self.direction)) * self.velocity # working out x and y velocities in relation to the direction
        self.vy = math.cos(math.radians(self.direction)) * self.velocity
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circle = pyglet.sprite.Sprite(planet_image, x=self.x, y=self.y, batch=batch)
        self.circle.scale = self.radius
        self.circle.color = self.colour
        
    def draw(self):
        self.circle.draw()

    # updates the position of the planet
    def update(self):
        # give planets gravity
        for planet in objects:
            if planet != self:
                dx = planet.x - self.x
                dy = planet.y - self.y
                distance = math.sqrt(dx ** 2 + dy ** 2)
                force = self.mass * planet.mass / (distance ** 2) + 0.000000001
                ax = dx / distance * force
                ay = dy / distance * force
                self.vx += ax
                self.vy += ay
        # update position
        self.x += self.vx
        self.y += self.vy
        self.circle.x = self.x
        self.circle.y = self.y
    
class Trales():
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.circle = pyglet.sprite.Sprite(planet_image, x=self.x, y=self.y, batch=batch)
        self.circle.scale = 0.1
        self.circle.color = self.colour

    def draw(self):
        self.circle.draw()

    def update(self):
        self.circle.x = self.x
        self.circle.y = self.y

planetNamelist = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Moon", "Sun"]

def new_planet():
    name = random.choice(planetNamelist)
    mass = random.randint(5, 20)
    direction = random.randint(0, 360)
    velocity = random.randint(1,4)
    x = random.randint(100, 1100)
    y = random.randint(100, 500)
    planet = Planet(name, x, y, mass, direction, velocity) 
    objects.append(planet)
    planet.draw()

running = True 
while running:
    dt = clock.tick()
    #show fps
    fpsLabel = pyglet.text.Label("FPS: " + str(round(clock.get_fps(), 1)), font_name='Times New Roman', font_size=16, x = 50, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    window.switch_to()
    window.dispatch_events()
    window.flip()
    window.clear()
    temp_object_list = []
    for planet in objects: # updates the position of each planet
        if planet.x > 1200 or planet.x < 0 or planet.y > 600 or planet.y < 0: # if planet of screen, delete
            temp_object_list.append(planet)
            
            

        else:
            planet.update()
            planet.draw()

    # add planets to current planets label in tkinter window
    currentPlanets = ""
    for planet in objects:
        currentPlanets += planet.name + "\n"
                
    for planet in temp_object_list:
        objects.remove(planet)

    exitLabel = pyglet.text.Label("Press ESC to exit", font_name='Times New Roman', font_size=12, x=1130, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()

    @window.event()
    def on_key_press(symbol, modifiers):    
        if symbol == key.S:
            new_planet()

        global running
        if symbol == key.ESCAPE:
            running = False
            window.close()
            
    
    

