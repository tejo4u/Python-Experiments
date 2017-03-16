#Count Number that doesnt occur twice or just occurs only once

#Input a list

nonRepList=map(int,list(raw_input("Enter the list").split()))

repDict=dict()

for value in nonRepList:
    repDict[value] = repDict.get(value,0) + 1

onceOccur=dict()

for key,value in repDict.items():
    if value == 1:
        onceOccur[key]=onceOccur.get(key,0) + 1
print onceOccur
