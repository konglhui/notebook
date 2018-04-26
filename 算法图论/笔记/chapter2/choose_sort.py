def choose_sort(list):
	sorted_list = []
	for i in range(len(list)):
		a = list[0]
		f = 0
		for j in range(len(list)):
			if a < list[j]:
				a = list[j]
				f = j
		list.pop(f)
		sorted_list.append(a)
	return sorted_list
my_list = [3,2,6,3,6,7,3,5,9,11234,123,1243,1234,124,125243,5345,63,456,345,634,56,345,63,45,634,5634,56,34,56345,63,45,63,45,63,456,345,63745,67,45,67,45,674,567,]
print(choose_sort(my_list))
