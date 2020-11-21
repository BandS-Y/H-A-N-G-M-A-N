import random
from string import ascii_lowercase

word_list = ('python', 'java', 'kotlin', 'javascript')
sicret_word = random.choice(word_list)
# print(sicret_word)
logs = set()
tries = 7
play = ""

print("H A N G M A N")
while play != "exit":
    play = input('Type "play" to play the game, "exit" to quit:')
    if play == "play":
        print_word_list = ["-" for _ in range(len(sicret_word))]
        print_word_str = "".join(print_word_list)
        print(tries)
        while tries >= 0:
            if "-" not in print_word_list:
                break
            print("")
            print("".join(print_word_list))
            letter = input("Input a letter:")
            if len(letter) != 1:
                print("You should input a single letter")
            elif letter not in ascii_lowercase:
                print("Please enter a lowercase English letter")
            elif letter in logs and letter not in print_word_list:
                print("You've already guessed this letter")
            elif letter in print_word_list:
                print("You've already guessed this letter")
                # tries -= 1
            elif letter in sicret_word:
                print_word_list = [
                    sicret_word[let] if sicret_word[let] == letter else "-" if print_word_list[let] == "-" else
                    sicret_word[let]
                    for let in range(len(sicret_word))]
            elif letter not in logs:
                print("That letter doesn't appear in the word")
                tries -= 1
            logs.add(letter)
        if tries < 0:
            print("""You lost!""")
        if tries >= 0:
            print()
            print("".join(print_word_list))
            print("""You guessed the word!\nYou survived!""")
        play = ""
        logs = set()
        tries = 7
