"""
20120913 - Andres Castano
Please, mail questions, errors, comments to andres@acastano.com
This is a Python 2.7 file
To execute:
Python <filename>

20120915: minor changes:
			- finding z with binary search (O(ln N) instead of N)
			- using sets instead of hash tables to test membership
			- changed the condition for fast rejection
20120913: minor changes:
			- nzp with iterators (0.5x speedup over no-iteration version)
			- timings averaged over multiple runs
				- 100 times for arrays with less than 500 elements
				- 20 times for arrays with more than 500 elements
20120909: original version

"""


import time, random, math


" ======== routines used to estimate running time of algorithm ========"
def mean(data):
    return sum(data)/len(data)


def linear_regression(x, y):
	"y = mx+b"
	x_bar = mean(x)
	y_bar = mean(y)
	num, den = 0.0, 0.0
	for i in range(len(x)):
		xt = x[i] - x_bar
		num += xt*(y[i] - y_bar)
		den += xt*xt
	m = num/den
	b = y_bar - m*x_bar
	return m, b


def running_time(input_size, time):
	"""estimates the constant and order of the running time of an algorithm
	as T(N) = a * N ^ b

	input_size is the list with various input sizes, e.g., [100, 200, 400, 800]
	time is a list with the corresponding running times
	"""
	lg_input_size = [math.log(i,2) for i in input_size]
	lg_time = [math.log(i,2) for i in time]
	m, b = linear_regression(lg_input_size, lg_time)
	#print m, b 
	a = pow(2,b)
	b = m
	return a, b  # running time = a*N^b


" ========  put answer in a standard form ========== "

def sum3_standard_answer(a):
	""" each triple of the answer is sorted
	e.g.,
	if a = [[3,4,-7], [0, -10, 10]]
	then, after the func is called, we have:
	a = [[-7, 3, 4], [-10, 0, 10]]
	"""
	for triple in a:
		triple.sort()

def sum3_results_are_equal(a,b):
	s1 = a[:]
	s2 = b[:]
	if len(s1) != len(s2):
		return False

	sum3_standard_answer(s1)
	sum3_standard_answer(s2)
	for e1 in s1:
		found = False
		for e2 in s2:
			if e1 == e2:
				found = True
				break
		if not found:
			return False
	return True





" =========== 3-sum algorithms  =============  "

" == brute force == "

def sum3_brute_force(a):
	res = []
	N = len(a)
	if N > 350: return res

    # Python ranges exclude the last term, i.e., range(0,3) = [0,1,2]
	for i in range(0, N-2):			  #for i = 0 to N-3
		for j in range(i+1, N-1):     #for j = i+1 to N-2
			for k in range (j+1, N):  #for k = j+1 to N-1
				if a[i] + a[j] + a[k] == 0:
					res.append( [a[i], a[j], a[k]] )
	return res


" == 3-sum with binary sort == "


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


" == 3-sum with hash table.. quadratic in average == "

def sum3_with_hash_table(a):
	res = []
	N = len(a)
	d = {}
	for i in range(N):
		d[a[i]] = 1
	a.sort()	# sort in place

    # Python ranges exclude the last term, i.e., range(0,3) = [0,1,2]
	for i in range(0, N-2):			  #for i = 0 to N-3
		for j in range(i+1, N-1):     #for j = i+1 to N-2
			val = -(a[i] + a[j])
			if a[i] < a[j] < val and val in d:
				res.append( [a[i], a[j], val] )
	return res


" == 3-sum reported in http://en.wikipedia.org/wiki/3SUM.. quadratic in worse case == "

def sum3_quad(S):
	res = []
	n = len(S)
	S.sort()
	for i in xrange(0,n-2):  # for i=0 to n-3 do:
		a = S[i]
		k = i+1
		l = n-1
		while k<l:
			b = S[k]
			c = S[l]
			if a+b+c == 0:
				res.append([a,b,c])
				l = l-1
				k = k+1
			elif a+b+c > 0:
				l = l-1
			else:
				k = k+1
	return res


""" the next two algorithms are nzp implemented without and with iterators.
Many languages do not have iterators (e.g., C) but many do.
This is a minor change that increases the speed about 50 percent but since
it falls in the realm of optimization, not algorithms, we will not delved into it"""

def signum(x):
    return (x > 0) - (x < 0)

def binary_search_2(a, key):
	""" searches an array 'a' for a value in lg(n) time
	returns whether it found the item and the last array pos used"""
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
			return True, mid
	return False, mid

