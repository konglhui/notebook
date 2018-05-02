def quicksort(array):
    if len(array) < 2:
        return array
    else:
    	pivot = array[0]
    	less = [i for i in array[1:] if i <= pivot]

    	greater = [i for i in array[1:] if i > pivot]
    	return quicksort(less) + [pivot] + quicksort(greater)
my_list = [3,2,6,3,6,7,3,5,9,11234,123,1243,1234,124,
			125243,5345,63,456,345,634,56,345,63,45,634,
			5634,56,34,56345,63,45,63,45,63,456,345,63745,67,45,67,45,674,567]
print(quicksort(my_list))