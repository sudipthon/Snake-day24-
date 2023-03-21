import time
from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.right,key="Right")
screen.onkey(fun=snake.left,key="Left")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.head.distance(food)<13:
        food.change_food()
        snake.extend()
        score.count_score()
        
# collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        score.game_over()
        game_on=False

    #   detect collision      # 
    for i in snake.segments[1:]:
        if snake.head.distance(i)<10:
              game_on=False
              score.game_over()


 

screen.exitonclick()


 