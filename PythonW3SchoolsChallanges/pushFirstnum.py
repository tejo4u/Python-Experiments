#Push first number to end of the list
numList= map(int,list(raw_input("Enter the List : ").split()))
numList.append(numList[0])
numList.remove(numList[0])
print numList
