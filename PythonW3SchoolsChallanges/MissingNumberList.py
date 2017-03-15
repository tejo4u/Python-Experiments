#Generate the missing list

refList=list(raw_input("Enter the list (Space saperated) ").split()) #Takes input as string and converts it into list of characters
refList = map(int,refList) #Converts list of chars to list of ints

missingList=list()

for i in range(1,len(refList)):
    if refList[i-1] != refList[i]-1:
        missingList.extend(range(refList[i-1]+1,refList[i])) #Appends list of missing numbers to the missing value list
print missingList
