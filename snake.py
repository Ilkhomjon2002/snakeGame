from turtle import Turtle
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
POSITIONS=[(0,0),(-20,0),(20,0)]
class Snake:
    def __init__(self):
        self.snakes=[]
        self.create_game()
        self.head=self.snakes[0]

    def create_game(self):
        for position in POSITIONS:
            self.add_extend(position)


    def move(self):
        for t in range(len(self.snakes) - 1, 0, -1):
            new_y = self.snakes[t - 1].ycor()
            new_x = self.snakes[t - 1].xcor()
            self.snakes[t].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def add_extend(self,position):
        new_snake=Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        new_p=self.snakes[-1].position()
        self.add_extend(position=new_p)

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




