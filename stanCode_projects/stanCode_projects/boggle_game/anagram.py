"""
File: anagram.py
Name: Ruby
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
STUDENT_INF = []


def main():
    """
    User can input any vocabulary, this program will searching the dictionary and print the amount of permutations and
     all permutations.
    """
    print("Welcome to stanCode 'Anagram Generator' (or -1 to quit) ")
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break

        start = time.time()

        read_dictionary()
        ans_lst = []
        find_anagrams(word, ans_lst)
        print(f'{len(ans_lst)} anagrams: {ans_lst}')

        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            STUDENT_INF.append(line.strip())



def find_anagrams(s,ans_lst):
    """
    :param s: the vocabulary which user want to find its permutation
    :return: the amount of permutation which found in the dictionary.
    """
    print('Searching...')
    find_anagram_helper(s, ans_lst, '', [])


def find_anagram_helper(word, ans_lst, current_str, used_index):
    # Base case
    if len(current_str) == len(word):
        if current_str in STUDENT_INF and current_str not in ans_lst:
            ans_lst.append(current_str)
            print('Found: ' + current_str)
            print('Searching...')

    # Recursive case
    else:
        for i in range(len(word)):
            if i not in used_index:
                # Choose
                current_str += word[i]
                used_index.append(i)

                # Explore
                if has_prefix(current_str):
                    find_anagram_helper(word, ans_lst, current_str, used_index)

                # Un-choose
                current_str = current_str[:-1]
                used_index.pop()


def has_prefix(sub_s):
    """
    :param sub_s: all permutation of the vocabulary
    :return: every permutation which was find in the dictionary
    """
    for d in STUDENT_INF:
        if d.startswith(sub_s):
            return True
    return False





if __name__ == '__main__':
    main()
