#Check if a given Number is power of another
powerNumber=int(raw_input("Enter a Value of X (Power): "))
baseNumber = int(raw_input("Enter the Value of Y (Base)"))
numFlag = True
while powerNumber != 1:
    if (powerNumber % baseNumber) != 0:
        numFlag = False
        break
    powerNumber/=baseNumber
print numFlag
