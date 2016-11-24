import re
import pyperclip

print "\t---------Text Censor 0.1----------\n"
print "Copy the Text to be Censored.(Copy to Clipboard)\n"
words=raw_input("Enter the words to be Censored (Space Saperated): ")   #User Input

TextSet=words.split()           #Converts Space Spaerated Input to List of words
DataSet=pyperclip.paste()       #Paste from Clipboard the text that has been copied

for word in TextSet:            #Iterates through TextSet and Censors the words
    CensoreWordRegx=re.compile(word,re.IGNORECASE)
    DataSet=CensoreWordRegx.sub('*'*len(word),DataSet)

pyperclip.copy(DataSet)
print "\nDone. Successfully Processed! Check Your Clipboard.\n"
