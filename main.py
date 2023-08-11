import time
from screenFile import ScreenC
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = ScreenC()

snk = Snake()
food = Food()
write = Scoreboard()

screen.listen_screen()
screen.push_key(snk.move_up, "Up")
screen.push_key(snk.move_down, "Down")
screen.push_key(snk.move_right, "Right")
screen.push_key(snk.move_left, "Left")

game_is_on = True
while game_is_on:
    screen.update_screen()
    time.sleep(0.1)
    snk.move()

    if snk.snake_blank[0].distance(food) < 15:
        food.refresh()
        snk.add_body()
        write.increase_score()

    if snk.xcor() > 280 or snk.xcor() < -280 or snk.ycor() > 280 or snk.ycor() < -280:
        write.game_over()
        food.game_over()
        screen.update_screen()
        game_is_on = False

    if snk.snake_blank[0].xcor() > 280 or snk.snake_blank[0].xcor() < -280 or snk.snake_blank[0].ycor() > 280 or \
            snk.snake_blank[0].ycor() < -280:
        food.game_over()
        write.game_over()
        snk.game_over()
        screen.update_screen()
        game_is_on = False

    for x in snk.snake_blank[1:]:
        if snk.snake_blank[0].distance(x) < 10:
            game_is_on = False
            write.game_over()

screen.stop_screen()
