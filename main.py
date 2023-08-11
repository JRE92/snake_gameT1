import time
from screenFile import ScreenC
# from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = ScreenC()
# screen = Screen()
# screen.setup(600, 600)
# screen.bgcolor('black')
# screen.title('snake game')
# screen.tracer(0)

snk = Snake()
food = Food()
write = Scoreboard()
# print(snk.head[0].distance(food))
# def rtrt():
#     print('puto')

# screen.listen()
# screen.onkey(snk.move_up, "Up")
# screen.onkey(snk.move_down, "Down")
# screen.onkey(snk.move_right, "Right")
# screen.onkey(snk.move_left, "Left")

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

    if snk.head[0].distance(food) < 15:
        food.refresh()
        snk.extend()
        write.increase_score()

    if snk.head[0].xcor() > 280 or snk.head[0].xcor() < -280 or snk.head[0].ycor() > 280 or snk.head[0].ycor() < -280:
        food.game_over()
        write.game_over()
        snk.game_over()
        screen.update_screen()
        game_is_on =  False
# check
    # for x in snk.head:
    #     # print(snk.snk[x], x)
    #     if x == snk.head[x]:
    #         pass
    #     if snk.head[x].distance(snk.snk[x]) < 15:
    #         game_is_on = False
    #         write.game_over()


screen.stop_screen()
