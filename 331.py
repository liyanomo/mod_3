331.py
a = float(input('Enter first side: ')) 
b = float(input('Enter second side: ')) 
c = float(input('Enter third side: ')) 
def area (a,b,c):
    pass
    p = (a+b+c)/2
    area = ((p*(p-a)*(p-b)*(p-c)) ** 0.5 )
    return area
print (area (a,b,c))
        