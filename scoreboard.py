from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,270)
        self.score=0
        self.write(arg=f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",align="center",font=("Arial",30))
    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(arg=f"Score: {self.score}",align="center",font=("Arial",24,"normal"))

