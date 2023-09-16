x="Enter a number\n"
second=int(input(x))
a=second/3600
print(type(a))
b=a*60
print(type(b))
c=b*60
print(type(c))
y=round(c)
print(type(y))
print(second,"second is",a,"hours,",b,"minutes,",y,"seconds")
