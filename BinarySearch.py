#import sys




def binarySearch( arr , l , r , x):
	if  l <= r :
		mid = (l + r) / 2 # l + (r - l)/2 
		if  arr[mid] == x : 
			return mid
		elif  arr[mid] > x  :
			return binarySearch( arr , l , mid-1 , x )
		else: 
			return binarySearch( arr , mid + 1 ,  r , x)
	
	else :
		return -1





n = int(raw_input("Cate numere vreti sa aiba lista?\n"))

arr = []

for i in range(n):
	arr.append(int(raw_input("Introdu numarul dorit: ")))

for i in range(n):
	min_indx = i
	for j in range(i+1 , n):
		if arr[j] < arr[min_indx]:
			min_indx = j
		arr[i] , arr[min_indx] = arr[min_indx] , arr[i]






x = int(raw_input("Introdu numarul cautat: "))

result = binarySearch( arr , 0 , len(arr)-1 , x);
#print result
if( result != -1):
	print "Numarul este %d." % result;
else:
	print "Numarul nu a fost gasit."