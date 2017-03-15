#Missing Number in a given list
refList = map(int,list(raw_input("Enter the List : ").split()))
missingnum = 0

for i in range(1,len(refList)):
    if refList[i] != refList[i-1]+1:
        missingnum=refList[i-1]+1
        break
print missingnum
