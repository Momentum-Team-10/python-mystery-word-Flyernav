#telling file you want words to be selected randomly

import random
words = []
underscores = []
guesses = []
end_game = False

with open('words.txt') as file:
    strings = file.readlines()

for string in strings:
    words.append(string)

random_word = random.choice(words)
random_word = random_word.replace("\n", "")

word_length = range(len(random_word))
for num in word_length:
    underscores.append('_')
underscores = "".join(underscores)

print(underscores)
user_input = input('Take a Chance... ').lower()

while user_input != 'Quit' and end_game == False:
    
    for index in range(len(random_word)):
        if random_word[index] == user_input:
            underscores = underscores[0:index] + user_input + underscores[index+1:]
    print(underscores)
    user_input = input('Take another Guess...')
        
    if user_input == 'Quit':
        end_game = True            
        