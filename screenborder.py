from turtle import Turtle

class ScreenBorder(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")








    def draw_screen(self):
        self.penup()
        self.goto(-285, 285)
        self.pendown()
        self.width(5)

        for side in range(4):
            self.forward(570)
            self.right(90)
