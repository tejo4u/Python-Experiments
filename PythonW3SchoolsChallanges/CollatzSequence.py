#Generate collatz Sequence

numberCollatz=int(raw_input("Enter a Number : "))

collatzSequence = list()
collatzSequence.append(numberCollatz)

while numberCollatz >1:
    if numberCollatz % 2 == 0:
        numberCollatz=int(numberCollatz/2)
        collatzSequence.append(int(numberCollatz))
    else:
        numberCollatz=int(numberCollatz * 3)+ 1
        collatzSequence.append(int(numberCollatz))

print collatzSequence
