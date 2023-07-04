import random
import turtle
 

def read_words():
    with open('E:\Edvgraz\EDVGraz_Übungen\Pyhton\Wiederholung\hangman_woerter.txt', 'r', encoding='utf-8') as file:
        words = [word.strip().lower() for word in file]
    return words
# Spielfeld 
def draw_playground():
    turtle.setup (500, 500)
    turtle.title("Hangman")
    turtle.forward(100)

# function um, Umlaute zu ersetzen
def replace_special_characters(word):
    replacements = {'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss'}
    for char, replacement in replacements.items():
        word = word.replace(char, replacement)
    return word

# functionEingeben des Spielernamens
def get_player_name():
    return input("Bitte geben Sie Ihren Namen ein: ")

# playfuntion
def play_hangman():
    words = read_words()
    player_name = get_player_name()
    highscore = 0

    while True:
        word = random.choice(words)
        word = replace_special_characters(word)
        guessed_letters = []
        tries = 0

        print("Willkommen bei Hangman!")
        print("Errate das Wort:")
        placeholder = "_" * len(word)
        print(word)
        print(placeholder)

        while tries < 20:
            guess = input("Gib einen Buchstaben ein: ").lower()

            if guess in guessed_letters:
                print("Du hast diesen Buchstaben bereits geraten. Bitte versuche es erneut.")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                tries += 1

            placeholder = ""
            for letter in word:
                if letter in guessed_letters:
                    placeholder += letter
                else:
                    placeholder += "_"

            print(placeholder)

            if placeholder == word:
                print("Herzlichen Glückwunsch! Du hast das Wort erraten.")
                score = 7 - tries
                if score > highscore:
                    highscore = score
                break

        if placeholder != word:
            print("Leider hast du das Wort nicht erraten. Das richtige Wort war:", word)

        play_again = input("Möchtest du noch einmal spielen? (Ja/Nein) ").lower()
        if play_again != "ja":
        
            break

        
draw_playground()
play_hangman()

