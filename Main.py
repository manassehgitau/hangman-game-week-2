import random 

total_attempts = 7

Themes = {
    "history": [
        "marco polo",
        "Napoleon",
        "Mesopotamia",
        "Persia",
        "World War"
    ],
    "computers": [
        "Bus",
        "semiconductor",
        "keyboard",
        "vaccum tube",
        "nanometer"
    ],
     "cars": [
        "Dodge",
        "Toyota",
        "daihatsu",
        "displacement",
        "stroke"
    ]
}

HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

available_themes = ["history", "computers", "cars"]

chosen_theme = int(input('''
Enter a theme you want for the hangman game?:
                     1. history
                     2. computers
                     3. cars
                     4. quit
'''))

hangman_words = Themes[available_themes[chosen_theme - 1]]
random_word_index = random.randint(0, len(hangman_words) - 1)
random_word = hangman_words[random_word_index]
random_word_characters = list(random_word.lower())
# print(random_word_characters)

dashed_characters = []

for character in random_word_characters:
    dashed_characters.append(" _ ")

print(dashed_characters)

guessed_characters = []
current_attempts = 0

while current_attempts < total_attempts and " _ " in dashed_characters:
    user_character = input("Enter a character: ").lower()

    if user_character in guessed_characters:
        print("You already guessed that character.")
        continue

    guessed_characters.append(user_character)

    if user_character in random_word_characters:
        for idx, character in enumerate(random_word_characters):
            if character == user_character:
                dashed_characters[idx] = character
        print("Correct!")
    else:
        current_attempts += 1
        print("Wrong guess!")
    
    print(HANGMAN_PICS[current_attempts])
    print("Word: ", "".join(dashed_characters))
    print(f"Guessed so far: {guessed_characters}")
    print(f"Attempts left: {total_attempts - current_attempts}")
    print('\n')

if " _ " not in dashed_characters:
    print("Congratulations! You guessed the word:", random_word)
else:
    print("Game Over! The word was:", random_word)
