n = 5879402
reverse = 0
  
while(n > 0): 
    a = n % 10
    reverse = reverse * 10 + a 
    n = n // 10
      
print(reverse) 
