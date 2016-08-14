# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(nested_list):
	# turn the nested list into a new single list first
	replacement = []
	def new_list(nested_list):
		for i in range(len(nested_list)):
			if type(nested_list[i]) == int:
				replacement.append(nested_list[i])
			else:
				new_list(nested_list[i])
		return replacement
	new_list(nested_list)
	print(sum(replacement))


lst = [1, 2, [3, [4, 5]]]
nested_sum(lst)

def main():
	pass
if __name__ == "__main__":
	main()
