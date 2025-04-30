while True:
    try:
        x=input("Fraction ")
        x,y=x.split('/')
        x=int(x)
        y=int(y)
        ans= round((x/y)*100)
    except (ValueError,ZeroDivisionError):
        ...
    else:
        if x <= y :
            break
if ans >= 99:
    print("F")
elif ans <= 1:
    print("E")
else:
    print(str(ans)+"%")
