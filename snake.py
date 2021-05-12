from turtle import Turtle
#import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.turtles = []
        self.createSnake()
        self.head = self.turtles[0]

    def createSnake(self):
        for i in range(3):
            self.addTail((0,i*-20))
    
    def addTail(self,position):
        t = Turtle(shape='square')
        t.color("white")
        t.penup()
        t.goto(position)
        self.turtles.append(t)

    def extend(self):
        self.addTail(self.turtles[-1].position())

    def move(self):
        for i in range(len(self.turtles)-1, 0, -1):
            t = self.turtles[i]
            nextTurtlePos = self.turtles[i-1].pos() 
            t.goto(nextTurtlePos)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

if __name__ == '__main__':
    Snake()

