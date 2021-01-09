from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        """Init of the Game class, creating screen and empty snake"""
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Krall's Snake Game")
        self.screen.tracer(0)

    def control(self):
        """Key listener for arrow keys"""
        self.screen.listen()
        self.screen.onkey(snake.snake_up, "Up")
        self.screen.onkey(snake.snake_down, "Down")
        self.screen.onkey(snake.snake_right, "Right")
        self.screen.onkey(snake.snake_left, "Left")

    def run(self):
        """Main method of the game"""

        self.control()
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.05)
            for seg in range(len(snake.snake) - 1, 0, -1):
                snake.snake[seg].goto(snake.snake[seg - 1].xcor(), snake.snake[seg - 1].ycor())
            snake.snake[0].forward(10)
            if snake.snake[0].distance(food) < 15:
                food.refresh()
                snake.add_length({snake.snake[-1].xcor(), snake.snake[-1].ycor()})
                scoreboard.increase_score()
            if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -300 or \
                    snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
                game_is_on = False
            for i in range(1, len(snake.snake) - 1):
                if snake.snake[0].distance(snake.snake[i]) < 9:
                    game_is_on = False
        scoreboard.game_over()
        self.screen.exitonclick()


if __name__ == '__main__':
    game = Game()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    game.run()
