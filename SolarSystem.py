# import libraries
from tkinter import *
import pyglet
import math
import random
from pyglet import clock 

# window setup
window = pyglet.window.Window(1200, 600, vsync=0)
window.set_caption("View Window")
key = pyglet.window.key
objects = []
root = Tk()
root.title("Control Panel")
xwidth, yheight = 400, 250
screen_resolution = str(xwidth)+'x'+str(yheight)
root.geometry(screen_resolution)
planet_image = pyglet.image.load("testplanet.png")
planet_image.anchor_x = planet_image.width // 2 ##this line is new
planet_image.anchor_y = planet_image.height // 2 ## and this line also
batch = pyglet.graphics.Batch()
#vsync=0 in the window class
#G = 6.67408 * 10**-11
G = 1

# setup tkinter interface
nameLabel = Label(root, text="Object Name:")
nameLabel.grid(row=0, column=0)

nameEntry = Entry(root, width = 8, relief=FLAT)
nameEntry.grid(row=0, column=1)

varName = IntVar()
nameCheckbox = Checkbutton(root, text="Randomise Name", variable=varName)
nameCheckbox.grid(row=0, column=2)

radiusLabel = Label(root, text="Radius:")
radiusLabel.grid(row=1, column=0)

radiusEntry = Entry(root, width = 8, relief=FLAT)
radiusEntry.grid(row=1, column=1)

varRad = IntVar()
radiusCheckbox = Checkbutton(root, text="Randomise Radius", variable=varRad)
radiusCheckbox.grid(row=1, column=2)

directionLabel = Label(root, text="Direction:")
directionLabel.grid(row=2, column=0)

directionEntry = Entry(root, width = 8, relief=FLAT)
directionEntry.grid(row=2, column=1)

varDirection = IntVar()
dirCheckbox = Checkbutton(root, text="Randomise Direction", variable=varDirection)
dirCheckbox.grid(row=2, column=2)

velocityLabel = Label(root, text="Velocity:")
velocityLabel.grid(row=3, column=0)

velocityEntry = Entry(root, width = 8, relief=FLAT)
velocityEntry.grid(row=3, column=1)

varVelocity = IntVar()
velCheckbox = Checkbutton(root, text="Randomise Velocity", variable=varVelocity)
velCheckbox.grid(row=3, column=2)

xcoordLabel = Label(root, text="X Coordinate:")
xcoordLabel.grid(row=4, column=0)

xcoordEntry = Entry(root, width = 8, relief=FLAT)
xcoordEntry.grid(row=4, column=1)

varXcoord = IntVar()
xCheckbox = Checkbutton(root, text="Randomise X coord", variable=varXcoord)
xCheckbox.grid(row=4, column=2)

ycoordLabel = Label(root, text="Y Coordinate:")
ycoordLabel.grid(row=5, column=0)

ycoordEntry = Entry(root, width = 8, relief=FLAT)
ycoordEntry.grid(row=5, column=1)

varYcoord = IntVar()
yCheckbox = Checkbutton(root, text="Randomise Y coord", variable=varYcoord)
yCheckbox.grid(row=5, column=2)

varAll = IntVar()
allCheckbox = Checkbutton(root, text="Randomise All", variable=varAll)
allCheckbox.grid(row=5, column=3)

varAll.set(1)

currentPlanetLabel = Label(root, text="Current Planets:")
currentPlanetLabel.grid(row=7, column=0)
currentPlanets = "0"
currentPlanetslabel = Label(root, text = currentPlanets)
currentPlanetslabel.grid(row=8, column=0)

planetDeletelabel = Label(root, text="Delete Planet:")
planetDeletelabel.grid(row=6, column=2)
planetDeleteEntry = Entry(root, width = 15, relief=FLAT)
planetDeleteEntry.grid(row=6, column=3)

velocityMultiplierlabel = Label(root, text="Velocity Multiplier:")
velocityMultiplierlabel.grid(row=0, column=3)
velocityMultiplierslider = Scale(root, from_=-15, to=15, orient=HORIZONTAL, length=100)
velocityMultiplierslider.grid(row=1, column=3)

