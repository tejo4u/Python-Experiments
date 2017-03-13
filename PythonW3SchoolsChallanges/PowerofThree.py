#Check if a given number is power of three
number=int(raw_input("Enter a Value : "))
numFlag = True
while number != 1:
    if (number % 3) != 0:
        numFlag = False
        break
    number = number / 3
print numFlag
