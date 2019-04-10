import webbrowser
import os, random
chat = True

helloIntent = ["hello","hey","hi","hi there","hello there","hey there"]
musicIntent = ["play music","start music","play a song","start a song","play song"]

#Membership Operators - in , not in
while chat:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello User")
    elif msg.startswith("open"):
        web = msg.split()[-1]
        webbrowser.open(web + ".com")
    elif msg in musicIntent:
        os.chdir("C:\\Users\\asus\\Music")
        s = random.choice(os.listdir())
        os.startfile(s)
    elif msg == "show songs":
        # print all the songs available in os.listdir() using a for loop
        # ask the number of song that user wants to play
        # find that index number and play that track
        os.chdir("C:\\Users\\asus\\Music")
        songs = os.listdir()
        for i in range(len(songs)):
            print(i+1,songs[i])
        num = int(input("Enter the track number : "))
        currentSong = songs[num-1]
        os.startfile(currentSong)
    elif msg == "tell me news":
        print("Select the news Category...")
        print("""
1. Sports
2. Politics
3. National
4. International
5. Entertainment
""")
        ch = int(input("Enter the News Type : "))
        if ch == 1:
            pass
        elif ch == 2:
            pass
        elif ch == 3:
            pass
        elif ch == 4:
            pass
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
