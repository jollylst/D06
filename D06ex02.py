import random


def main():
	fp = open('random_num.txt', 'w')
	for num in range(10):
	    fp.write(str(random.random())+'\n')
	fp.close()

if __name__ == "__main__":
	main()
