from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("high-score.txt") as file :
            self.highScore=int(file.read())
        self.goto(0,270)
        self.hideturtle()
        self.penup()
        self.color("White")
        self.speed(0)
        self.display()
        
        
    def display(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score : {self.score}  High score : {self.highScore}",True,align="center",font=('Arial', 10, 'normal'))
        
    def reset(self):
        if(self.score>self.highScore):
            self.highScore=self.score
        
        with open("high-score.txt",mode="w") as file:
            file.write(str(self.highScore))
        self.score=0
        self.display()
    
    
    def increment(self):
        self.score+=1
        self.display()
        
        
      

        


