from tkinter import LEFT
from turtle import Turtle, Screen

screen = Screen()

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.a = 0
        self.create_snake()
        self.head=self.segments[0]
        self.head.color("blue")

    def create_snake(self):
        for i in range(3):
            self.add_segments()

    def add_segments(self): 

        snake = Turtle(shape="circle")
        snake.penup()
        snake.color("white")
        snake.goto(0, 0)
        self.a -= 20
        self.segments.append(snake)

    def extend(self):
  
        self.add_segments()
        
   
    def move(self):
            for seg in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(new_x, new_y)
            self.head.fd(20)
            
    def up(self):
        if self.head.heading()!=DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
           self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)