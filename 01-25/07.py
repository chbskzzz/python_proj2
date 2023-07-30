#매일 꾸준히 하면 매일 는다

#hangman. For&While Loops, IF/ELSE, Lists, Strings, Range, Modules

#Flow chart Programming. 어떻게 만들지 생각해보기
#app.diagrams.net
#순서도는 코드를 짤 때 많이 보는 것이 좋다
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#testing code
print(f"the solution is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position : {position}\n Current Letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

