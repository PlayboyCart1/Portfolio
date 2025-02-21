#basic hangman game
import random

print("""=== HANGMAN 2025 ===

Welcome to HANGMAN 2025.

Guess the word before the man is drawn.

Have fun!
      """)

words = [ #100 words to be randomly selected
    "apple", "banana", "cherry", "dragonfruit", "elephant", "flamingo", "grapefruit", "hamburger", "internet", "jungle",
    "kangaroo", "lightning", "mountain", "notebook", "octopus", "penguin", "quicksand", "rainstorm", "sunflower", "tornado",
    "umbrella", "volcano", "watermelon", "xylophone", "yellow", "zeppelin", "airplane", "backpack", "caterpillar", "dolphin",
    "emerald", "firetruck", "giraffe", "helicopter", "igloo", "jellyfish", "koala", "lighthouse", "moonlight", "nightmare",
    "ocean", "parachute", "question", "reptile", "spaceship", "telescope", "underwater", "vampire", "whirlpool", "xenon",
    "yesterday", "zookeeper", "avalanche", "butterfly", "chocolate", "dandelion", "earphone", "fountain", "galaxy", "horizon",
    "illusion", "jigsaw", "kayak", "landscape", "marathon", "nectarine", "ostrich", "pyramid", "quarantine", "rhinoceros",
    "strawberry", "trampoline", "universe", "voyager", "wildflower", "xenophobia", "yacht", "zephyr", "alphabet", "blueberry",
    "cactus", "dungeon", "envelope", "fireplace", "gondola", "harpoon", "icicle", "jackpot", "kaleidoscope", "labyrinth",
    "meadow", "nebula", "origami", "puzzle", "quasar", "rainforest", "symphony", "turquoise", "utopia", "vortex"
    ]

hangmanpics = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

hangman_word = words[random.randint(0,99)]

hangman_word_letters = list(hangman_word)

print("Guess a letter: ")

print_ans = [] #create empty list

for letter in hangman_word_letters: #add to empty list with appropriate amount of '_' for # of characters
    print_ans.append("_")

print(" ")
print(print_ans)

x = 0 #variable to count hang man stick figure number

while True:
    print(hangmanpics[x])

    if x == 6:
        print(" ")
        print("Unfortunately, you lost 😂")
        print(" ")
        print("The word was: " + str(hangman_word))
        break

    else:
        letter_guess = input(str("Guess a letter (type 'SOLVE' to solve): ")) #ask user to make a guess / ask to solve
        
        if letter_guess == "1":
            break
        if letter_guess.upper() == "SOLVE": #if user chooses to solve
            word_guess = str(input("Please guess the word: "))
            if word_guess.upper() == hangman_word.upper(): #correct solve
                print(" ")
                print("Congratulations, you got it 🎉")
                break
            else: #incorrect solve
                print(" ")
                print("Unfortunately, that isn't it 👎")
                x += 1

        else: #if user chooses to guess
            for i in range(len(hangman_word)):
                if hangman_word_letters[i] == letter_guess: #tell user if their guess was a letter or not
                    isletter = str(letter_guess) + " is a letter."
                    break
                else:
                    isletter = str(letter_guess) + " is not a letter."
            if isletter == str(letter_guess) + " is not a letter.":
                x += 1
            print(" ")
            print(isletter) #print if guess was letter or not - put here so it doesn't print multiple times
            print(" ")
            for i in range(len(hangman_word_letters)):
                if hangman_word_letters[i] == letter_guess:
                    print_ans[i] = letter_guess #replace '_' with correctly guessed letters in relevant places
                else:
                    pass
            print(print_ans) #print list with correctly guessed letters

        underscore = 0
        for i in range(len(print_ans)):
            if print_ans[i] == "_":
                underscore += 1
        if underscore == 0:
            print(" ")
            print("Congratulations, you win 🎉")
            break

