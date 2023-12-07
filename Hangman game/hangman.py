import random
from words import words
import string
from hangman_visual import lives_visual_dict

def get_word(words):
    word = random.choice(words)
    while " " in word or "-" in word or len(word)<6:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_word(words)
    letters_word = set(word)
    used_letters = set()
    tries = 7
    alphabet = set(string.ascii_uppercase)

    while len(letters_word) > 0 and tries > 0:
        # Get user guess and compare it with the letters in the word
        # print(word)
        user_guess = input("Guess a letter: ").upper()
        if user_guess in (
            alphabet - used_letters
        ):  # Means the letter is in the alphabet and has not been guessed before
            used_letters.add(user_guess)
            if user_guess in letters_word:
                letters_word.remove(user_guess)
                print(f"Correct. Tries left {tries}\n")
                print(lives_visual_dict[tries])

            else:
                tries -= 1
                print(f"{user_guess} is not in the word. Tries left {tries}\n")
                print(lives_visual_dict[tries])
            print(f"You have used these letters {" ".join(sorted(list(used_letters)))}")
        elif user_guess in used_letters:
            print("You have already used this letter\n")
        else:  # When the guess is not an alphabet letter
            print(f"{user_guess} is not an alphabetical letter. Guess again.\n")

        print("Current word: ", end="")
        for l in word:
            if l not in letters_word:
                print(l, end=" ")
            else:
                print("-", end=" ")
        print("")
    if tries == 0:
        print(f"You died! The word is {word}")

    if len(letters_word) == 0:
        print(f"Congratulation! Your guess {word} was correct")


if __name__ == "__main__":
    hangman()
