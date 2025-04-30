# getting username
u = input("camelCase ")
i = 0
temp=''
while i < len(u):
    if u[i].isupper():
        temp+='_'
        x=u[i].lower()
        temp+=x
        i+=1
        continue
    temp+=u[i]


    i+=1
print(temp)












