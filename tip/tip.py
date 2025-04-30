def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    b=d.replace("$","")
    return float(b)


def percent_to_float(p):
    o=p.replace("%","")
    return float(o)/100


main()
