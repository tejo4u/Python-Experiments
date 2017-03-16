#add two binary numbers.

binNum=list(raw_input("Enter a two Numbers : ").split())
numA= int(binNum[0],2)
numB = int(binNum[1],2)

print bin(numA+numB)[2:] #removing 0b
