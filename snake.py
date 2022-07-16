from turtle import Turtle

class Snake:
    STARTING_POSITON=[(0,0),(-20,0),(-40,0)]
    MOVE_DISTANCE=20
    UP=90
    DOWN=270
    LEFT=180
    RIGHT=0
        
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
        self.head_color()
        
    def create_snake(self):
        for pos in self.STARTING_POSITON:
            self.add_segment(pos)
          
            
    def add_segment(self,position):
        segment=Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def head_color(self):
        self.head.color("red")
    
    def reset(self):
        for seg in self.segments: #clear the old snake
            seg.reset()
        
        self.__init__() #again start
            
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_pos=self.segments[i-1].position() 
            self.segments[i].goto(new_pos)
        self.head.forward(self.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)
        
        
        
