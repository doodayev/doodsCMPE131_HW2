def tripler(func):
    def wrapper(*args, **kwargs):
 
        print("Inside the calculation function")
         #thing returns whatever got inputted
        thing=func(*args, **kwargs)
        thing=func(*args, **kwargs)
        thing=func(*args, **kwargs)
        print("Before return from calculation function")
        return thing
 
    return wrapper
 
 
#@tripler
#def addition(a, b):
#    print("Inside the addition function")
#    return a + b
 
 
#print("Sum =", addition(5, 10))
