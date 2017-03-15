# Print the list of three numbers in a array such that the sum is zero
#This can done trivially by Brute Force using O(n^3) available at : http://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
#For more optimized version Visit : http://home.acastano.com/blog/3-sum-nzp-algorithm/
#Same Repo Contions the The Full expalination and code taken from the above link.

def sum3_brute_force(a,value):
	res = []
	N = len(a)
	if N > 350: return res

    # Python ranges exclude the last term, i.e., range(0,3) = [0,1,2]
	for i in range(0, N-2):			  #for i = 0 to N-3
		for j in range(i+1, N-1):     #for j = i+1 to N-2
			for k in range (j+1, N):  #for k = j+1 to N-1
				if a[i] + a[j] + a[k] == value:
					res.append( [a[i], a[j], a[k]] )
	return res

refList = map(int,list(raw_input("Enter the List : ").split()))
refList.sort()
distval=int(raw_input("Enter Dictinct Value"))
print refList
threeSumsolution=sum3_brute_force(refList,int(distval))
print threeSumsolution
