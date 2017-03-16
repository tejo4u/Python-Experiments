def is_hamming_numbers(x):
	if x == 1:
		return 1
	if x % 2 == 0:
		return is_hamming_numbers(x/2)
	if x % 3 == 0:
		return is_hamming_numbers(x/3)
	if x % 5 == 0:
		return is_hamming_numbers(x/5)
	return 0

def hamming_numbers_sequence(x):
	if x == 1:
		return 1
	hamming_numbers_sequence(x-1)
	if is_hamming_numbers(x) == True:
		print("%s" % x, end=' ')


print(is_hamming_numbers(7))
print(is_hamming_numbers(1))

hamming_numbers_sequence(24)
print()
