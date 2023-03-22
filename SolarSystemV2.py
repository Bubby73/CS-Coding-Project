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


# setup tkinter interface
nameLabel = Label(root, text="Object Name:")
nameLabel.grid(row=0, column=0)

nameEntry = Entry(root, width = 8, relief=FLAT)
nameEntry.grid(row=0, column=1)

ranName = IntVar()
nameCheckbox = Checkbutton(root, text="Randomise Name", variable=ranName)
nameCheckbox.grid(row=0, column=2)

massLabel = Label(root, text="Mass:")
massLabel.grid(row=1, column=0)

massEntry = Entry(root, width = 8, relief=FLAT)
massEntry.grid(row=1, column=1)

ranMass = IntVar()
massCheckbox = Checkbutton(root, text="Randomise Mass", variable=ranMass)
massCheckbox.grid(row=1, column=2)

directionLabel = Label(root, text="Direction:")
directionLabel.grid(row=2, column=0)

directionEntry = Entry(root, width = 8, relief=FLAT)
directionEntry.grid(row=2, column=1)

ranDirection = IntVar()
dirCheckbox = Checkbutton(root, text="Randomise Direction", variable=ranDirection)
dirCheckbox.grid(row=2, column=2)

velocityLabel = Label(root, text="Velocity:")
velocityLabel.grid(row=3, column=0)

velocityEntry = Entry(root, width = 8, relief=FLAT)
velocityEntry.grid(row=3, column=1)

ranVelocity = IntVar()
velCheckbox = Checkbutton(root, text="Randomise Velocity", variable=ranVelocity)
velCheckbox.grid(row=3, column=2)

xcoordLabel = Label(root, text="X Coordinate:")
xcoordLabel.grid(row=4, column=0)

xcoordEntry = Entry(root, width = 8, relief=FLAT)
xcoordEntry.grid(row=4, column=1)

ranXcoord = IntVar()
xCheckbox = Checkbutton(root, text="Randomise X coord", variable=ranXcoord)
xCheckbox.grid(row=4, column=2)

ycoordLabel = Label(root, text="Y Coordinate:")
ycoordLabel.grid(row=5, column=0)

ycoordEntry = Entry(root, width = 8, relief=FLAT)
ycoordEntry.grid(row=5, column=1)

ranYcoord = IntVar()
yCheckbox = Checkbutton(root, text="Randomise Y coord", variable=ranYcoord)
yCheckbox.grid(row=5, column=2)

ranAll = IntVar()
allCheckbox = Checkbutton(root, text="Randomise All", variable=ranAll)
allCheckbox.grid(row=5, column=3)

ranAll.set(1)

generateMultiplierlabel = Label(root, text="Generate Multiplier:") 
generateMultiplierlabel.grid(row=0, column=3)
generateMultiplierslider = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=100) 
generateMultiplierslider.grid(row=1, column=3)



class Planet():
    def __init__(self, name, x, y, mass, direction, velocity):
        self.name = name
        self.radius = mass / 1000
        self.mass = 4/3 * math.pi * mass**3 * 5.51 * 10**12 # working out the mass of the planet
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
        self.x += self.vx * dt 
        self.y += self.vy * dt 
        self.circle.x = self.x 
        self.circle.y = self.y  


planetNames = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#new planet
def newplanet():
        for i in range(generateMultiplierslider.get()):
            if ranAll.get() == 1: # if the randomise all checkbox is checked
                name = random.choice(planetNames)
                direction = random.randint(0, 360)
                velocity = random.randint(100,500)
                x = random.randint(100, 1100)
                y = random.randint(100, 500)
                mass = random.randint(50, 100)
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

            else:
                if ranName.get() == 1:
                    name = random.choice(planetNames)
                else:
                    if nameEntry.get() == "":
                        nameEntry.config(bg = "red")
                    else:
                        name = nameEntry.get()
                        nameEntry.config(bg = "white")
                if ranMass.get() == 1:
                    mass = random.randint(50, 100)
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

# new planet button
generateButton = Button(root, text="Generate", command=newplanet)
generateButton.grid(row=6, column=0)

objects = [] # list of objects

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

    temp_object_list = [] # reset the temporary object list at the end of each frame
    for planet in objects: # for each planet in the list
        if planet.x > pygletWindowsize[0] or planet.x < 0 or planet.y > pygletWindowsize[1] or planet.y < 0: # if the planet goes off the screen
            temp_object_list.append(planet)

        else:
             planet.update()

    batch.draw() # draw the batch

    for planet in temp_object_list:
            planet.circle.delete() # delete the sprite
            objects.remove(planet) # remove the planet from the list 
            print("planet removed")
        
    

    root.update() # update the secondary window at the end of each frame

    @window.event() # event handler
    def on_key_press(symbol, modifiers):
        global running
        
       
        if symbol == key.ESCAPE: # checks if the key pressed was escape
            running = False # stop the main loop
            window.close() # close the window