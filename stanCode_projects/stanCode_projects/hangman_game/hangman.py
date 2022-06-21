"""
File: hangman.py
Name: Ruby
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Every candidate has seven chances to try. If candidate input more than two alphabet or wrong format,
    it's need to input again. Chance would not be effect neither incorrect format nor repeat answer.

    """
    new_random_word = random_word()
    ans = ""
    for i in range(len(new_random_word)):
        ans += '_'
    print('THe word looks like'+ans)
    print('You have '+ str(N_TURNS)+' wrong guesses left.')
    guess = input('Your guess: ')
    step = 0
    history = ''
    while step != N_TURNS:
        if guess.isalpha():
            if len(guess) == 1:
                new_guess = guess.upper()
                # record entry history
                if new_guess in new_random_word:
                    if new_guess in history:
                        print('The word looks like' + ans)
                        print('You have ' + str(N_TURNS-step) + ' wrong guesses left.')
                    else:
                        for j in range(len(new_random_word)):
                            alphabet = new_random_word[j]
                            if alphabet == new_guess:
                                ch1 = ans[:j]
                                ch2 = ans[j+1:]
                                ans = ch1 + alphabet + ch2
                                print('You are correct!\nThe word looks like' + ans)
                                print('You have ' + str(N_TURNS - step) + ' wrong guesses left.')
                                if ans == new_random_word:
                                    print('you are correct!\nYou win!!\nThe word was: ' + ans)
                                    return
                                else:
                                    history = new_guess + guess
                                    guess = input('Your guess: ')
                else:
                    step += 1
                    print('There is no '+new_guess+"\'s in the world.")
                    if step == N_TURNS:
                        print('You are completely hung :(\nThe word was:'+new_random_word)
                        return
                    else:
                        print('The word looks like' +ans)
                        print('You have ' + str(N_TURNS-step) + ' wrong guesses left.')
                    history = new_guess + guess
                    guess = input('Your guess: ')
            else:
                print('Illegal format')
                guess = input('Your guess')
        else:
            print('Illegal format')
            guess = input('Your guess: ')





















def random_word():
    """

    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
