from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        # self.shape('square')
        self.score = 0
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", False, 'center', ("Roboto", 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color('red')
        self.write(f"GAME OVER", False, 'center', ("Roboto", 24, 'normal'))


