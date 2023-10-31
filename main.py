name=input("enter name : ")
if len(name)<3:
    print("name must atleast 3 charectors")
elif len(name)>10:
    print("name must not cross 10 charectors")
else:
    print("name is perfect")