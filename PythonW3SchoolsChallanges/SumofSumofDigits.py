#Find Digital Roots of a number
def return_digiroot(number): #Returns the digital root
    digiSum=0
    while number > 0:
        digiSum+=number % 10
        number/=10
        if len(str(digiSum)) > 1 and number==0:
            number=digiSum
            digiSum=0
    return digiSum

refValue = int(raw_input("Enter a value : "))
print "Digital Roots / Sum of Sum of Digits is : ",return_digiroot(refValue)
