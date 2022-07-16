from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkeypress(key="Up",fun=snake.up)
screen.onkeypress(key="Down",fun=snake.down)
screen.onkeypress(key="Left",fun=snake.left)
screen.onkeypress(key="Right",fun=snake.right)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    
    if snake.head.distance(food)<15:
        snake.extend()
        score.increment()
        food.refresh()
    
    #detect collision - wall
    if abs(snake.head.xcor())>290 or abs(snake.head.ycor())>290:
        score.reset()
        snake.reset()
        
    #detect collision - snake segment
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset()
            snake.reset()
            
        
screen.exitonclick()