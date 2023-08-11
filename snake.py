from turtle import Turtle


class Snake:

    def __init__(self):

        self.snk = []
        self.pos = 0
        self.head = self.snk
        self.create_snake()

    def create_snake(self):
        for x in range(0, 3):
            self.add_segment(x)

        # print(self.head[0].distance(10))

    def add_segment(self, x):
        self.snk.append(Turtle('square'))
        self.snk[x].color('white')
        self.snk[x].penup()
        self.snk[x].setposition(self.pos, 0)
        self.pos += 20

    def extend(self):
        # print(len(self.snk))
        self.add_segment(len(self.snk))

    def move(self):

        for x in range(len(self.snk) - 1, 0, -1):
            self.snk[x].goto(self.snk[x - 1].xcor(), self.snk[x - 1].ycor())
        self.head[0].forward(20)

    def move_up(self):
        if self.head[0].heading() != 270:
            self.head[0].setheading(90)

    def move_down(self):
        if self.head[0].heading() != 90:
            self.snk[0].setheading(270)

    def move_left(self):
        if self.head[0].heading() != 0:
            self.snk[0].setheading(180)

    def move_right(self):
        if self.head[0].heading() != 180:
            self.snk[0].setheading(0)

    def game_over(self):

        for x in range(len(self.snk)):
            self.snk[x].ht()
