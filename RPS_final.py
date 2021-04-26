import random
from tkinter import *
from PIL import Image,ImageTk

stats = []


def get_winner(call):
    if random.random() <= (1 / 3):
        throw = "rock"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw = "scissors"
    else:
        throw = "paper"

    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors") \
            or (throw == "scissors" and call == "rock"):
        stats.append('W')
        result = "You won!"
    elif throw == call:
        stats.append('D')
        result = "It's a draw"
    else:
        stats.append('L')
        result = "You lost!"

    global output
    output.config(text="Computer did: " + throw + "\n" + result)


def pass_s():
    get_winner("scissors")


def pass_r():
    get_winner("rock")


def pass_p():
    get_winner("paper")


window = Tk()
window.title("Rock Paper Scissors")

l1=Label(window,text="WELCOME FRIENDS",font= 100,fg="black",border=10)
l1.pack()

img = Image.open("C:\\Users\\LENOVO\\Desktop\\WORK\\project\\RPS\\RPS.png")
x = 4
y = 4
re_img = img.resize((2048//x,1316//y))
img = ImageTk.PhotoImage(re_img)
l2=Label(image = img)
l2.pack()


l3=Label(window,text="Lets Play !",font= 100,fg="black",border=10)
l3.pack()

l4=Label(window,text="          ",font= 100,fg="black",border=10)
l4.pack()

scissors = Button(window, text="Scissors", bg="#ff9999", padx=10, pady=5, command=pass_s, width=20)
rock = Button(window, text="Rock", bg="#80ff80", padx=10, pady=5, command=pass_r, width=20)
paper = Button(window, text="Paper", bg="#3399ff", padx=10, pady=5, command=pass_p, width=20)
output = Label(window, width=20, fg="red", text="What's your call?")

scissors.pack(side="left")
rock.pack(side="left")
paper.pack(side="left")
output.pack(side="right")
window.mainloop()

for i in stats: print(i, end=" ")
if stats.count('L') > stats.count('W'):
    result = "\nYou loose the series."
elif stats.count('L') == stats.count('W'):
    result = "\nSeries ended in a draw."
else:
    result = "\nYou win the series."

print(result)
