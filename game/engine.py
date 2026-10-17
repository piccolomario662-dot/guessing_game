import random

class GuessingGame:
    """A class representing the simple text-based guessing game logic."""

    def __init__(self, min_val: int = 1, max_val: int = 100) -> None:
        """
        Initializes the game state.

        :param min_val: The minimum possible secret number.
        :param max_val: The maximum possible secret number.
        """
        self.min_val = min_val
        self.max_val = max_val
        self._secret_number = random.randint(self.min_val, self.max_val)
        self._attempts = 0
        self._is_game_over = False

    def guess(self, number: int) -> str:
        """
        Processes a player's guess and returns feedback.

        :param number: The number guessed by the player.
        :return: A string indicating if the guess was too high, too low, or correct.
        """
        if self._is_game_over:
            return "Game is over. Start a new game."

        self._attempts += 1

        if number < self._secret_number:
            return "Too low!"
        elif number > self._secret_number:
            return "Too high!"
        else:
            self._is_game_over = True
            return f"Correct! You guessed it in {self._attempts} attempts."

    def is_over(self) -> bool:
        """
        Checks if the game has been won.

        :return: True if correct number was guessed, False otherwise.
        """
        return self._is_game_over

    def reset(self) -> None:
        """Resets the game state with a new secret number."""
        self._secret_number = random.randint(self.min_val, self.max_val)
        self._attempts = 0
        self._is_game_over = False