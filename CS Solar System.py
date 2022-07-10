from tkinter import *
import pyglet
import math
import random
numObjects = 20
window = pyglet.window.Window(1200, 600)

key = pyglet.window.key

root = Tk()

nameLabel = Label(root, text="Object Name:")
nameLabel.grid(row=0, column=0)

nameEntry = Entry(root, width = 8, relief=FLAT)
nameEntry.grid(row=0, column=1)

massLabel = Label(root, text="Mass:")
massLabel.grid(row=1, column=0)

massEntry = Entry(root, width = 8, relief=FLAT)
massEntry.grid(row=1, column=1)

directionLabel = Label(root, text="Direction:")
directionLabel.grid(row=2, column=0)

directionEntry = Entry(root, width = 8, relief=FLAT)
directionEntry.grid(row=2, column=1)

velocityLabel = Label(root, text="Velocity:")
velocityLabel.grid(row=3, column=0)

velocityEntry = Entry(root, width = 8, relief=FLAT)
velocityEntry.grid(row=3, column=1)

xcoordLabel = Label(root, text="X Coordinate:")
xcoordLabel.grid(row=4, column=0)

xcoordEntry = Entry(root, width = 8, relief=FLAT)
xcoordEntry.grid(row=4, column=1)

ycoordLabel = Label(root, text="Y Coordinate:")
ycoordLabel.grid(row=5, column=0)

ycoordEntry = Entry(root, width = 8, relief=FLAT)
ycoordEntry.grid(row=5, column=1)

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
        planet = Planet(random.choice(planets), random.randint(0, 1200), random.randint(0, 600), random.randint(10, 300), random.randint(0, 360), random.randint(1, 10))
        return planet

objects = []

for i in range(0, numObjects):
    objects.append(new_planet())


running = True
while running:
    window.switch_to()
    window.dispatch_events()
    window.flip()

    window.clear()
    temp_object_list = []
    for planet in objects:
        if planet.x > 1200 or planet.x < 0 or planet.y > 600 or planet.y < 0:
            temp_object_list.append(new_planet())
        else:
            temp_object_list.append(planet)

        planet.update()
        planet.draw()

    objects = temp_object_list

    #detect if escape key is pressed
    @window.event
    def on_key_press(symbol, modifiers):  
        global running    
        if symbol == pyglet.window.key.ESCAPE:
             running = False

    #generateButton = Button(root, text="Generate")
    #generateButton.grid(row=6, column=0)

mainloop()