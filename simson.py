import random
import time

def simon_says():
    colors = ['red', 'blue', 'green', 'yellow']  # Possible colors
    sequence = []  # The sequence of colors to remember
    score = 0  # Player's score

    print("Welcome to Simon Says!")
    print("Repeat the sequence of colors in order. Type 'exit' to quit.")

    while True:
        # Add a random color to the sequence
        next_color = random.choice(colors)
        sequence.append(next_color)

        # Show the sequence to the player
        print("\nSimon says:")
        for color in sequence:
            print(color, end=" ", flush=True)
            time.sleep(0.4)  # Wait before showing the next color
        print("\n" + "-" * 20)

        # Clear the screen (optional for better experience)
        print("\033c", end="")  # Works in most terminals; remove if unnecessary

        # Get player's input
        print("Your turn! Enter the sequence (space-separated):")
        user_input = input().lower().strip()

        if user_input == 'exit':
            print("Thanks for playing! Your final score is:", score)
            break

        # Check the player's input
        user_sequence = user_input.split()
        if user_sequence != sequence:
            print("\nGame Over! You entered the wrong sequence.")
            print("The correct sequence was:", " ".join(sequence))
            print("Your final score is:", score)
            break

        # Increment score if correct
        score += 1
        print(f"Good job! Current score: {score}")

# Run the game
if __name__ == "__main__":
    simon_says()
