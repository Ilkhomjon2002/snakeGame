from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import  Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
all_turtles=[]
snake = Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        break
    #Detect collision with tail
    for snake_segment in snake.snakes[1:]:
        if snake.head.distance(snake_segment)<10:
            break


scoreboard.game_over()






screen.exitonclick()