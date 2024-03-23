list_name=[]
mylist=["siva","tanuja","john","77",5.54,4154,True]
list_name.append
mylist.insert(3,"sanket")
print(mylist[0])
print(mylist[2])
print(mylist[3])
for i in range(0,len(mylist)):
    print(mylist[4])
    print(mylist[2:4])
print(mylist[:4])
print(mylist[1:])
print(mylist[1:2:])
print(mylist[::5])
print(mylist[:2:4])
print(mylist[1:3:4])

mytuple=("prashant","ashish","rahul","sandaya",)
print(mytuple)
print(type(mytuple))
mytuple=mytuple+("hello",)
##mutability
mytuple[2]="ashish"
mytuple=mytuple+(14,23,"hello")
print(mytuple)
for i in range(0,5):
    n=int(input("enter"))
    mytuple+(n,)

