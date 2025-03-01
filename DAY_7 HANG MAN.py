import random
stages = [
    '''
   +-------+
   |       |
           |
           |
           |
           |
 ================
''',
    '''
   +-------+
   |       |
   O       |
           |
           |
           |
 ================
''',
    '''
   +-------+
   |       |
   O       |
   |       |
           |
           |
 ================
''',
    '''
   +-------+
   |       |
   O       |
  /|       |
           |
           |
 ================
''',
    '''
   +-------+
   |       |
   O       |
  /|\\      |
           |
           |
 ================
''',
    '''
   +-------+
   |       |
   O       |
  /|\\      |
  /        |
           |
 ================
''',
    '''
   +-------+
   |       |
   O       |
  /|\\      |
  / \\      |
           |
 ================
   GAME OVER!
'''
]

logo = '''
   _
  | |                                          
  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
  | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  | | | | (_| | | | | (_| | | | | | | (_| | | | |
  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/  '''

word_list = ['trees','galaxy','mystery','bridge','spiderman','harrypotter','star','goblin','castle','rainbow']
lives = 6
print(logo)
print("In this game you want to guess a random word!")
print("You have 6 lives!")
choosen_word = random.choice(word_list)
print(choosen_word)
placeholder = "_" * len(choosen_word)
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []

while not game_over:
    print(f"*** {lives}/6 LIVES LEFT ***")
    user_input = input("Guess a letter: ").lower()
    if user_input in correct_letters:
        print(f"You've already guessed {user_input}")
    display = ""

    for letter in choosen_word:
        if letter == user_input:
            display += letter
            correct_letters.append(user_input)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    if user_input not in choosen_word:
        lives -= 1
        print(f"You guessed wrong {user_input}, You lose a life.")
        print(stages[6 - lives])

        if lives == 0:
            game_over = True
            print(f"*** IT WAS {choosen_word}! YOU LOSE! ***")

    if "_" not in display:
        game_over = True
        print("*** YOU WIN! ***")