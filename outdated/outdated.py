months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
la = [ '1','2','3','4','5','6','7','8','9','10','11','12']
while True:
    a = input("Date: ")
    a=a.strip()
    b=a.split('/')
    c=a.split(' ')
    if len(b)==3 and b[0] in la and int(b[1]) < 32 :
        print(b[2]+'-'+f"{("0" + b[0]) if len(b[0]) == 1 else b[0]}"+'-'+f"{("0" + b[1]) if len(b[1]) == 1 else b[1]}")
        break
    if c[0] in months and "," in c[1]  and  int(c[1].strip(',')) < 32 :
        c[1]=c[1].strip(',')
        m=months.index(c[0])
        m=int(m)+1
        m=str(m)
        print(c[2]+'-'+f"{("0"+m) if len (m) == 1 else m }"+'-'+f"{("0" + c[1]) if len(c[1]) == 1 else c[1]}")
        break




