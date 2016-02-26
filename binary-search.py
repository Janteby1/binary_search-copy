# word doc binay search
def read_words (document):
	# read in the article file
	with open(document) as doc:
		words = []
		# loop through the article line by line
		for line in doc :
			words.append(line.strip('\n'))
		return words


def binary_search_word(value):
	my_list = read_words ("wordlist.txt")
	print (my_list)
	my_dict = {}
	
	# create dictionary in one line, switch the position of key and value 
	my_dict = dict((value,key) for key,value in enumerate(my_list))
	print (my_dict)

	new_list = my_list

	while len(new_list)>=0:
		middle = int(len(new_list)/2)

		if (len(new_list))>0:
			if value > new_list[middle]:
				# cut in half to the right  
				new_list = new_list[middle+1:]
			elif value < new_list[middle]:
				# cut in half to the left 
				new_list = new_list[:middle]
			elif value == new_list[middle]:
				print ("You found the value", new_list[middle], "in your array")
				# now you have the value just need to look up its key in the dict
				value_idex = my_dict[new_list[middle]]
				print ("Your index position of that value is ", value_idex)
				return True
		else:
			print ("The value is not in the array")
			return False


##sample dataset
print (binary_search_word("hello"))
print (" ")





# regulare binary search 
def binary_search(my_list, value):
	sorted = check_sort(my_list)
	my_dict = {}
	counter = 0
	
	# create dictionary in one line, switch the position of key and value 
	my_dict = dict((value,key) for key,value in enumerate(my_list))
	# print (my_dict)

	# for item in my_list:
	# 	my_dict[item] = counter
	# 	counter += 1

	if sorted == True:
		new_list = my_list

		while len(new_list)>=0:
			middle = int(len(new_list)/2)

			if (len(new_list))>0:
				if value > new_list[middle]:
					# cut in half to the right  
					new_list = new_list[middle+1:]
				elif value < new_list[middle]:
					# cut in half to the left 
					new_list = new_list[:middle]
				elif value == new_list[middle]:
					print ("You found the value", new_list[middle], "in your array")
					# now you have the value just need to look up its key in the dict
					value_idex = my_dict[new_list[middle]]
					print ("Your index position of that value is ", value_idex)
					return True
			else:
				print ("The value is not in the array")
				return False


# no point in binary search bc this check is linear
def check_sort (my_list):
	changed = True
	while changed:
		for i in range (0, len(my_list)-1):
			if my_list[i]>my_list[i+1]:
				changed = False
		return changed

##sample dataset
arr = [1,3,9,11,23,44,66,88,102,142,188,192,239,382,492,1120,1900,2500,4392,5854,6543,8292,9999,29122]
print (binary_search(arr, 88))



'''
The whole point of a binary search is that, since the data is already sorted, you can quickly locate the information you want.

Take the phone book, which is sorted by last name.

How do you find someone in the phone book? You open it up to a page which you assume will be close to what you want, and then start flipping pages.

But you don't flip one page each time, if you missed by a lot, you flip a bunch of pages, and then finally start flipping one at a time, until finally you start looking at a single page.

This is what binary search does. Since the data is sorted, it knows it can skip a lot and do another look, and it'll focus in on the information you want.

A binary search does 1 comparison for every doubled number of items. So a 1024 element collection would require around 10 comparisons, at the most, to find your information, or at least figure out that it's not there.

If you, before running the actual binary search, does a full run-through to check if the data is sorted, you might as well just do a scan for the information. A full run-through + the binary search will require N + log2 N operations, so for 1024 elements, it would require around 1034 comparisons, whereas a simple scan for the information will on average require half, which is 512.

So if you can't guarantee that the data is sorted, you should not use binary search, as it will be outperformed by a simple scan.
'''