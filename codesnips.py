import pyglet, math, random # import libraries
from tkinter import * # import tkinter library
from pyglet import clock # import clock from pyglet
key = pyglet.window.key # import key constants



window = pyglet.window.Window(1200, 600, vsync = 0) # create the window
window.set_caption("View Window") # set the window caption
root = Tk() # create the secondary window
root.title("Control Panel") # set the secondary window caption
xwidth, yheight = 400, 200 # set the size of the secondary window
screen_resolution = str(xwidth)+'x'+str(yheight) # set the screen resolution
root.geometry(screen_resolution) # set the geometry of the secondary window

running = True

class Planet():
    def __init__(self, name, x, y, radius, direction, velocity, static):
        global planetDensity
        self.name = name
        self.radius = radius / 100
        self.mass = radius 
        self.x = x 
        self.y = y 
        self.static = static
        self.direction = direction
        self.velocity = velocity 
        self.vx = math.sin(math.radians(self.direction)) * self.velocity # working out x and y velocities in relation to the direction
        self.vy = math.cos(math.radians(self.direction))* self.velocity
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=self.colour)
        self.circle.scale = self.radius
        self.circle.color = self.colour

def on_closing():
    global running 
    running = False 
root.protocol("WM_DELETE_WINDOW", on_closing) # detect when the secondary window is closed

while running: # main loop 
    clock.tick()
    #show fps
    fpsLabel = pyglet.text.Label("FPS: " + str(round(clock.get_fps(), 1)), font_name='Times New Roman', font_size=16, x = 50, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    exitLabel = pyglet.text.Label("Press ESC to exit", font_name='Times New Roman', font_size=12, x=1130, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    window.switch_to()
    window.dispatch_events() 
    window.flip()
    window.clear() # clear the window at the end of each frame

    root.update() # update the secondary window at the end of each frame

    @window.event() # event handler
    def on_key_press(symbol, modifiers):
        global running
        
       
        if symbol == key.ESCAPE: # checks if the key pressed was escape
            running = False # stop the main loop
            window.close() # close the window