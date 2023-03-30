import pyglet, math, random # import libraries
from tkinter import * # import tkinter library
from pyglet import clock # import clock from pyglet
key = pyglet.window.key # import key constants


pWindowx, pWindowy = 1200, 600
pygletWindowsize = pWindowx, pWindowy
window = pyglet.window.Window(pygletWindowsize[0], pygletWindowsize[1], vsync = 0)
window.set_caption("View Window") # set the window caption
root = Tk() # create the secondary window
root.title("Control Panel") # set the secondary window caption
xwidth, yheight = 400, 250 # set the size of the secondary window
screen_resolution = str(xwidth)+'x'+str(yheight) # set the screen resolution
root.geometry(screen_resolution) # set the geometry of the secondary window
planet_image = pyglet.image.load("planet.png") # load the image
planet_image.anchor_x = planet_image.width // 2 # set the anchor to the center of the image
planet_image.anchor_y = planet_image.height // 2 
batch = pyglet.graphics.Batch() # create a batch object
G = 6.67408 * 10**-11 # gravitational constant

objects = [] # list of objects
planetNames = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] # list of planet names

# setup tkinter interface

nameLabel = Label(root, text="Object Name:") # name label
nameLabel.grid(row=0, column=0)

nameEntry = Entry(root, width = 8, relief=FLAT) # name entry
nameEntry.grid(row=0, column=1)

ranName = IntVar()
nameCheckbox = Checkbutton(root, text="Randomise Name", variable=ranName) # name checkbox
nameCheckbox.grid(row=0, column=2)

massLabel = Label(root, text="Mass:") # mass label
massLabel.grid(row=1, column=0)

massEntry = Entry(root, width = 8, relief=FLAT) # mass entry
massEntry.grid(row=1, column=1)

ranMass = IntVar()
massCheckbox = Checkbutton(root, text="Randomise Mass", variable=ranMass) # mass checkbox
massCheckbox.grid(row=1, column=2)

directionLabel = Label(root, text="Direction:") # direction label
directionLabel.grid(row=2, column=0)

directionEntry = Entry(root, width = 8, relief=FLAT) # direction entry
directionEntry.grid(row=2, column=1)

ranDirection = IntVar()
dirCheckbox = Checkbutton(root, text="Randomise Direction", variable=ranDirection) # direction checkbox
dirCheckbox.grid(row=2, column=2)

velocityLabel = Label(root, text="Velocity:") # velocity label
velocityLabel.grid(row=3, column=0)

velocityEntry = Entry(root, width = 8, relief=FLAT) # velocity entry
velocityEntry.grid(row=3, column=1)

ranVelocity = IntVar()
velCheckbox = Checkbutton(root, text="Randomise Velocity", variable=ranVelocity) # velocity checkbox
velCheckbox.grid(row=3, column=2)

xcoordLabel = Label(root, text="X Coordinate:") # x coordinate label
xcoordLabel.grid(row=4, column=0)

xcoordEntry = Entry(root, width = 8, relief=FLAT) # x coordinate entry
xcoordEntry.grid(row=4, column=1)

ranXcoord = IntVar()
xCheckbox = Checkbutton(root, text="Randomise X coord", variable=ranXcoord) # x coordinate checkbox
xCheckbox.grid(row=4, column=2)

ycoordLabel = Label(root, text="Y Coordinate:") # y coordinate label
ycoordLabel.grid(row=5, column=0)

ycoordEntry = Entry(root, width = 8, relief=FLAT) # y coordinate entry
ycoordEntry.grid(row=5, column=1)

ranYcoord = IntVar()
yCheckbox = Checkbutton(root, text="Randomise Y coord", variable=ranYcoord) # y coordinate checkbox
yCheckbox.grid(row=5, column=2)

ranAll = IntVar()
allCheckbox = Checkbutton(root, text="Randomise All", variable=ranAll) # randomise all checkbox
allCheckbox.grid(row=5, column=3)

ranAll.set(1)

generateMultiplierlabel = Label(root, text="Generate Multiplier:") # generate multiplier label
generateMultiplierlabel.grid(row=2, column=3)
generateMultiplierslider = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=100)  # generate multiplier slider
generateMultiplierslider.grid(row=3, column=3)

