#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

def has_no_e(word):
	words = list(word)
	for i in words:
		if i == 'e' or i == 'E':
			return False
	return True


def print_no_e(file_name):
	fp = open(file_name, 'r')
	words = fp.readlines()
	word_count = 0
	count = 0
	print("The following words have no 'e':")
	for item in words:
		word = item.strip()
		word_count += 1
		if ('e' not in word) and ('E' not in word):
			print(word)
			count += 1
	print("Percentage of the words in the list that have no 'e': " + "{:.2%}".format(count/word_count))
	fp.close()	
# Body


##############################################################################
def main():
    print(has_no_e('world'))
    print_no_e('words.txt') # Call your function(s) here.

if __name__ == '__main__':
    main()
