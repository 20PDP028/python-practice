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

def is_valid(s):
    a= len(s)
    if a <2 or a >6:
        return False
    x=0
    for i in s:
        if x==2:
            break
        if isnumber(i)== False:
            x+=1
        else :
            return False
    t= True
    for i in s :
        if isnumber(i) and t==True:
            if i=="0":
                return False
            t= False
        if isnumber(i)==False and t== False :
            return False
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")





main()
