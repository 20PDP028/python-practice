my_dictionary = {}
try:
    while True:
        items = input().lower()
        items = items.strip()

        if  items in my_dictionary :
            my_dictionary[items] += 1
        else:
            my_dictionary[items] = 1
except EOFError :
    ...
finallist = sorted(my_dictionary.items())

for items, count in finallist:
    print(f"{count} {items.upper()}")

