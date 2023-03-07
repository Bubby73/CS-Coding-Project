import pyglet # import pyglet library
from pyglet import clock # import clock from pyglet
key = pyglet.window.key # import key constants


window = pyglet.window.Window(1200, 600, vsync = 0) # create the window
window.set_caption("View Window") # set the window caption


running = True


while running: # main loop 
    clock.tick()
    #show fps
    fpsLabel = pyglet.text.Label("FPS: " + str(round(clock.get_fps(), 1)), font_name='Times New Roman', font_size=16, x = 50, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    exitLabel = pyglet.text.Label("Press ESC to exit or P to pause", font_name='Times New Roman', font_size=12, x=1100, y=590, anchor_x='center', anchor_y='center', color=(255,255,255, 255)).draw()
    window.switch_to()
    window.dispatch_events() 
    window.flip()
    window.clear() # clear the window at the end of each frame


    @window.event() # event handler
    def on_key_press(symbol, modifiers):
        global running
       
        if symbol == key.ESCAPE: # checks if the key pressed was escape
            running = False # stop the main loop
            window.close() # close the window