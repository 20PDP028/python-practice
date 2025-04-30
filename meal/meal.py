# getting username
def main():
    time= input("What time is it? ")
    a=convert(time)
    if  7.00 <= a <= 8.00 :
        print("breakfast time")
    elif 12.00 <= a <= 13.00:
        print("lunch time")
    elif 18.00 <= a <= 19.00:
        print("dinner time")



def convert(time):
    h,m= time.split(":")
    h=h.removeprefix('0')
    h=float(h)
    m=float(m)
    m=m/60
    ans=h+m
    return ans

if __name__ == "__main__":
    main()

