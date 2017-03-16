def check_anagram(refStr1,refStr2):
    if len(refStr1) != len(refStr2):
        return False
    else:
        return str(list(refStr1).sort()) == str(list(refStr2).sort())

inputStrings=list(raw_input("Enter Two strings : ").split())
print check_anagram(inputStrings[0],inputStrings[1])
