from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = []
        self.init_snake()

    def add_length(self, pos):
        """Adds a segment to the snake at pos=(x,y)"""
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(pos)
        self.snake.append(new_turtle)

    def init_snake(self):
        """Create the initial 3 segments snake"""
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for start in starting_positions:
            self.add_length(start)

    def snake_up(self):
        """Change direction of the head of the snake to face up if possible"""
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def snake_down(self):
        """Change direction of the head of the snake to face down if possible"""
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def snake_right(self):
        """Change direction of the head of the snake to face right if possible"""
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def snake_left(self):
        """Change direction of the head of the snake to face left if possible"""
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
