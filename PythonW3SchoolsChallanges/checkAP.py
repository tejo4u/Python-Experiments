#Check if the progression is arthemetic progression

apProg = map(int,list(raw_input("\nEnter the Progression : ").split()))

apdiff=int(apProg[1]-apProg[0])

for i in range(2,len(apProg)):
    if apProg[i]-apProg[i-1] != apdiff:
        print "\nNot an arthemetic progression."
        exit()
print "\nArthemetic Progression"
