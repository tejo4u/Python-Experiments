# Print the list of three numbers in a array such that the sum is zero
#This can done trivially by Brute Force using O(n^3) available in the same repo with algo of distinct number
#This particular Implemetaion is taken from : 

def binary_search(a, key):
	""" searches an array 'a' for a value in lg(n) time """
	N = len(a)
	lo = 0
	hi = N-1
	while (lo <= hi):
		mid = lo + (hi-lo)/2
		if key < a[mid]:
			hi = mid - 1
		elif key > a[mid]:
			lo = mid +1
		else:
			return mid
	return None


def sum3_with_sort(a):
	res = []
	N = len(a)
	if N > 3500: return res
	a.sort()	                      # Quick sort or Merge sort, O(N ln N)

    # Python ranges exclude the last term, i.e., range(0,3) = [0,1,2]
	for i in range(0, N-2):			  #for i = 0 to N-3
		for j in range(i+1, N-1):     #for j = i+1 to N-2
			val = -(a[i] + a[j])
			if a[i] < a[j] < val and binary_search( a, val ):
				res.append( [a[i], a[j], val] )
	return res

refList = map(int,list(raw_input("Enter List values : ").split()))
outlist=sum3_with_sort(refList)
print outlist, "is the soultion List."
