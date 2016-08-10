#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(word, forbidden_letters):
    """ return True if word NOT forbidden"""
    for char in word:
        if char in forbidden_letters:
            return False
    return True


def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    fp = open('words.txt', 'r')
    words = fp.readlines()
    count = 0
    forbidden_letters = input('Please enter the forbidden letters: \n')
    for item in words:
        word = item.strip()
        if avoids(word, forbidden_letters):
            count += 1
    print("Count of words not forbidden by 'input': " + str(count))
    fp.close()

def forbidden_param(forbidden_str):
    """ return count of words NOT forbidden by param"""
    fp = open('words.txt', 'r')
    words = fp.readlines()
    count = 0
    for item in words:
        word = item.strip()
        if avoids(word, forbidden_str):
            count += 1
    print("Count of words not forbidden by 'input': " + str(count))


def find_five():
    pass #cannot figure it out yet...

##############################################################################
def main():
    print(avoids('hello', "abcf"))
    forbidden_prompt()
    forbidden_param('aeiou')
    # Your final submission should only call five_five

if __name__ == '__main__':
    main()
