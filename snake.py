from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20


class Snake:

    def __init__(self):
        self.snakes = []
        for i in POSITION:
            self.add_segment(i)
        self.head = self.snakes[0]

    def add_segment(self, i):
        snake = Turtle(shape="square")
        snake.penup()
        snake.goto(i)
        snake.color("white")
        self.snakes.append(snake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):

        for j in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[j - 1].xcor()
            new_y = self.snakes[j - 1].ycor()
            self.snakes[j].goto(x=new_x, y=new_y)

        self.snakes[0].forward(MOVE_SPEED)

    def up(self):
        if self.snakes[0].heading() == 270:
            pass
        else:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() == 90:
            pass
        else:
            self.snakes[0].setheading(270)

    def right(self):
        if self.snakes[0].heading() == 180:
            pass
        else:
            self.snakes[0].setheading(0)

    def left(self):
        if self.snakes[0].heading() == 0:
            pass
        else:
            self.snakes[0].setheading(180)
