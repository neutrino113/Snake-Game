from turtle import Screen, Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360

class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()  # So that all the turtle moves correctly without leaving a line behind when they move
        new_segment.goto(position)
        self.segments.append(new_segment)  # segment is list of turtle objects

    def extend(self):
        self.add_segment(self.segments[-1].position())  # adding new turtle object at the position of last turtle object

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # So that the last segment moves to the position of second last and second last at the position of third last and so on, so that when we move our first segment left, other segments also follows the left path
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # As in snake game, snake can not directly move to up when the snake's head is moving down and same for other cases
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(360)



