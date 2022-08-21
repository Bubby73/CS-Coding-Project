# import libraries
from tkinter import *
from turtle import circle 
import pyglet
import math
import random
from pyglet import clock 

# window setup
window = pyglet.window.Window(1200, 600)
window.set_caption("View Window")
key = pyglet.window.key
objects = []
root = Tk()
root.title("Control Panel")
xwidth, yheight = 400, 250
screen_resolution = str(xwidth)+'x'+str(yheight)
root.geometry(screen_resolution)
planet_image = pyglet.image.load("planet.png")
batch = pyglet.graphics.Batch()

# setup tkinter interface
nameLabel = Label(root, text="Object Name:")
nameLabel.grid(row=0, column=0)

nameEntry = Entry(root, width = 8, relief=FLAT)
nameEntry.grid(row=0, column=1)

varName = IntVar()
nameCheckbox = Checkbutton(root, text="Ranomize Name", variable=varName)
nameCheckbox.grid(row=0, column=2)

massLabel = Label(root, text="Mass:")
massLabel.grid(row=1, column=0)

massEntry = Entry(root, width = 8, relief=FLAT)
massEntry.grid(row=1, column=1)

varMass = IntVar()
massCheckbox = Checkbutton(root, text="Ranomize Mass", variable=varMass)
massCheckbox.grid(row=1, column=2)

directionLabel = Label(root, text="Direction:")
directionLabel.grid(row=2, column=0)

directionEntry = Entry(root, width = 8, relief=FLAT)
directionEntry.grid(row=2, column=1)

varDirection = IntVar()
dirCheckbox = Checkbutton(root, text="Ranomize Direction", variable=varDirection)
dirCheckbox.grid(row=2, column=2)

velocityLabel = Label(root, text="Velocity:")
velocityLabel.grid(row=3, column=0)

velocityEntry = Entry(root, width = 8, relief=FLAT)
velocityEntry.grid(row=3, column=1)

varVelocity = IntVar()
velCheckbox = Checkbutton(root, text="Ranomize Velocity", variable=varVelocity)
velCheckbox.grid(row=3, column=2)

xcoordLabel = Label(root, text="X Coordinate:")
xcoordLabel.grid(row=4, column=0)

xcoordEntry = Entry(root, width = 8, relief=FLAT)
xcoordEntry.grid(row=4, column=1)

varXcoord = IntVar()
xCheckbox = Checkbutton(root, text="Ranomize X coord", variable=varXcoord)
xCheckbox.grid(row=4, column=2)

ycoordLabel = Label(root, text="Y Coordinate:")
ycoordLabel.grid(row=5, column=0)

ycoordEntry = Entry(root, width = 8, relief=FLAT)
ycoordEntry.grid(row=5, column=1)

varYcoord = IntVar()
yCheckbox = Checkbutton(root, text="Ranomize Y coord", variable=varYcoord)
yCheckbox.grid(row=5, column=2)

varAll = IntVar()
allCheckbox = Checkbutton(root, text="Randomize All", variable=varAll)
allCheckbox.grid(row=5, column=3)

currentPlanetLabel = Label(root, text="Current Planets:")
currentPlanetLabel.grid(row=7, column=0)
currentPlanets = ""
currentPlanetslabel = Label(root, text = currentPlanets)
currentPlanetslabel.grid(row=8, column=0)

planetDeletelabel = Label(root, text="Delete Planet:")
planetDeletelabel.grid(row=6, column=2)
planetDeleteEntry = Entry(root, width = 15, relief=FLAT)
planetDeleteEntry.grid(row=6, column=3)

velocityMultiplierlabel = Label(root, text="Velocity Multiplier:")
velocityMultiplierlabel.grid(row=0, column=3)
velocityMultiplierslider = Scale(root, from_=1, to=15, orient=HORIZONTAL, length=100)
velocityMultiplierslider.grid(row=1, column=3)
# set slider to 5
velocityMultiplierslider.set(5)

generateMultiplierlabel = Label(root, text="Generate Multiplier:")
generateMultiplierlabel.grid(row=2, column=3)
generateMultiplierslider = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=100)
generateMultiplierslider.grid(row=3, column=3)


# new planet class
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
                self.vx += ax / 2
                self.vy += ay / 2
        # update position
        self.x += self.vx
        self.y += self.vy
        self.circle.x = self.x
        self.circle.y = self.y

# random planet names      
planetNamelist = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Moon", "Sun"]

