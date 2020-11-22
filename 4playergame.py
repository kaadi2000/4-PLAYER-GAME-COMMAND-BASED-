import random
import time

min=0
max=77

def main_menu():
    print("\n1.Play Game\n2.How to Play?\n3.Rules\n4.Developer Contact")
    print("5.Credit\n6.Disclaimer\n7.Exit")
    main=input("\nEnter your choice:")
    if main == "1":
        play_game()
    elif main == "2":
        how_to_play()
    elif main == "3":
        rules()
    elif main == "4":
        developer_contact()
    elif main == "5":
        credit()
    elif main == "6":
        disclaimer()
    elif main == "7":
        exit()
    else:
        print("\nInvalid Input! Try Again!\n")
        time.sleep(2.0)
        main_menu()

def play_game():
    score=[0,0,0,0]
    life=[3,3,3,3]
    name=[]
    input("Press ENTER to Start.")
    for i in range(0,4):
        name.append(input("\nEnter Player name:"))

    while life[0] != 0 or life[1] != 0 or life[2] != 0 or life[3] != 0:
        print("\nChoosing Question....\n")
        time.sleep(2.0)
        index=choose_question()
        ans=[]
        for i in range(0,4):
            if life[i] != 0:
                print("\n{}:".format(name[i]))
                ans.append(input())
                if ans[i] == answer(index):
                    score[i] = score[i] + 1
                else:
                    life[i] = life[i] - 1
            else:
                print("No life remaining for Player ",i)
                ans.append(0)
        for i in range(0,4):
            if ans[i] == answer(index):
                print("Player {} got it correct.".format(i+1))
            elif ans[i] == 0:
                break
            else:
                print("Player {} got it wrong.".format(i+1))
        print("\nScore Updated.")

    print("GAME OVER!!\n")
    for i in range(0,4):
        print("Player {} Score is {}.".format(i+1,score[i]))
    time.sleep(4.0)
    input("\nPress ENTER for Main Menu.")
    main_menu()


def choose_question():
    choose=random.randint(min,max)
    ques=["What has to be broken before you can use it?","I’m tall when I’m young, and I’m short when I’m old. What am I?","What month of the year has 28 days?","What is full of holes but still holds water?","What is always in front of you but can’t be seen?","What can you break, even if you never pick it up or touch it?","What goes up but never comes down?","A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?","What gets wet while drying?","What can you keep after giving to someone?","I shave every day, but my beard stays the same. What am I?","I shave every day, but my beard stays the same. What am I?","You walk into a room that contains a match, a kerosene lamp, a candle and a fireplace. What would you light first?"," I have branches, but no fruit, trunk or leaves. What am I?","What can’t talk but will reply when spoken to?","The more of this there is, the less you see. What is it?","David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?","I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?","What has many keys but can’t open a single lock?","What can you hold in your left hand but not in your right?"," What is black when it’s clean and white when it’s dirty?","What gets bigger when more is taken away?"," I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?","I’m found in socks, scarves and mittens; and often in the paws of playful kittens. What am I?","Where does today come before yesterday?","What invention lets you look right through a wall?","If you’ve got me, you want to share me; if you share me, you haven’t kept me. What am I?","What can’t be put in a saucepan?","What goes up and down but doesn’t move?","If you’re running in a race and you pass the person in second place, what place are you in?","It belongs to you, but other people use it more than you do. What is it?","What has lots of eyes, but can’t see?"," What has one eye, but can’t see?","What has many needles, but doesn’t sew?"," What has hands, but can’t clap?","What has legs, but doesn’t walk?","What has one head, one foot and four legs?","What can you catch, but not throw?","What kind of band never plays music?","What has many teeth, but can’t bite?","What is cut on a table, but is never eaten?","What has words, but never speaks?","What runs all around a backyard, yet never moves?","What can travel all around the world without leaving its corner?","What has a thumb and four fingers, but is not a hand?","What has a head and a tail but no body?","Where does one wall meet the other wall?","What building has the most stories?","What tastes better than it smells?","What has 13 hearts, but no other organs?","It stalks the countryside with ears that can’t hear. What is it?","What kind of coat is best put on wet?","What has a bottom at the top?","What has four wheels and flies?"," I am an odd number. Take away a letter and I become even. What number am I?","If two’s company, and three’s a crowd, what are four and five?","What five-letter word becomes shorter when you add two letters to it?","What begins with an “e” and only contains one letter?","What is 3/7 chicken, 2/3 cat and 2/4 goat?","I am a word of letters three; add two and fewer there will be. What word am I?","What word of five letters has one left when two are removed?","What word is pronounced the same if you take away four of its five letters?","What word in the English language does the following: The first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word?","What is so fragile that saying its name breaks it?","What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?","What can fill a room but takes up no space?","If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?","The more you take, the more you leave behind. What are they?"," I turn once, what is out will not get in. I turn again, what is in will not get out. What am I?","People make me, save me, change me, raise me. What am I?","What breaks yet never falls, and what falls yet never breaks?","What goes through cities and fields, but never moves?","I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?"," The person who makes it has no need of it; the person who buys it has no use for it. The person who uses it can neither see nor feel it. What is it?","With pointed fangs I sit and wait; with piercing force I crunch out fate; grabbing victims, proclaiming might; physically joining with a single bite. What am I?","I have lakes with no water, mountains with no stone and cities with no buildings. What am I?","What does man love more than life, hate more than death or mortal strife; that which contented men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to their graves?"]
    print(ques[choose])
    return choose

def answer(index):
    ans=["Egg","Candle","All","Sponge","Future","Promise","Age","He was bald","Towel","Your word","Barber","All are married","Match","Bank","Echo","Darkness","David","Shadow","Piano","Right Elbow","Chalkboard","Hole","Breadth","Yarn","Dictionary","Window","Secret","Lid","Staircase","Second Place","Name","Potato","Needle","Chritmas Tree","Clock","Table","Bed","Cold","Rubber band","Comb","Deck of cards","Book","Fence","Stamp","Glove","Coin","On the corner","Library","Tongue","Deck of cards","Corn","Coat of paint","Legs","Garbage Truck","Seven","Nine","Short","Envelope","Chicago","Few","Stone","Queue","Heroine","Silence","River","Light","Mirror","Footsteps","Key","Money","Day and Night","Road","Fire","Coffin","Stappler","Map","Nothing"]
    return ans[index]

def developer_contact():
    print("\nDeveloper Name: Kumar Aditya\nE-mail: aditya.g.2005001@gmail.com\n")
    input("Press any key for Main Menu:")
    main_menu()

def disclaimer():
    print("\nThis program is purely made for entertainment purpose! So kindly\ndon't take it on your heart, mind, leg etc\n")
    input("Press any key for main menu:")
    main_menu()

def credit():
    print("This program is made from the help of the greatest god of all time.\nShre Shree GOOGLE Baba")
    input("Press any key for main menu:")
    main_menu()

print("Welcome to the Game!")
main_menu()
