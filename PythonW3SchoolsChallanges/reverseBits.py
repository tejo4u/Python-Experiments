#Reverse Bits of an integer
#If yopu dont understand the whole thing (Even i dont Completly) visit Source : http://stackoverflow.com/questions/746171/best-algorithm-for-bit-reversal-from-msb-lsb-to-lsb-msb-in-c
#Bit Dwindling hacks : http://graphics.stanford.edu/~seander/bithacks.html

def reverseBits(x):
    x = (((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1));
    x = (((x & 0xcccccccc) >> 2) | ((x & 0x33333333) << 2));
    x = (((x & 0xf0f0f0f0) >> 4) | ((x & 0x0f0f0f0f) << 4));
    x = (((x & 0xff00ff00) >> 8) | ((x & 0x00ff00ff) << 8));
    return((x >> 16) | (x << 16));

inputVal = int(raw_input("Enter a Number : "))
print "The Reversed Bit Value (32 bit unsigned ) is : ",reverseBits(inputVal)
