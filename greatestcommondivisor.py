def gcd(a, b):  
    if a == 0 : 
        return b      
    return gcd(b%a, a) 
  
a = 270
b = 192
print("gcd(", a , "," , b, ") = ", gcd(a, b))
