#Find majority element in the list where majority = n/2 times in list of n

numList = map(int,list(raw_input("Enter a List : ").split()))
numDict = dict()

for num in numList:
    numDict[num]=numDict.get(num,0) + 1

for key,value in numDict.items():
    if value > int(len(numDict)/2):
        print key,":",value
