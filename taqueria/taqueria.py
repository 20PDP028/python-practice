menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

a=float(0.00)
while True  :
    try:
        dish = input("Item ")
        dish=dish.title()
        a="{0:.2f}".format(a+float(menu[dish]))
        a=str(a)
        print("Total: $"+a)
        a=float(a)



    except EOFError :
        break
    except KeyError:
        ...

    else:
        ...



