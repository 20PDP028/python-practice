# getting input
a= input("Expression:")
x,y,z = a.split(" ")
x= float(x)
z= float(z)
match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "/":
        print(x/z)
    case "*":
        print(x*z)
