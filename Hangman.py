import random
import turtle
import tkinter

# function um Wörter aus der Datei zu lesen
def read_words():
    with open('hangman_woerter.txt', 'r', encoding='utf-8') as file:
        words = [word.strip().lower() for word in file]
        return words

# Spielfeld "Galgen" zeichnen
def draw_playground():
    turtle.setup (500, 500)
    turtle.speed(0)
    turtle.pensize(8)
    turtle.hideturtle()
    turtle.title("Hangman")
    turtle.penup()
    turtle.goto(-100, -150)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(220)
    turtle.right(40)
    turtle.forward(50)
    turtle.left(-50)
    turtle.forward(70)
    turtle.backward(20)
    turtle.right(90)


# Hangman zeichnen (Seil, Kopf, Körper, ArmRechts, ArmLinks, BeinRechts, BeinLinks)
def draw_hangman(tries):
    if tries == 1: #Seil
        turtle.pensize(4)
        turtle.forward(50)
    elif tries == 2: #Kopf
        turtle.right(90)
        turtle.circle(20)
        turtle.penup()
        turtle.circle(20, 180)
        turtle.right(90)
        turtle.pendown()
    elif tries == 3: #Körper
        turtle.forward(100)
        turtle.backward(65)
        turtle.left(120)
    elif tries == 4: #ArmRechts
        turtle.forward(40)
        turtle.backward(40)
        turtle.left(120)
    elif tries == 5: #ArmLinks
        turtle.forward(40)
        turtle.backward(40)
        turtle.left(120)
        turtle.penup()
        turtle.forward(65)
        turtle.pendown()
    elif tries == 6: #BeinRechts
        turtle.left(30)
        turtle.forward(60)
        turtle.backward(60)
        turtle.right(60)
    elif tries == 7: #BeinLinks
        turtle.forward(60)
        turtle.backward(60)
        turtle.penup()
        turtle.goto(-100, -200)
        turtle.pendown()
        turtle.write("Game Over", font=("Arial", 16, "normal"))
        
    
        


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
    tries = 0
    

    while True:
        word = random.choice(words)
        word = replace_special_characters(word)
        guessed_letters = []
        
        
        print("*******************************************")
        print("Willkommen bei Hangman!")
        print()
        print("Errate das Wort: ",player_name)
        print("Du hast 7 Versuche, um das Wort zu erraten.")
        print("*******************************************")
        placeholder = "_" * len(word)
        print(word)
        print(placeholder)

        
        

        while tries < 7:
            guess = input("Gib einen Buchstaben ein: ").lower()

            score = 7 - tries

            if guess not in word:
                tries += 1
                print("Leider falsch. Du hast noch", score, "Versuche.")
                draw_hangman(tries)
                print()
                print(placeholder)

                continue

            if guess in guessed_letters:
                
                print("Du hast diesen Buchstaben bereits geraten. Bitte versuche es erneut.")
                print("du hast noch", score, "Versuche.")
                tries += 1
                draw_hangman(tries)
                print()
                print(placeholder)

                continue

            guessed_letters.append(guess)

            placeholder = ""
            for letter in word:
                if letter in guessed_letters:
                    placeholder += letter
                else:
                    placeholder += "_"
            print()
            print(placeholder)
            

            if placeholder == word:
                print("Herzlichen Glückwunsch! Du hast das Wort erraten.")
                print("Du hast", score, "Versuche gebraucht.")
                    
                break

        if placeholder != word:
            print("Leider hast du das Wort nicht erraten. Das richtige Wort war:", word)

        play_again = input("Möchtest du noch einmal spielen? (Ja/Nein) ").lower()
        if play_again != "ja":
        
            break

        else:
            turtle.clearscreen()
            draw_playground()
            tries = 0
            continue


draw_playground()
play_hangman()