def sum3_nzp_no_iterators(a):
	" nzp without iterators (easy to port to, say, C)"
	res = []
	a.sort()

	" fast rejection "
	if ( a[0]*a[-1] == 0 ) or ( signum(a[0]) == signum(a[-1]) ):
		return res

	d = {}
	for i in xrange(N):
		d[a[i]] = 1

	zero_found, i = binary_search_2(a, 0)
	if zero_found:	n, p = i-1, i+1
	elif a[i] < 0:	n, p = i, i+1
	else:			n, p = i-1, i

	"reverse negatives"
	for i in xrange((n+1)/2):
		a[i], a[n-i] = a[n-i], a[i]

	"first deal with zero case"
	if zero_found:
		num_neg = n+1
		num_pos = len(a) - num_neg
		if zero_found:
			num_pos -= 1

		if num_neg <= num_pos:
			l, h = 0, n+1
		else:
			l, h = p, N
		for i in xrange(l, h):
			if -a[i] in d:
				res.append([a[i], 0, -a[i]])

	"now assume |A| > |B| > |C| and A > 0.. then B < 0 and C < 0"
	for i in xrange(p,N):
		A = a[i]
		bound = A/2.
		for j in xrange(0, n+1):
			C = a[j]
			if -C < bound:
				B = -(A + C)
				if B in d:
					res.append([A, B, C])
			else:
				break

	"now assume that |A| > |B| > |C| and A < 0.. then B > 0 and C > 0"
	for i in xrange(0, n+1):
		A = a[i]
		bound = -A/2.
		for j in xrange(p,N):
			C = a[j]
			if C < bound:
				B = -(A + C)
				if B in d:
					res.append([A, B, C])
			else:
				break

	return res



def sum3_nzp(a):
	""" nzp version with iterators (e.g., Python, Java, etc.)
	this version is about 0.5x faster than the one without iterators """
	res = []
	a.sort()

	" fast rejection "
	if ( a[0]*a[-1] == 0 ) or ( signum(a[0]) == signum(a[-1]) ):
		return res

	" using set as hash table"
	#d = {elem for elem in a}
	d =set(a)

	zero_found, i = binary_search_2(a, 0)
	if zero_found:	n, p = i-1, i+1
	elif a[i] < 0:	n, p = i, i+1
	else:			n, p = i-1, i

	neg = a[:n+1]
	neg.reverse()		#"reverse negatives"
	pos = a[p:]

	"first deal with zero case"
	if zero_found:
		if len(neg)	<= len(pos):	v = neg
		else:						v = pos
		for A in v:
			if -A in d:
				res.append([A, 0, -A])

	"now assume |A| > |B| > |C| and A > 0.. then B < 0 and C < 0"
	for A in pos:
		bound = A/2.
		for C in neg:
			if -C < bound:
				if -(A+C) in d:
					res.append([A, -(A+C), C])
			else:
				break

	"now assume that |A| > |B| > |C| and A < 0.. then B > 0 and C > 0"
	for A in neg:
		bound = -A/2.
		for C in pos:
			if C < bound:
				if -(A+C) in d:
					res.append([A, -(A+C), C])
			else:
				break

	return res



""" =============  testing routines =========  """


def test_verification_routines():
	a = [[3,4,-7], [0, -10, 10]]
	b = [[10,-10,0],[-7,4,3]]
	c = [[11,-11,0],[-7,4,3]]
	assert sum3_results_are_equal(a,b) == True
	assert sum3_results_are_equal(a,c) == False


algor = ["brute f.", "w/ binsort", "w/ hash t.", "quadrat.", "quad. nzp"]
fn = [ sum3_brute_force, sum3_with_sort, sum3_with_hash_table, sum3_quad, sum3_nzp]

def test(N, PRINT=False):
	""" make a list of N distint integers """
	s = set()
	while len(s) != N:
		s.add(random.randint(-2*N, 2*N))
	d = list(s)
	

	if PRINT:
		print "d=",d

	""" vector that holds timings """
	run_time = []

	""" use results of brute force as benchmark as long as N <= 640 """
	data = d[:]

	start = time.clock()
	res = sum3_brute_force(data)
	run_time.append( time.clock() - start )

	if PRINT:
		sum3_standard_answer(res)
		print "brute force =\t", res
	a = res

	for i in range(1,len(algor)):

		data = d[:]
		start = time.clock()
		res = fn[i](data)
		run_time.append( time.clock() - start )
		if PRINT:
			sum3_standard_answer(res)
			print algor[i]+" =\t", res
		if N <= 350:						#cutoff for brute force
			assert sum3_results_are_equal(a,res)


	return run_time




if __name__ == '__main__':
	test_verification_routines()

	if True:
		"limit with brute force ~ 320; takes a few mins"
		t = 100
		input_size = [10, 20, 40, 80, 160, 320]
	else:
		"limit with binary sort ~ 5120; takes a few hours"
		t = 20
		input_size = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]

	print "iteratations = ",t
	results = []
	for N in input_size:
		res = [0]*len(algor)
		for i in xrange(t):
			print "(N, i) = ", N, "elements,", i, "out of",t, "runs"
			r = test (N, PRINT=False)
			for j in xrange(len(r)):
				res[j] += r[j]
		for j in xrange(len(res)):
			res[j] = res[j]/t
		results.append( res )

	s = ''
	for i in algor:
		s = s+'\t%8s'%str(i)
	s = s+"\tspeedup"
	print s

	len_algor = len(algor)
	for i in range(len(input_size)):
		s = "%5d"%(input_size[i],)
		for j in range(len_algor):
			s = s+"\t"+"%.3e"%results[i][j]
		s = s+"\t"+"%.1f"%(results[i][len_algor-2]/results[i][len_algor-1])+"x"
		print s

	res = zip(*results)

	print
	for i in range(len(res)):
		a, b = running_time(input_size, res[i])
		#print algor[i],":\tT(N)=", a,"x N ^", b
		print "%12s:\tT(N)=%.3e x N ^ %.3f" % (algor[i], a, b)