planetDeletelabel = Label(root, text="Delete Planet:") # delete planet label
planetDeletelabel.grid(row=6, column=2)
planetDeleteEntry = Entry(root, width = 15, relief=FLAT) # delete planet entry
planetDeleteEntry.grid(row=6, column=3)

currentPlanetLabel = Label(root, text="Current Planets:") # current planets label
currentPlanetLabel.grid(row=7, column=0)
currentPlanets = "" # current planets variable
currentPlanetslabel = Label(root, text = currentPlanets) 
currentPlanetslabel.grid(row=8, column=0)

velocityMultiplierlabel = Label(root, text="Velocity Multiplier:") # velocity multiplier label
velocityMultiplierlabel.grid(row=0, column=3)
velocityMultiplierslider = Scale(root, from_=0, to=25, orient=HORIZONTAL, length=100)
velocityMultiplierslider.grid(row=1, column=3)

# set slider to 1 by default
velocityMultiplierslider.set(1)



class Planet():
    def __init__(self, name, x, y, mass, direction, velocity):
        self.name = name
        self.radius = mass / 2000
        self.mass = 4/3 * math.pi * mass**3 * 5.51 * 10**12 * 10000# working out the mass of the planet
        self.x = x
        self.y = y
        self.direction = direction
        self.velocity = velocity
        self.vx = math.sin(math.radians(self.direction)) * self.velocity
        self.vy = math.cos(math.radians(self.direction)) * self.velocity
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circle = pyglet.sprite.Sprite(planet_image, x=self.x, y=self.y, batch=batch) # create the sprite
        self.circle.scale = self.radius # set the radius of the sprite
        self.circle.color = self.colour # set the colour of the sprite
    
    def update(self):
        for planet in objects: # for every planet in the objects list
            if planet != self: # if the planet is not the same as the current planet
                dx = planet.x - self.x
                dy = planet.y - self.y
                distance = math.sqrt(dx**2 + dy**2) * 1000 # distance formula
                if distance < planet.radius + self.radius: # if the planets collide
                    distance = planet.radius + self.radius # set the distance to the radius of the planets
                    # collision algorithm
                F = G * self.mass * planet.mass / distance**2 # working out the force of gravity
                self.vx += F * dx / distance / self.mass 
                self.vy += F * dy / distance / self.mass 

        self.x += self.vx * dt * velocityMultiplierslider.get()
        self.y += self.vy * dt * velocityMultiplierslider.get()  
        self.circle.x = self.x 
        self.circle.y = self.y  


# functions/procedures

#new planet
def newplanet():
        for i in range(generateMultiplierslider.get()):
            if ranAll.get() == 1: # if the randomise all checkbox is checked
                # reset the colours of the entry boxes
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

            
            if ranName.get() == 1:
                name = random.choice(planetNames) # get a random name from the list
                # if name already in use increase number on the end by one
                def checkName(name):
                    for planet in objects:
                        if planet.name == name: # if name already in use
                            if name[-1].isdigit(): # if last character is a number
                                name = name[:-1] + str(int(name[-1]) + 1) # increase number on end by one
                            else:
                                name += "1" # if last character is not a number add a 1 to the end
                            checkName(name) # check again
                    return name # return name
                name = checkName(name)

            else:
                if nameEntry.get() == "": # if no name entered
                    nameEntry.config(bg = "red")
                    return
            
                else:
                    name = nameEntry.get()
                    for planet in objects: 
                        if planet.name == name: 
                            nameEntry.config(bg = "red")
                            return
                                
                    nameEntry.config(bg = "white")
            if ranMass.get() == 1:
                mass = random.randint(20, 70)
            else:
                try:
                    mass = float(massEntry.get())
                    massEntry.config(bg = "white")
                except:
                    massEntry.config(bg = "red")
            if ranDirection.get() == 1:
                direction = random.randint(0, 360)
            else:
                try:
                    direction = float(directionEntry.get())
                    directionEntry.config(bg = "white")
                    if direction > 360 or direction < 360: 
                        direction = direction % 360 # direction mod 360
                        directionEntry.delete(0, END)
                        directionEntry.insert(0, direction) # insert new direction into entry box
                except:
                    directionEntry.config(bg = "red")
            if ranVelocity.get() == 1:
                velocity = random.randint(1, 5)
            else:
                try:
                    velocity = float(velocityEntry.get())
                    velocityEntry.config(bg = "white")
                except:
                    velocityEntry.config(bg = "red")
            if ranXcoord.get() == 1:
                x = random.randint(100, 1100)
            else:
                try:
                    x = int(xcoordEntry.get())
                    if x <= pWindowx and x >= 0:
                        xcoordEntry.config(bg = "white")
                    else:
                        xcoordEntry.config(bg = "red")
                except:
                    xcoordEntry.config(bg = "red")
            if ranYcoord.get() == 1:
                y = random.randint(100, 500)
            else:
                try:
                    y = int(ycoordEntry.get())
                    if y <= pWindowy and y >= 0:
                        ycoordEntry.config(bg = "white")
                    else:
                        ycoordEntry.config(bg = "red")
                except:
                    ycoordEntry.config(bg = "red")
            
            planet = Planet(name, x, y, mass, direction, velocity) # sets planet attributes
            # update the entry boxes with the new values
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
            objects.append(planet) # add the planet to the list of objects
            updatePlanetlist()

