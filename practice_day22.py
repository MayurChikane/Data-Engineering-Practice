print("------------------------- Practice Day 22 ------------------------")

# mini project day 6

# Rock Paper Scissors App
import random
class GamesApp:
    def __init__(self):
        self.games = ["Rock-Paper-Scissors", "Guess the Number"]

    def play_rock_paper_scissors(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "You lose!"
# Example usage
games_app = GamesApp()  
result = games_app.play_rock_paper_scissors("rock")
print(result)

# Guess the Number App
class GuessTheNumber:
    def __init__(self, lower=1, upper=100):
        self.number_to_guess = random.randint(lower, upper)
        self.attempts = 0

    def make_guess(self, guess):
        self.attempts += 1
        if guess < self.number_to_guess:
            return "Too low!"
        elif guess > self.number_to_guess:
            return "Too high!"
        else:
            return f"Correct! You've guessed the number in {self.attempts} attempts."
# Example usage
guess_game = GuessTheNumber()
print(guess_game.make_guess(50))
print(guess_game.make_guess(75))

print("------------------------ End of Practice Day 22 ------------------------")        