from tkinter import *
import pyglet
import math
import random

#window setup
window = pyglet.window.Window(1200, 600)
key = pyglet.window.key
objects = []
root = Tk()
root.title("CS Solar System")
xwidth = 350
screen_resolution = str(xwidth)+'x'+str(190)

            

root.geometry(screen_resolution)

#setup tkinter interface
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

planetDeletelabel = Label(root, text="Delete Planet:")
planetDeletelabel.grid(row=0, column=2)
planetDeleteEntry = Entry(root, width = 15, relief=FLAT)
planetDeleteEntry.grid(row=0, column=3)


#new planet class
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
        
randomnames = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Moon", "Sun"]

#new planet
def new_planet():
    if var.get() == 1:
        planet = Planet(random.choice(randomnames), random.randint(200, 1000), random.randint(100, 500), random.randint(50, 500), random.randint(0, 360), random.randint(1, 15))
    else:
        planet = Planet(nameEntry.get(), float(xcoordEntry.get()), float(ycoordEntry.get()), float(massEntry.get()), float(directionEntry.get()), float(velocityEntry.get()))
    objects.append(planet)
    planet.draw()

#delete planet
def deletePlanet():
    planetTodelete = planetDeleteEntry.get()
    for planet in objects:
        planetName = planet.name
        if planetName.lower() == planetTodelete.lower():
            objects.remove(planet)
            planet.circle.delete()
            currentPlanetslabel.config(text = currentPlanets)


            
#new planet button
generateButton = Button(root, text="Generate", command=new_planet)
generateButton.grid(row=6, column=0)

#delete planet button
planetDeletebutton = Button(root, text="Delete Planet", command=deletePlanet)
planetDeletebutton.grid(row=1, column=3)

running = True
paused = False

def pause():
    global paused
    paused = True
    pauseButton.config(text="Resume")
    pauseButton.config(command=resume)
    pausedLabel = pyglet.text.Label("Paused", font_name='Times New Roman', font_size=16, x = 30, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    window.flip()
    print("Paused")


def resume():
    global paused
    paused = False
    pauseButton.config(text="Pause")
    pauseButton.config(command=pause)
    pausedLabel = pyglet.text.Label("Paused", font_name='Times New Roman', font_size=16, x = 30, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255))
    pausedLabel.delete()
    window.flip()
    print("Unpaused")

pauseButton = Button(root, text="Pause", command=pause)
pauseButton.grid(row=2, column=3)


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

        exitLabel = pyglet.text.Label("Press ESC to exit", font_name='Times New Roman', font_size=12, x=1130, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    else:
        window.switch_to()
        window.dispatch_events()
        #window.flip()
        root.update()
        currentPlanets = ""
        for planet in objects:
            currentPlanets += planet.name + "\n"
        currentPlanetslabel.config(text = currentPlanets)
        
        
    screen_resolution = str(xwidth)+'x'+str(190 + 15*len(objects))
        
    root.geometry(screen_resolution)


    #detect if escape key is pressed
  
    @window.event()
    def on_key_press(symbol, modifiers):
        global running
        global paused
        
        if symbol == key.ESCAPE:
            running = False
            window.close()
            root.destroy()
                
        if symbol == key.P and paused == False:
            pause()
            window.flip()
            symbol = key.R

        if symbol == key.P and paused == True:
            resume()
            window.flip()
            symbol = key.R
            

         
        
     


   
        
    

    #print(paused)

    