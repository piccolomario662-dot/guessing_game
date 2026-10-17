from game.engine import GuessingGame

def main() -> None:
    """
    Primary entry point for the guessing game application.
    Runs the main input loop to interact with the player.
    """
    print("--- Welcome to the Guessing Game! ---")
    game = GuessingGame(min_val=1, max_val=100)
    print(f"I am thinking of a number between {game.min_val} and {game.max_val}.")

    while not game.is_over():
        try:
            user_input = input("Enter your guess: ")
            
            # Allow quit command
            if user_input.lower() in ('quit', 'exit'):
                print("Thanks for playing!")
                break
                
            guess = int(user_input)
            result = game.guess(guess)
            print(result)
            
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'quit'.")
        
    if game.is_over():
        print("Game over!")

if __name__ == "__main__":
    main()