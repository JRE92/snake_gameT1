from turtle import Turtle
import random


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.pos = 20
        self.color = ['blue', 'red', 'green']
        self.chose_color = 0
        self.snake_blank = []
        self.last_body = 0
        self.last_body_x = 0
        self.last_body_y = 0
        self.create_snake()

    def create_snake(self):
        for x in range(0, 3):
            self.snake_blank.append(Turtle('square'))
            self.snake_blank[x].penup()
            if x == 0:
                self.snake_blank[x].color('white')
                self.snake_blank[x].setposition(0, 0)
            elif x == 1:
                self.snake_blank[x].color('red')
                self.snake_blank[x].setposition(-20, 0)
            elif x == 2:
                self.snake_blank[x].color('blue')
                self.snake_blank[x].setposition(20, 0)

    def add_body(self):
        self.refresh()
        self.snake_blank.append(Turtle('square'))
        self.snake_blank[self.last_body].penup()
        self.snake_blank[self.last_body].color(self.color[self.chose_color])
        self.snake_blank[self.last_body].setposition(self.last_body_x, self.last_body_y)

    def refresh(self):
        self.last_body = len(self.snake_blank)
        self.last_body_x = self.snake_blank[self.last_body - 1].xcor()
        self.last_body_y = self.snake_blank[self.last_body - 1].ycor()
        self.chose_color = random.randint(0, 2)

    def move(self):
        for x in range(len(self.snake_blank) - 1, 0, -1):
            self.snake_blank[x].goto(self.snake_blank[x - 1].xcor(), self.snake_blank[x - 1].ycor())
        self.snake_blank[0].forward(20)

    def move_up(self):
        if self.snake_blank[0].heading() != 270:
            self.snake_blank[0].setheading(90)

    def move_down(self):
        if self.snake_blank[0].heading() != 90:
            self.snake_blank[0].setheading(270)

    def move_left(self):
        if self.snake_blank[0].heading() != 0:
            self.snake_blank[0].setheading(180)

    def move_right(self):
        if self.snake_blank[0].heading() != 180:
            self.snake_blank[0].setheading(0)

    def game_over(self):
        for x in range(len(self.snake_blank)):
            self.snake_blank[x].ht()
