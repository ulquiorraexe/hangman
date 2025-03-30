import random
hangman_memo = '''_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/'''

five_left = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''

four_left = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''

three_left = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''

two_left = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''

one_left = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''

zero_left = '''  
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

words = [
  "apple", "banana", "grape", "orange", "cherry",
  "lemon", "tomato", "carrot", "potato", "onion",
  "guitar", "piano", "violin", "trumpet", "flute",
  "butterfly", "elephant", "giraffe", "dolphin", "penguin",
  "computer", "keyboard", "monitor", "printer", "charger",
  "bicycle", "airplane", "helicopter", "submarine", "train",
  "jungle", "desert", "island", "volcano", "glacier",
  "puzzle", "shadow", "whisper", "gadget", "lantern",
  "candle", "pirate", "monster", "skeleton", "zombie",
  "wizard", "rainbow", "thunder", "whistle", "mystery"
]

game_is_on = True

def remaining_lives(life):
    if life == 5:
        print(five_left)
    elif life == 4:
        print(four_left)
    elif life == 3:
        print(three_left)
    elif life == 2:
        print(two_left)
    elif life == 1:
        print(one_left)
    elif life == 0:
        print(zero_left)

while game_is_on:
    ind = random.randrange(50)
    word = words[ind]
    hidden = list(len(word)*'_')
    lives = 6
    print(hangman_memo)
    while "_" in hidden:
        guess = input("Guess a letter: ").lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden[i] = guess
        else:
            lives -= 1
            remaining_lives(lives)
            print("Wrong guess!")
            if lives == 0:
                break


        print(" ".join(hidden))

        if "_" not in hidden:
            print("Congratulations! You guessed the word!")
            game_is_on = False
            break

