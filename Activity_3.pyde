# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario
# Modified by Gabriel Henrique

# Draws a "vehicle" on the screen

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
from Food import Food

def setup():
    global vehicle, food, counter
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2)
    food = Food(random(width), random(height), velocity)
    counter = 0

def draw():
    global counter
    background(255)
    target = PVector(food.position.x, food.position.y)
    vehicle.arrive(target)
    vehicle.update()
    vehicle.display()
    #food.update()
    food.display()

    vector = vehicle.position - food.position

    if vector.mag() < 5:
        food.update(random(width), random(height))
        counter+=1
        print('Comidas Coletadas:',counter)
    
