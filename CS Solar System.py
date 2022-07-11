from symtable import Symbol
from tkinter import *
import pyglet
import math
import random
window = pyglet.window.Window(1200, 600)

key = pyglet.window.key
objects = []
root = Tk()
root.title("CS Solar System")
screen_resolution = str(200)+'x'+str(190)

root.geometry(screen_resolution)

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

var = IntVar()
nameCheckbox = Checkbutton(root, text="Ranomize", variable=var)
nameCheckbox.grid(row=6, column=1)

currentPlanetLabel = Label(root, text="Current Planets:")
currentPlanetLabel.grid(row=7, column=0)
currentPlanets = ""
currentPlanetslabel = Label(root, text = currentPlanets)
currentPlanetslabel.grid(row=8, column=0)



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
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=self.colour)


    def draw(self):
        self.circle.draw()

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.circle.x = self.x
        self.circle.y = self.y
        
randomnames = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
#new planet
def new_planet():
    if var.get() == 1:
        planet = Planet(random.choice(randomnames), random.randint(200, 1000), random.randint(100, 500), random.randint(50, 500), random.randint(0, 360), random.randint(1, 15))
    else:
        planet = Planet(nameEntry.get(), float(xcoordEntry.get()), float(ycoordEntry.get()), float(massEntry.get()), float(directionEntry.get()), float(velocityEntry.get()))
    objects.append(planet)
    planet.draw()

generateButton = Button(root, text="Generate", command=new_planet)
generateButton.grid(row=6, column=0)

running = True
paused = False
while running:
    if not paused:
        window.switch_to()
        window.dispatch_events()
        window.flip()
        root.update()
        window.clear()
        temp_object_list = []
        for planet in objects:
            if planet.x > 1200 or planet.x < 0 or planet.y > 600 or planet.y < 0:
                temp_object_list.append(planet)


            else:
                planet.update()
                planet.draw()

        #add planets to current planets label
        currentPlanets = ""
        for planet in objects:
            currentPlanets += planet.name + "\n"
        currentPlanetslabel.config(text = currentPlanets)
                    
        for planet in temp_object_list:
            objects.remove(planet)
    else:
        window.switch_to()
        window.dispatch_events()
        window.flip()
        root.update()
        currentPlanets = ""
        for planet in objects:
            currentPlanets += planet.name + "\n"
        currentPlanetslabel.config(text = currentPlanets)

    screen_resolution = str(200)+'x'+str(190 + 15*len(objects))

    root.geometry(screen_resolution)


    #detect if escape key is pressed
    @window.event
    def on_key_press(symbol, modifiers):  
        global running    
        global paused
        if symbol == pyglet.window.key.ESCAPE:
            running = False
                    
        if paused == False and symbol == pyglet.window.key.P:
            paused = True
            #say paused on screen
            pausedLabel = pyglet.text.Label("Paused", font_name='Times New Roman', font_size=16, x = 30, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255))
            pausedLabel.draw()
    
        elif paused == True and symbol == pyglet.window.key.P:
            paused = False

        print(paused)