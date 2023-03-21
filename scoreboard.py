from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        with open("data.txt") as data:
            self.highs_score=int(data.read())
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.score=0
        self.update_score()

    def update_score(self):
            self.write(arg=f"Score:{self.score}", align="center",font=("Arial","8","normal"))
    def game_over(self):

        self.goto(0,0)
        self.write("Gameover",align="center",font=("Arial","50","normal"))
        
      
        
       
        if self.score>self.highs_score:
            self.highs_score=self.score
            with open("data.txt","w") as data:
                data.write(f"{self.highs_score}")
            
  
        
        self.goto(0,200)
        self.write(f"Your Score:{self.score}",align="center",font=("Arial","30","normal"))
        
        self.goto(0,100)
        with open("data.txt","r") as data:
            high=data.read()
            self.write(f"Highest score:{high}",align="center",font=("Arial","30","normal"))
            
  
        
        
    def count_score(self):
        self.score+=1
        self.clear()
        self.update_score ()      
        