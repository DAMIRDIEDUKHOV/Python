import random
import tkinter

colors_name = ['Red', 'White', 'Yellow', 'Pink', "Blue", 'Black', 'Brown', 'Purple', 'Grenn', 'Cyan']

score = 0
time_left = 60

def startGame(play):
    if time_left == 60:
        countdown()
    changeColor()

def changeColor():
    global score
    global time_left


    if time_left > 0:
        e.focus_set()
        if e.get().lower() == colors_name[1].lower():
            score += 1

        e.delete(0, tkinter.END)
        random.shuffle(colors_name)
        label.config(fg = str(colors_name[1]), text = str(colors_name[0]))
        scoreLabel.config(text = "Score" + str(score))


def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timeLabel.config(text = "Time Left:" + str(time_left))
        timeLabel.sfter(1000, countdown)

root = tkinter.Tk()
root.title("The COLORGAME")
root.geometry("600x400")

instruct = tkinter.Label(root, text = "Wich Color?", font = ("san_serif", 30))
instruct.pack()

scoreLabel = tkinter.Label(root, text = "Press Enter Key To Start", font = ("san-serif", 24))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "Time Left:" + str(time_left), font = ('san_serif', 18))
timeLabel.pack()

label = tkinter.Label(root , font = ("san_serif", 60))
label .pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()