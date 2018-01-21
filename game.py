import random

def hangman(stage):
    if stage == 0:
        print(" _________    ")
        print("|         |   ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")

    elif stage == 1:
        print(" _________    ")
        print("|         |   ")
        print("|         0   ")
        print("|             ")
        print("|             ")
        print("|             ")

    elif stage == 2:
        print(" _________    ")
        print("|         |   ")
        print("|         0   ")
        print("|         |   ")
        print("|             ")
        print("|             ")

    elif stage == 3:
        print(" _________    ")
        print("|         |   ")
        print("|         0   ")
        print("|        /|   ")
        print("|             ")
        print("|             ")

    elif stage == 4:
        print(" _________    ")
        print("|         |   ")
        print("|         0   ")
        print("|        /|\  ")
        print("|             ")
        print("|             ")

    elif stage == 5:
        print(" _________    ")
        print("|         |   ")
        print("|         0   ")
        print("|        /|\  ")
        print("|        /    ")
        print("|             ")

    elif stage == 6:
        print(" _________    ")
        print("|         |   ")
        print("|         0   ")
        print("|        /|\  ")
        print("|        / \  ")
        print("|             ")
        print("You failed!")
    else:
        print("stage error")

def game():
    # initializing a new game
    word = random.choice(['apple', 'orange', 'lime', 'banana', 'foobar'])
    
    found_letters = []
    stage = 0
    solved = False
    hangman(stage)
    
    print()
    print()
    print("_ " * len(word))
    
    while solved == False:
        try:
            if "_" not in update_word:
                print("Congratulations, you solved the word!")
                solved = True
                continue
        except UnboundLocalError:
            pass # this will be the case everytime a new game starts
        
        letter = input("Guess a letter/word: ")
        letter = letter.strip().lower() #normalize inputs
        
        if letter in found_letters:
            print("You've already found this letter. Please choose another one.")
            continue

        if letter == word:
            print("Congratulations, you solved the word!")
            solved = True
            continue

        if word.count(letter) == 1:
            print("The letter", letter, "is in the word 1 time")
            found_letters.append(letter)
            found_letters = list(set(found_letters)) # just to be sure the list is unique

            update_word = []

            for l in word:
                if l not in found_letters:
                    update_word.append("_")
                else:
                    update_word.append(l)

            print(" ".join(update_word))

        elif word.count(letter) > 1:
            print("The letter", letter, "is in the word", word.count(letter), "times")
            found_letters.append(letter)
            found_letters = list(set(found_letters)) # just to be sure the list is unique

            update_word = []

            for l in word:
                if l not in found_letters:
                    update_word.append("_")
                else:
                    update_word.append(l)

            print(" ".join(update_word))

        else:
            print("Sorry,",letter, "is not in the word")
            try:
                print(" ".join(update_word))
            except UnboundLocalError:
                print("_ " * len(word))

            stage += 1

            if stage == 6:
                hangman(stage)
                break #to end the game
            else:
                hangman(stage)


if __name__ == '__main__':
    game()
