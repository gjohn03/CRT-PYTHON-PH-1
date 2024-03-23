n=21
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10 
if n%s==0:
    print("divisble")
else:
    print("not")

n=153
n1=n
nod=0
org=n
while n>0:
    n=n//10
    nod=nod+1
sum1=0
while n1>0:
    digit=n1%10
    sum1=sum1+digit**nod
    n1=n1//10
if sum1==org:
    print("yes")
else:
    print("no")

n=1234
while n>0:
    digit=n%10
    print(digit,end="")
    n=n//10



