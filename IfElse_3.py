chat = True

#Logical Operators - and, or, not

while chat:
    msg = input("Enter your message : ")
    if msg == "hello" or msg == "hi" or msg == "hey" or msg == "hi there":
        print("Hello User")
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
