#check if a sequence is geometric progression or not

gpProg=map(float,list(raw_input("Enter the Progression : ").split()))

commRatio=float(gpProg[1]/gpProg[0])

for i in range(2,len(gpProg)):
    if gpProg[i-1] * commRatio != float(gpProg[i]): # casting to float coz division return floating.
        print "Not a geometric progression."
        exit()
print "geometric progression."
