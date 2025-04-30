42

#removing white spaces
def deep():
    a = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    a = a.strip()
    a = a.casefold()
    if a == "42":
        print("Yes")
    elif a == "forty-two":
        print("Yes")
    elif a == "forty two":
        print("Yes")
    else:
        print("No")

deep()
