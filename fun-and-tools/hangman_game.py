# def hangman():
#     target_word = "secret"
#     num_tries = 3
#     current_word = "_"*len(target_word)
#     print('Guess which word is it :)')
#     guessed_letters = []
#     while True:
#         if num_tries <= 0:
#             break
#         print("Word:", current_word)
#         if current_word == target_word:
#             print("Congratulations you've guessed the word!!")
#             break
#         guess = input("Enter a letter: ")
#         if guess in target_word:
#             guessed_letters.append(guess)
#             temp_word = ""
#             for v in target_word:
#                 if v in guessed_letters:
#                     temp_word += v
#                 else:
#                     temp_word += "_"
                    
#             if current_word == "_"*len(target_word):
#                 current_word = temp_word
#             else:
#                 res = ""
#                 for i in range(len(target_word)):
#                     if current_word[i] == "_":
#                         res += temp_word[i]
#                     else:
#                         res += current_word[i]
#                 current_word = res
#         else:
#             num_tries -= 1    
#             print(f"Sorry, the letter is not present ({num_tries} tries left)")

                                      
# def main():
#     hangman()        


# if __name__ == "__main__":
#     main()

###############################################

from random import choice

def run_game():
    word: str = choice(["secret", "dolphin", "guitar"])

    username: str = input("What is you name? >> ")
    print(f'Welcome to hangman {username}!')

    # Setup
    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0
        
        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end="")
            else:
                print('_', end="")
                blanks += 1

        print() # Adds a blank line

        if blanks == 0:
            print("You got it!")
            break
        try:
            guess: str = input('Enter a letter: ').strip()

            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Please enter a single letter!")
        except ValueError as e:
            print(e)
            tries -= 1
            print(f"({tries} tries remaining)")
            continue

        if guess in guessed:
            print(f"You already used: '{guess}'. Please try with another letter!")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong... ({tries} tries remaining)")

            if tries == 0:
                print('No more tries remaining... You lose.')
                break

if __name__ == "__main__":
    run_game()
