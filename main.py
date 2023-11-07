from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard(0, 460)
gameover = Scoreboard(0, 0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

times = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(times)
    snake.move()
    scoreboard.update_score()
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.eat()
        if times > 0.05:
            times -= 0.005

        scoreboard.increase_score()

    if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 480 or snake.head.ycor() < -480:
        game_is_on = False
        gameover.game_over()
    if len(snake.segments) > 4:
        for seg in snake.segments[2:]:
            if snake.head.distance(seg) < 10:
                game_is_on = False
                gameover.game_over()


screen.exitonclick()