# new planet
def new_planet():
    for i in range(generateMultiplierslider.get()):
        if varAll.get() == 1:
            name = random.choice(planetNamelist)
            mass = random.randint(5, 50)
            direction = random.randint(0, 360)
            velocity = random.randint(1,5)
            x = random.randint(100, 1100)
            y = random.randint(100, 500)
            nameEntry.config(bg = "white")
            nameCheckbox.select()
            massEntry.config(bg = "white")
            massCheckbox.select()
            directionEntry.config(bg = "white")
            dirCheckbox.select()
            velocityEntry.config(bg = "white")
            velCheckbox.select()
            xcoordEntry.config(bg = "white")
            xCheckbox.select()
            ycoordEntry.config(bg = "white")
            yCheckbox.select()
        else:
            if varName.get() == 1:
                name = random.choice(planetNamelist)
            else:
                if nameEntry.get() == "":
                    nameEntry.config(bg = "red")
                else:
                    name = nameEntry.get()
                    nameEntry.config(bg = "white")
            if varMass.get() == 1:
                mass = random.randint(5, 50)
            else:
                try:
                    mass = int(massEntry.get())
                    massEntry.config(bg = "white")
                except:
                    massEntry.config(bg = "red")
            if varDirection.get() == 1:
                direction = random.randint(0, 360)
            else:
                try:
                    direction = int(directionEntry.get())
                    directionEntry.config(bg = "white")
                except:
                    directionEntry.config(bg = "red")
            if varVelocity.get() == 1:
                velocity = random.randint(1, 5)
            else:
                try:
                    velocity = int(velocityEntry.get())
                    velocityEntry.config(bg = "white")
                except:
                    velocityEntry.config(bg = "red")
            if varXcoord.get() == 1:
                x = random.randint(100, 1100)
            else:
                try:
                    x = int(xcoordEntry.get())
                    xcoordEntry.config(bg = "white")
                except:
                    xcoordEntry.config(bg = "red")
            if varYcoord.get() == 1:
                y = random.randint(100, 500)
            else:
                try:
                    y = int(ycoordEntry.get())
                    ycoordEntry.config(bg = "white")
                except:
                    ycoordEntry.config(bg = "red")
        planet = Planet(name, x, y, mass, direction, velocity) # sets planet attributes
        nameEntry.delete(0, END)
        nameEntry.insert(0, name)
        massEntry.delete(0, END)
        massEntry.insert(0, mass)
        directionEntry.delete(0, END)
        directionEntry.insert(0, direction)
        velocityEntry.delete(0, END)
        velocityEntry.insert(0, velocity)
        xcoordEntry.delete(0, END)
        xcoordEntry.insert(0, x)
        ycoordEntry.delete(0, END)
        ycoordEntry.insert(0, y)
        objects.append(planet)
        planet.draw()

# delete planet
def deletePlanet():
    planetTodelete = planetDeleteEntry.get()
    for planet in objects:
        planetName = planet.name
        if planetName.lower() == planetTodelete.lower():
            objects.remove(planet)
            planet.circle.delete()
            currentPlanetslabel.config(text = currentPlanets)
            break


            
# new planet button
generateButton = Button(root, text="Generate", command=new_planet)
generateButton.grid(row=6, column=0)

# delete planet button
planetDeletebutton = Button(root, text="Delete Planet", command=deletePlanet)
planetDeletebutton.grid(row=7, column=3)

running = True
paused = False

# pause procedure
def pause():
    global paused
    paused = True
    pauseButton.config(text="Resume")
    pauseButton.config(command=resume)
    pausedLabel = pyglet.text.Label("Paused", font_name='Times New Roman', font_size=16, x = 30, y=570, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    window.flip()
    print("Paused")

# resume procedure
def resume():
    global paused
    paused = False
    pauseButton.config(text="Pause")
    pauseButton.config(command=pause)
    pausedLabel = pyglet.text.Label("Paused", font_name='Times New Roman', font_size=16, x = 30, y=570, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).delete()
    window.flip()
    print("Unpaused")

pauseButton = Button(root, text="Pause", command=pause) # pause button
pauseButton.grid(row=7, column=2)



 # main loop
while running:
    dt = clock.tick()
    #show fps
    fpsLabel = pyglet.text.Label("FPS: " + str(round(clock.get_fps(), 1)), font_name='Times New Roman', font_size=16, x = 50, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    window.switch_to()
    window.dispatch_events()
    root.update()
    currentPlanetLabel.config(text = "Current Planets: " + str(len(objects)))
    if not paused:
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
        currentPlanetslabel.config(text = currentPlanets)
                    
        for planet in temp_object_list:
            objects.remove(planet)

        exitLabel = pyglet.text.Label("Press ESC to exit", font_name='Times New Roman', font_size=12, x=1130, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    else:
        currentPlanets = ""
        for planet in objects:
            currentPlanets += planet.name + "\n"
        currentPlanetslabel.config(text = currentPlanets)
        
    # increase window size when more planets being displayed  
    screen_resolution = str(xwidth)+'x'+str(yheight + 15*len(objects))
    root.geometry(screen_resolution)


    # detect if a key is pressed
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
            # temporarily set symbol to not P to prevent infinite loop
            symbol = key.R

        if symbol == key.P and paused == True:
            resume()
            window.flip()
            symbol = key.R
            

         
        
     


   
        
    

   

    