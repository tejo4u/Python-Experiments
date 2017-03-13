#Check if a given number is power of two
number=int(raw_input("Enter a Value : "))
numFlag = True
while number != 1:
    if (number % 2) != 0:
        numFlag = False
        break
    number = number / 2
print numFlag