# set slider to 5
velocityMultiplierslider.set(1)

generateMultiplierlabel = Label(root, text="Generate Multiplier:")
generateMultiplierlabel.grid(row=2, column=3)
generateMultiplierslider = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=100)
generateMultiplierslider.grid(row=3, column=3)

staticVar = IntVar()
static = Checkbutton(root, text="Star", variable=staticVar)
static.grid(row=4, column=3)

planetDensity = 50

# new planet class
class Planet():
    def __init__(self, name, x, y, radius, direction, velocity, static):
        global planetDensity
        self.name = name
        self.radius = radius / 100
        self.mass = radius * planetDensity  
        self.x = x 
        self.y = y 
        self.static = static
        self.direction = direction
        self.velocity = velocity 
        self.vx = math.sin(math.radians(self.direction)) * self.velocity # working out x and y velocities in relation to the direction
        self.vy = math.cos(math.radians(self.direction)) * self.velocity
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circle = pyglet.sprite.Sprite(planet_image, x=self.x, y=self.y, batch=batch)
        self.circle.scale = self.radius
        self.circle.color = self.colour
        

    # updates the position of the planet
    def update(self):
        if self.static == False:
            # give planets gravity
            for planet in objects:
                    if planet != self:
                        dx = planet.x - self.x 
                        dy = planet.y - self.y
                        distance = math.sqrt(dx ** 2 + dy ** 2)
                        if (distance / 100) < planet.radius + self.radius:
                            if self.radius > planet.radius: # delete the smaller planet
                                objects.remove(planet)
                                planet.circle.delete()
                                print("Planet " + planet.name + " has been destroyed by " + self.name)
                                # add attributes
                                self.vx += planet.vx
                                self.vy += planet.vy
                                self.mass += planet.mass
                                self.radius += planet.radius / 2
                                self.circle.scale = self.radius # update circle
                                self.velocity = math.sqrt(self.vx ** 2 + self.vy ** 2)
                                self.direction = math.degrees(math.atan2(self.vx, self.vy))
                                
                                
                            elif self.radius < planet.radius:
                                objects.remove(self)
                                self.circle.delete()
                                print("Planet " + self.name + " has been destroyed by " + planet.name)
                                # add attributes
                                planet.vx += self.vx
                                planet.vy += self.vy
                                planet.mass += self.mass
                                planet.radius += self.radius / 2
                                planet.circle.scale = planet.radius # update circle
                                planet.velocity = math.sqrt(planet.vx ** 2 + planet.vy ** 2)
                                planet.direction = math.degrees(math.atan2(planet.vx, planet.vy))
                                return
                            
                            else:
                                objects.remove(self)
                                self.circle.delete()
                                objects.remove(planet)
                                planet.circle.delete()
                                print(self.name + " and " + planet.name + " have collided")
                                return
                                
                        else:
                            force = (G * self.mass * planet.mass) / (distance ** 2)
                            ax = dx / distance * force
                            ay = dy / distance * force
                            self.vx += ax / 5
                            self.vy += ay / 5 
             
                            
            # update position
            self.x += self.vx * (velocityMultiplierslider.get() / 100) 
            self.y += self.vy * (velocityMultiplierslider.get() / 100) 
            self.circle.x = self.x
            self.circle.y = self.y

class staticPlanet():
    def __init__(self, x, y, radius, static):
        self.name = "Sun"
        self.static = static
        self.radius = radius / 100
        self.mass = radius * planetDensity
        self.x = x 
        self.y = y 
        self.static = static
        self.colour = (255, 255, 0)
        self.circle = pyglet.sprite.Sprite(planet_image, x=self.x, y=self.y, batch=batch)
        self.circle.scale = self.radius
        self.circle.color = self.colour
        
    def draw(self):
        self.circle.draw()

# random planet names      
planetNamelist = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Moon"]

