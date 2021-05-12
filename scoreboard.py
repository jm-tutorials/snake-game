from turtle import Turtle

ALIGNMENT = "center"
FONT1 = ("Arial", 24, "normal")
FONT2 = ("Arial", 48, "bold") 
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.write("Score: {}".format(self.score), align=ALIGNMENT, font=FONT1)
 
    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER".format(self.score), align=ALIGNMENT, font=FONT2)
    
    def addPoints(self, points=1):
        self.score += points
        self.clear()
        self.updateScoreboard()
