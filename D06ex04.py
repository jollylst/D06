def main():
	f1 = open('roster.txt', 'r')
	names = f1.readlines()
	count = 0
	f2 = open('roster_e.txt', 'w')
	f2.write("The following names contain letter 'e':\n")
	for name in names:
	    first_name = name.split()[0]
	    if 'e' in first_name:
	        f2.write(first_name + '\n')
	        count += 1
	f2.write("Total number of names contain letter 'e': " + str(count))
	f1.close()
	f2.close()

if __name__ == "__main__":
	main()