# new planet
def new_planet():
    if staticVar.get() == 1:
        static = True
    else:
        static = False
    for i in range(generateMultiplierslider.get()):
        if varAll.get() == 1:
            name = random.choice(planetNamelist)
            direction = random.randint(0, 360)
            velocity = random.randint(1,5)
            x = random.randint(100, 1100)
            y = random.randint(100, 500)
            if static == True:
                radius = random.randint(6, 12)
            else:
                radius = random.randint(1, 5)
            nameEntry.config(bg = "white")
            nameCheckbox.select()
            radiusEntry.config(bg = "white")
            radiusCheckbox.select()
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
            if varRad.get() == 1:
                if static == True:
                    radius = random.randint(6, 12)
                else:
                    radius = random.randint(1, 5)
            else:
                try:
                    radius = float(radiusEntry.get())
                    radiusEntry.config(bg = "white")
                except:
                    radiusEntry.config(bg = "red")
            if varDirection.get() == 1:
                direction = random.randint(0, 360)
            else:
                try:
                    direction = float(directionEntry.get())
                    directionEntry.config(bg = "white")
                except:
                    directionEntry.config(bg = "red")
            if varVelocity.get() == 1:
                velocity = random.randint(1, 5)
            else:
                try:
                    velocity = float(velocityEntry.get())
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
        if static == True:
            planet = staticPlanet(x, y, radius, static)
            direction = ""
            velocity = ""
        else:
            planet = Planet(name, x, y, radius, direction, velocity, static) # sets planet attributes
        nameEntry.delete(0, END)
        nameEntry.insert(0, name)
        radiusEntry.delete(0, END)
        radiusEntry.insert(0, radius)
        directionEntry.delete(0, END)
        directionEntry.insert(0, direction)
        velocityEntry.delete(0, END)
        velocityEntry.insert(0, velocity)
        xcoordEntry.delete(0, END)
        xcoordEntry.insert(0, x)
        ycoordEntry.delete(0, END)
        ycoordEntry.insert(0, y)
        objects.append(planet)
        

# delete planet
def deletePlanet():
    planetTodelete = planetDeleteEntry.get()
    for planet in objects:
        planetName = planet.name
        if planetName.lower() == planetTodelete.lower():
            objects.remove(planet)
            planet.circle.delete()
            print(planetName + " deleted")
            currentPlanetslabel.config(text = currentPlanets)
            break

# clear all procedure
def clearAll():
    currentPlanetslabel.config(text = currentPlanets)
    for planet in objects:
        planet.circle.delete()
        planetName = planet.name
        print(planetName + " deleted") 
    objects.clear()
    print("cleared")
        

running = True
paused = False

# pause procedure
def pause():
    global paused
    paused = True
    pauseButton.config(text="Resume")
    pauseButton.config(command=resume)
    window.flip()
    print("Paused")

# resume procedure
def resume():
    global paused
    paused = False
    pauseButton.config(text="Pause")
    pauseButton.config(command=pause)
    window.flip()
    print("Resumed")

# all buttons

# pause button
pauseButton = Button(root, text="Pause", command=pause) # pause button
pauseButton.grid(row=6, column=1)

# new planet button
generateButton = Button(root, text="Generate", command=new_planet)
generateButton.grid(row=6, column=0)

# delete planet button
planetDeletebutton = Button(root, text="Delete Planet", command=deletePlanet)
planetDeletebutton.grid(row=7, column=3)

# clear all button
clearAllbutton = Button(root, text="Clear All", command=clearAll)
clearAllbutton.grid(row=7, column=2)

pausedText = ""

 # main loop
while running:
    clock.tick()
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
            if planet.static == False:
                if planet.x > 1200 or planet.x < 0 or planet.y > 600 or planet.y < 0: # if planet of screen, delete
                    temp_object_list.append(planet)
                    

                else:
                    planet.update()
     

        batch.draw()
        # add planets to current planets label in tkinter window
        currentPlanets = ""
        for planet in objects:
            currentPlanets += planet.name + "\n"
        currentPlanetslabel.config(text = currentPlanets)
                    
        for planet in temp_object_list:
            objects.remove(planet)
            planet.circle.delete()
            print(planet.name + " left the screen and was deleted")

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





# make exe file
# pyinstaller --onefile -w SolarSystem.py    