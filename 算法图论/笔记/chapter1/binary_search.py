def binary_search(list,item):
	low = 0
	high = len(list) - 1

	while low<= high:
		median = (low + high)//2
		guess = list[median]
		if item == guess:
			return median
		elif item > guess:
			low = median+1
		elif item < guess:
			high = median-1
	return None

my_list = [1,2,3,4,5,6,7,8,9]

print(binary_search(my_list,10))
