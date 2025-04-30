a= input("Input: ")
b=['a','e','i','o','u','A','E','I','O','U']
for x in b:
    for y in a:
        if x==y:
            a=a.replace(x,'')
print(a)







