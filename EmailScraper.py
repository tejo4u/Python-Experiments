# Extracts Email from text Copied into Keyborad
import re
import pyperclip

DataSet=pyperclip.paste() #Copies Data From Clipborad

EmailRegxObj=re.compile(r'[a-zA-Z0-9_+.]+@[a-zA-Z0-9_+.]+') #Serching for Email Pattern
EmailExtracts=EmailRegxObj.findall(DataSet) #Finds and Stores every eamil in the DataSet

#Print Every Email line By line
for email in EmailExtracts:
    print email
