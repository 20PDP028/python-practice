def isnumber(input):
    match input :
        case "0":
            return True
        case "1":
            return True
        case "2":
            return True
        case "3":
            return True
        case "4":
            return True
        case "5":
            return True
        case "6":
            return True
        case "7":
            return True
        case "8":
            return True
        case "9":
            return True
        case _:
            return False

def test(input):
    a= len(input)
    if a <2 or a >6:
        print("invalid")
        return
    x=0
    for i in input:
        if x==2:
            break
        if isnumber(i)== False:
            x+=1
        else :
            print("invalid")
            return
    t= True
    for i in input :
        if isnumber(i):
            t= False
        if isnumber(i)==False and t== False :
            print("invalid")
            return
    print("valid")


v= input("")
test(v)

