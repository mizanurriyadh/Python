a=60       #60= 0011 1100
b=13       #13= 0000 1101

print("a=", a, ':', bin(a))
print("b=",b, ':', bin(b))

c = a & b  #AND operation
print("c=",c,':', bin(c))

c = a | b  #OR operation
print("c=",c,':', bin(c))

c = a ^ b  #XOR operation
print("c=",c,':', bin(c))


c = ~a  #Compliment
print("c=",c,':', bin(c))

c = a << 2  #Left Shift
print("c=",c,':', bin(c))

c = a >> 2  #Right Shift
print("c=",c,':', bin(c))