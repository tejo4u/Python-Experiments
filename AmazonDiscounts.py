
#Works only with Amazon India
import sys,webbrowser

#Node Number Dictionary!
nodeDict={"Books":976390031,
"Computers":976393031,
"DVD":976417031,
"Electronics":976420031,
"Jewellery":1951049031,
"Toys":1350381031,
"Watches":1350388031,
"Clothing":1355016031};

if len(sys.argv)<0:
    print "No input! Enter the Product Section and Discount range (Space saperated)."
else:
    inputString=sys.argv
    refernceString="https://www.amazon.in/gp/search/?node="+str(nodeDict[inputString[1]])+"&pct-off="+inputString[2]
    webbrowser.open(refernceString);
