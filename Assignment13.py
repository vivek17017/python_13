#Q1
x=500
if x>=100 and x<=999:
    print("three digit number")
else:
    print("not a three digit")

#Q2
x=-0
if x>0:
    print("positive")
elif x<0:
    print("negative")
else:
    print("zero")
#Q3
a,b,c=3,5,6

#Q5
x=896
a=x%10
b=x//100
c=(x%100)//10
if a>=b and a>=c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)




