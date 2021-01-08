from turtle import Screen, Turtle
import time


class Game:
    def __init__(self):
        """Init of the Game class, creating screen and empty snake"""
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Krall's Snake Game")
        self.screen.tracer(0)
        self.snake = []

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

    def run(self):
        """Main method of the game"""
        self.init_snake()
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.1)
            for seg in range(len(self.snake)-1, 0, -1):
                self.snake[seg].goto(self.snake[seg-1].xcor(), self.snake[seg-1].ycor())
            self.snake[0].forward(10)
        self.screen.exitonclick()


if __name__ == '__main__':
    game = Game()
    game.run()
