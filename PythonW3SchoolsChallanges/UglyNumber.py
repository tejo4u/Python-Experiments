#Ugly number is a number who prime factors are divisible by 2 3 or 5

numVal=int(raw_input("Enter a Number : "))

if numVal % 2 == 0 or numVal % 5 == 0 or numVal % 3==0:
    print True
else:
    print False 
