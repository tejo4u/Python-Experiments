#Check if a given number is power of Four
number=int(raw_input("Enter a Value : "))
numFlag = True
while number != 1:
    if (number % 4) != 0:
        numFlag = False
        break
    number = number / 4
print numFlag
