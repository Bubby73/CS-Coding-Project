import pyglet # import pyglet library
key = pyglet.window.key

window = pyglet.window.Window(1200, 600) # create the window
window.set_caption("View Window") # set the window caption

running = True 

while running: # main loop  
    window.switch_to() 
    window.dispatch_events()  
    window.flip() 
    window.clear() # clear the window at the end of each frame

    @window.event()
    def on_key_press(symbol, modifiers):
        global running
        print("Key pressed")
        
        if symbol == key.ESCAPE:
            print("Escape key pressed")
            running = False
            window.close()
         