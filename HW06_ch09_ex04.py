#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: coffee coca cola
#       2: call alchohol
#       3: oh aloe cool
##############################################################################
# Imports

# Body
def uses_only(word, string):
	for char in word:
		if char not in string:
			return False
	return True


def find_using_only():
	fp = open('words.txt', 'r')
	words = fp.readlines()
	uses_only_count = 0
	uses_only_string = input("The acceptable letters: \n")
	for item in words:
		word = item.strip()
		if uses_only(word, uses_only_string):
			print(word)
			uses_only_count += 1
	print(uses_only_count)
	fp.close()

##############################################################################
def main():
    print(uses_only('examination', 'acefhlo')) # Call your function(s) here.
    find_using_only()
if __name__ == '__main__':
    main()
