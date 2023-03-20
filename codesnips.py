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


numPlnaetslabel = Label(root, text="Number of planets:")
numPlnaetslider = Scale(root, from_=0, to=150, orient=HORIZONTAL, length=100)
numPlnaetslabel.grid(row=0, column=0)
numPlnaetslider.grid(row=0, column=1)
numPlnaetslider.set(0) # set the starting value of the slider to 0

class Planet():
    def __init__(self, name, x, y, mass, direction, velocity):
        self.name = name
        self.radius = mass 
        self.mass = 4/3 * math.pi * self.radius**3 * 5.51 * 10**12 # working out the mass of the planet
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
        planet = Planet(random.choice(planets), random.randint(0, 1200), random.randint(0, 600), random.randint(50, 100), random.randint(0, 360), random.randint(1, 5))
        return planet


objects = [] # list of objects

def on_closing():
    global running 
    running = False 
root.protocol("WM_DELETE_WINDOW", on_closing) # detect when the secondary window is closed

running = True
while running: # main loop 
    clock.tick()
    #show fps
    fpsLabel = pyglet.text.Label("FPS: " + str(round(clock.get_fps(), 1)), font_name='Times New Roman', font_size=16, x = 50, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    exitLabel = pyglet.text.Label("Press ESC to exit", font_name='Times New Roman', font_size=12, x=1130, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    window.switch_to()
    window.dispatch_events() 
    window.flip()
    window.clear() # clear the window at the end of each frame

    temp_object_list = [] # reset the temporary object list at the end of each frame
    for planet in objects: # for each planet in the list
        planet.update()
        if planet.x > pygletWindowsize[0] or planet.x < 0 or planet.y > pygletWindowsize[1] or planet.y < 0: # if the planet goes off the screen
            temp_object_list.append(planet)

    for planet in temp_object_list:
            objects.remove(planet) # remove the planet from the list 
            print("planet removed")
        
    if len(objects) < numPlnaetslider.get(): # if the number of planets is less than the number of planets on the slider
        objects.append(newplanet()) # add a new planet to the list
        print(numPlnaetslider.get())

    

    root.update() # update the secondary window at the end of each frame

    @window.event() # event handler
    def on_key_press(symbol, modifiers):
        global running
        
       
        if symbol == key.ESCAPE: # checks if the key pressed was escape
            running = False # stop the main loop
            window.close() # close the window