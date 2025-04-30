b=['5','10','25']
x=50
while int(x) >= 1:
    ans=str(x)
    a = input("Amount Due: "+ans+ "\nInsert Coin: ")
    for x in b:
        if a == x:
            a=int(a)
            ans=int(ans)
            ans= ans-a
    x=ans
    if int(ans) < 1:
        ans=abs(ans)
        ans=str(ans)
        print("Change Owed: "+ans)














