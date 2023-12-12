a=input("enter a word : ")
if len(a)<3:
    print(a)
elif a[-3:]=="ing":
    print(a+"ly")
else:
    print(a+"ing")