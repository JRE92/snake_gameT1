from turtle import Screen


class ScreenC:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor('black')
        self.screen.title('snake game')
        self.screen.tracer(0)

    def stop_screen(self):
        self.screen.exitonclick()

    def update_screen(self):
        self.screen.update()

    def listen_screen(self):
        self.screen.listen()

    def push_key(self, fun, key):
        self.screen.onkey(fun, key)

    # def pushing(self):
    #     return self.screen.onkey(None, "w")
