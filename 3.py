x="Enter a number\n"
second=int(input(x))
a=second/3600
print(type(a))
b=a*60
print(type(b))
c=b*60
value=round(c)
print(type(c))
print("the result using round :",value)
print(second,"second is",a,"hours,",b,"minutes,",value,"seconds")
