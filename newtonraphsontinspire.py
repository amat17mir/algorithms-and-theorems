
def func( x ): 
    return x * x - x + 2
  # test function one

def derivFunc( x ): 
    return x * x  - 2 * x +1
  # test function two

def newtonRaphson( x ): 
    h = func(x) / derivFunc(x) 
    while abs(h) >= 0.0001: 
        h = func(x)/derivFunc(x) 
          
        # x(i+1) = x(i) - f(x) / f'(x) 
        x = x - h 
      
    print("The value of the root is : ", 
                             "%.4f"% x) 
  
x0 = -1 
newtonRaphson(x0) 


