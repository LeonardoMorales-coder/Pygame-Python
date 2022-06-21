from turtle import *
from random import randrange
import random
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
cont=0

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)


    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake)

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)

def foodMove():
    food.x = (randrange(-3, 3)*10) + food.x
    food.y = (randrange(-3, 3)*10) + food.y 
    ontimer(foodMove,2000)
    

colors = ['yellow', 'orange', 'green', 'black', 'pink']
def selected(colors):
  return random.choice(colors)

colorSnake = selected(colors)
colorFood = selected(colors)
while colorSnake == colorFood:
    colorFood = selected(colors)
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
foodMove()
done()