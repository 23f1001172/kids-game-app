#kids-game-app

import random

def display_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[0][col] != " " for row in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def display_congratulations(player):
    message = f"🎉 Congratulations, {player}! 🎉"
    print("\n" + "=" * len(message))
    print(message)
    print("=" * len(message) + "\n")

def tic_tac_toe():
    player1 = input("Enter the name of Player 1 (X): ")
    player2 = input("Enter the name of Player 2 (O): ")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = player1
    current_symbol = "X"
    
    moves = {1: (0, 0), 2: (0, 1), 3: (0, 2),
             4: (1, 0), 5: (1, 1), 6: (1, 2),
             7: (2, 0), 8: (2, 1), 9: (2, 2)}
    
    for turn in range(9):
        display_board(board)
        print(f"{current_player}'s turn ({current_symbol}). Choose a number (1-9) or type 'exit' to quit:")
        
        choice = input()
        
        if choice.lower() == 'exit':
            print("Exiting the game. Returning to main menu...")
            return

        try:
            move = int(choice)
            if move < 1 or move > 9 or board[moves[move][0]][moves[move][1]] != " ":
                print("Invalid choice! Try again.")
                continue
        except (ValueError, KeyError):
            print("Invalid input! Please enter a number from 1 to 9.")
            continue
        
        board[moves[move][0]][moves[move][1]] = current_symbol
        
        if check_winner(board):
            display_board(board)
            display_congratulations(current_player)
            return
        current_player = player2 if current_player == player1 else player1
        current_symbol = "O" if current_symbol == "X" else "X"
    
    display_board(board)
    print("It's a draw!")

def jumble_word(word):
    """Jumble the letters of a word."""
    jumbled = ''.join(random.sample(word, len(word)))
    return jumbled

def get_words_with_hints(level):
    """Return words and hints based on difficulty level."""
    words_with_hints = {
        1: {
            "cat": "A small domestic animal.",
            "dog": "A loyal pet, often called 'man's best friend'.",
            "fish": "An aquatic animal that swims.",
            "bat": "A nocturnal flying mammal.",
            "ant": "A small insect that lives in colonies.",
            "sun": "The star at the center of our solar system.",
            "hat": "An accessory worn on the head.",
            "cup": "A small, typically cylindrical container.",
            "map": "A representation of an area.",
            "toy": "An object for play."
        },
        2: {
            "bird": "An animal that can fly.",
            "tree": "A tall plant with a trunk.",
            "horse": "A large domesticated animal used for riding.",
            "table": "A piece of furniture with a flat surface.",
            "piano": "A musical instrument with keys.",
            "chair": "A piece of furniture for sitting.",
            "apple": "A round fruit that is usually red or green.",
            "orange": "A citrus fruit.",
            "giraffe": "A tall animal with a long neck.",
            "pencil": "A tool used for writing or drawing."
        },
        3: {
            "elephant": "The largest land animal.",
            "giraffe": "A tall animal with a long neck.",
            "dolphin": "A highly intelligent aquatic mammal.",
            "crocodile": "A large aquatic reptile.",
            "chocolate": "A sweet food made from roasted and ground cacao seeds.",
            "computer": "An electronic device for processing data.",
            "photograph": "An image created by capturing light.",
            "helicopter": "A type of aircraft that can take off and land vertically.",
            "pterodactyl": "A flying reptile that lived during the time of dinosaurs.",
            "submarine": "A watercraft capable of independent operation underwater."
        }
    }
    
    return words_with_hints.get(level, {})

def jumbled_words():
    level = 1
    while True:
        words_with_hints = get_words_with_hints(level)
        if not words_with_hints:
            print("No more words available at this difficulty level!")
            break

        word, hint = random.choice(list(words_with_hints.items()))
        jumbled = jumble_word(word)  # Jumble the word
        
        print(f"\nJumbled word: {jumbled}")
        
        while True:
            guess = input("Your guess (or type 'exit' to quit, or 'hint' for a hint): ")
            
            if guess.lower() == 'exit':
                print("Exiting the game. Returning to main menu...")
                return
            if guess.lower() == 'hint':
                print(f"Hint: {hint} (The first letter is '{word[0]}')")
                continue

            if guess.lower() == word:
                print("Correct! Well done!")
                increase_difficulty = input("Do you want to increase the difficulty level? (yes/no): ")
                if increase_difficulty.lower() == 'yes':
                    level += 1
                    print("Difficulty level increased!")
                break
            else:
                print(f"Sorry, the correct word was: {word}")
                return  # End the game after one guess for simplicity.

def main():
    while True:
        print("Welcome to the Kids Game App!")
        print("1. Tic Tac Toe")
        print("2. Jumbled Words")
        print("3. Exit")
        
        choice = input("Choose a game (1-3): ")
        
        if choice == "1":
            tic_tac_toe()
        elif choice == "2":
            jumbled_words()
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
