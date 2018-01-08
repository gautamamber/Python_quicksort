from random import randint

def quicksort(l):   
	pivot = len(l)/2   # take pivot is middle
	less ,equal, greater = [],[],[]
	for i in xrange(len(l)):
		if l[i] < l[pivot]:
			less.append(l[i])
		elif l[i] >l[pivot]:
			greater.append(l[i])
		else:
			equal.append(l[i])
	if len(less) > 1:
		less = quicksort(less)
	if len(greater) >1 :
		greater = quicksort(greater)
	return less + equal + greater



