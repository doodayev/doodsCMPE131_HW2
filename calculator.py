import re

def calculator(number1, number2, operator):
    number1=float(number1)
    number2=float(number2)
    if(operator=="+"):
        return(float(number1+number2))
    if(operator=="-"):
        return(float(number1-number2))
    if(operator=="*"):
        return(float(number1*number2))
    if(operator=="/"):
        return(float(number1/number2))
    if(operator=="//"):
        return(number1//number2)
    if(operator=="**"):
        return(float(number1**number2))
    else:
        return False
    
def parse_input():
    numba1=""
    numba2=""
    number1Done="False"
    ParseThis=input("Enter equation: ")
    #I had to use regex to seperate the numbers from the operators
    #Trying to filter them manually ended up being more of a burden than it would be in C++
    Bruh=re.findall(r'[0-9\.]+|[^0-9\.]+', ParseThis)
    #Bruh=re.split(r'(\D)', ParseThis)
    print(calculator(Bruh[0], Bruh[2], Bruh[1]))
    
    

#parse_input()

