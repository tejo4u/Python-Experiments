#Finding the Perfect Square
def return_digiroot(number): #Returns the digital root
    digiSum=0
    while number > 0:
        digiSum+=number % 10
        number/=10
        if len(str(digiSum)) > 1 and number==0:
            number=digiSum
            digiSum=0
    return digiSum

testNumber=int(raw_input("Enter a number : "))
numDigiRoot = return_digiroot(testNumber)

if testNumber % 10 == 2 or testNumber % 10 == 3 or testNumber %10 == 7 or testNumber % 10 == 8:
    print testNumber,"is not a prefect Square."
else:
    if numDigiRoot == 0 or numDigiRoot == 1 or numDigiRoot == 4 or numDigiRoot ==7 or numDigiRoot == 9:
        print  testNumber,"is a Perfect Square."
    else:
        print testNumber,"is not a Perfect Square."
