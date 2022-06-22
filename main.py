from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # by doing this nothing's gonna happen till we update the screen

# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto((-20,0))
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto((-40,0))

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # to read the buttons we click to move the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # till now the tracer was set to off, when we update the screen, it shows all the three turtle getting updated together instead of turtles getting updated individually
    time.sleep(0.1)  # to delay the screen by 0.1 seconds to get better visuals
    snake.move()

    if snake.head.distance(food) < 15:  # To detect collision
        food.refresh()
        snake.extend()  # to increase the size
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.gameover()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if segment != snake.head and snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()




















screen.exitonclick()