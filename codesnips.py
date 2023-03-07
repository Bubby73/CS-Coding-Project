import pygame
import math

# Set up the display
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the simulation variables
G = 6.67430e-11 # Gravitational constant
AU = (149.6e6 * 1000) # Astronomical unit in meters

scale = 250 / AU

class Body:
    def __init__(self, name, mass, x_pos, y_pos):
        self.name = name
        self.mass = mass
        self.x_pos = x_pos * scale + width/2 # Scale and center on screen
        self.y_pos = y_pos * scale + height/2 # Scale and center on screen
        
    def attraction(self, other):
        dx = (self.x_pos - other.x_pos)
        dy = (self.y_pos - other.y_pos)
        d_squared = dx**2 + dy**2
        
        force_magnitude = G * self.mass * other.mass / d_squared
        
        theta = math.atan2(dy,dx)
        
        force_x_component = math.cos(theta) * force_magnitude
        force_y_component