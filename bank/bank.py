# getting input from user by giving greetings
a= input ("Greeting: ")
a=a.lstrip()
a=a.casefold()
#checking for hello in the sentece
if  a.startswith("hello"):
    print("$0")
elif a.startswith("h"):
    print("$20")
else :
    print("$100")



# checking for h in the sentence
# if not fine 100