# clear all procedure
def clearAll():
    for planet in objects: # cycle through all the planets
        planet.circle.delete() # delete the sprite
        planetName = planet.name # get the name of the planet
        print(planetName + " deleted") 
    objects.clear() # clear the list of objects
    updatePlanetlist()
    print("Cleared")

# delete planet procedure
def deletePlanet():
    planetTodelete = planetDeleteEntry.get() # get the name of the planet to delete
    planetDeleteEntry.delete(0, END) # clear the entry box
    for planet in objects: # cycle through all the planets
        planetName = planet.name # get the name of the planet
        if planetName.lower() == planetTodelete.lower(): # if the name of the planet matches the name of the planet to delete
            objects.remove(planet) # remove the planet from the list of objects
            planet.circle.delete() # delete the sprite
            print(planetName + " deleted")
            updatePlanetlist()
            break # stop the loop

def updatePlanetlist():
    # add planets to current planets label in tkinter window
    currentPlanets = ""
    for planet in objects: 
        currentPlanets += planet.name + "\n"
    currentPlanetslabel.config(text = currentPlanets)

    # increase window size when more planets being displayed  
    screen_resolution = str(xwidth)+'x'+str(yheight + 15*len(objects)) 
    root.geometry(screen_resolution)

# new planet button
generateButton = Button(root, text="Generate", command=newplanet)
generateButton.grid(row=6, column=0)

# clear all button
clearAllbutton = Button(root, text="Clear All", command=clearAll)
clearAllbutton.grid(row=7, column=2)

# delete planet button
planetDeletebutton = Button(root, text="Delete Planet", command=deletePlanet)
planetDeletebutton.grid(row=7, column=3)



def on_closing():
    global running 
    running = False 
root.protocol("WM_DELETE_WINDOW", on_closing) # detect when the secondary window is closed


running = True
while running: # main loop 
    #show fps
    dt = clock.tick() # get the time since the last frame
    fpsLabel = pyglet.text.Label("FPS: " + str(round(clock.get_fps(), 1)), font_name='Times New Roman', font_size=16, x = 50, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    exitLabel = pyglet.text.Label("Press ESC to exit", font_name='Times New Roman', font_size=12, x=1130, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255), batch=batch)
    window.switch_to()
    window.dispatch_events() 
    window.flip()
    window.clear() # clear the window at the end of each frame
    currentPlanetLabel.config(text = "Current Planets: " + str(len(objects)))


    temp_object_list = [] # reset the temporary object list at the end of each frame
    for planet in objects: # for each planet in the list
        if planet.x > pygletWindowsize[0] or planet.x < 0 or planet.y > pygletWindowsize[1] or planet.y < 0: # if the planet goes off the screen
            temp_object_list.append(planet)

        else:
             planet.update()

    batch.draw() # draw the batch

    if len(temp_object_list) > 0: # if there are any planets to remove
        for planet in temp_object_list:
                planet.circle.delete() # delete the sprite
                objects.remove(planet) # remove the planet from the list 
                updatePlanetlist()
                print("planet removed")
        

    root.update() # update the secondary window at the end of each frame

    @window.event() # event handler
    def on_key_press(symbol, modifiers):
        global running
        
       
        if symbol == key.ESCAPE: # checks if the key pressed was escape
            running = False # stop the main loop
            window.close() # close the window