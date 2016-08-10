def main():
	fp = open('roster.txt', 'r')
	names = fp.readlines()
	count = 0
	print("The following names contain letter 'e':")
	for name in names:
	    first_name = name.split()[0]
	    if 'e' in first_name:
	        print(first_name)
	        count += 1
	print("Total number of names contain letter 'e': " + str(count))
	fp.close()

if __name__ == "__main__":
	main()
