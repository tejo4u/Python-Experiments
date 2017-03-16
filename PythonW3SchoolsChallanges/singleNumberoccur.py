#Single number that occurs odd number of times

numList=map(int,list(raw_input("Enter the List : ").split()))

numDict = dict()
for num in numList:
     numDict[num] = numDict.get(num,0) + 1

for nKey,nValue in numDict.items():
    if int(nValue%2!=0):
        print nKey,":",nValue
