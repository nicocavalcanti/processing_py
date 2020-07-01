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
    global vehicle, food, counter, textY, textH, foodH
    size(640, 360)
    textH = height
    textH = 14
    foodH = 12
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2)
    food = Food(random(width-foodH), random(height-foodH-textH-1), velocity)
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
    fill(0)
    textSize(textH)
    text('Quantidade de comida coletada: '+str(counter),10,height)

    vector = vehicle.position - food.position

    if vector.mag() < 5:
        food.update(random(width-foodH), random(height-foodH-textH-1))
        counter+=1
        print('Comidas Coletadas:',counter)
    
