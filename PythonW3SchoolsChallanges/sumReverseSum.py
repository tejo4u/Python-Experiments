#Find Reverse of sum of rversed numbers
aVal=raw_input("Enter First Number : ")
bVal = raw_input("Enter Second Number : ")
sumofRev = str(int(aVal[::-1]) + int(bVal[::-1]))[::-1]
print sumofRev
