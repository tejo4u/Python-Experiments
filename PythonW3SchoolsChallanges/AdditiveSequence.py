#find the additive sequence

inputSequence = map(int,list(raw_input("Enter a Sequence : ").split()))

for i in range(2,len(inputSequence),):
    if inputSequence[i] != inputSequence[i-1] + inputSequence[i-2]:
        print "Not Additive Sequence!"
        exit()
print "Additive Sequence"
