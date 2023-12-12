a="use a nonbreaking space or nonbreaking hyphen instead of a regular space or hyphen. Click where you want to insert the nonbreaking space."
b=dict()
c=a.split(" ")
for i in c:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
print(b)


