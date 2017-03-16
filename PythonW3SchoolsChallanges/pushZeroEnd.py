#Push all zeros to end of list

numList=map(int,list(raw_input("Enter the List : ").split()))

for val in numList:
    if val == 0:
        numList.append(val)
        numList.remove(val)
print numList
