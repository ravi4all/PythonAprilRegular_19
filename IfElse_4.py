import webbrowser
chat = True

helloIntent = ["hello","hey","hi","hi there","hello there","hey there"]

#Membership Operators - in , not in
while chat:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello User")
    elif msg.startswith("open"):
        web = msg.split()[-1]
        webbrowser.open(web + ".com")
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
