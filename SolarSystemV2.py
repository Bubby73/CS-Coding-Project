import pyglet, math, random # import libraries
from tkinter import * # import tkinter library
from pyglet import clock # import clock from pyglet
key = pyglet.window.key # import key constants



pygletWindowsize = 1200, 600
window = pyglet.window.Window(pygletWindowsize[0], pygletWindowsize[1], vsync = 0)
window.set_caption("View Window") # set the window caption
root = Tk() # create the secondary window
root.title("Control Panel") # set the secondary window caption
xwidth, yheight = 400, 200 # set the size of the secondary window
screen_resolution = str(xwidth)+'x'+str(yheight) # set the screen resolution
root.geometry(screen_resolution) # set the geometry of the secondary window
planet_image = pyglet.image.load("planet.png") # load the image
planet_image.anchor_x = planet_image.width // 2 # set the anchor to the center of the image
planet_image.anchor_y = planet_image.height // 2 
batch = pyglet.graphics.Batch() # create a batch object


numPlnaetslabel = Label(root, text="Number of planets:")
numPlnaetslider = Scale(root, from_=0, to=150, orient=HORIZONTAL, length=100)
numPlnaetslabel.grid(row=0, column=0)
numPlnaetslider.grid(row=0, column=1)
numPlnaetslider.set(0) # set the starting value of the slider to 0

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


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#new planet
def newplanet():
        planet = Planet(random.choice(planets), random.randint(0, 1200), random.randint(0, 600), random.randint(50, 100), random.randint(0, 360), random.randint(100, 500))
        return planet


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
            #planet.circle.delete() # delete the sprite
            objects.remove(planet) # remove the planet from the list 
            print("planet removed")

        
    if len(objects) < numPlnaetslider.get(): # if the number of planets is less than the number of planets on the slider
        objects.append(newplanet()) # add a new planet to the list
        print(numPlnaetslider.get())

    print("running")
        
    

    root.update() # update the secondary window at the end of each frame

    @window.event() # event handler
    def on_key_press(symbol, modifiers):
        global running
        
       
        if symbol == key.ESCAPE: # checks if the key pressed was escape
            running = False # stop the main loop
            window.close() # close the window