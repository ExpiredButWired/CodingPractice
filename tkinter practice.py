from tkinter import *
import tkinter.messagebox

root = Tk()


################################################# Label layouts ########################################


one = Label(root, text = "Label One\n NOT ME", bg = "red", fg = "white")
one.pack() #notice how the pack isn't given any parameters

two = Label(root, text = "Label Two. I EXPAND WITH THE SIZE OF THE WINDOW", bg = "purple", fg = "black")
two.pack(fill = X) # this fills the 'bg' color along the x coordinates

three = Label(root, text = "Label Three.\n I EXPAND \nWITH THE \nSIZE OF THE\n WINDOW", bg = "blue", fg = "white")
three.pack(side = LEFT, fill = Y) #this fills the 'bg' color along the y coordinates


#################################   GRAPHICS, SHAPES & LINES ###########################################


canvas = Canvas(root, width = 200, height = 100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill = "red")
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill = "green")

#################################   POPUP WINDOWS ##############################################


tkinter.messagebox.showinfo("Mr. Testy Mc. Testerson", "I'm testing window popups and drawing to the screen using Tkinter!")
answer = tkinter.messagebox.askquestion("Question # 1", "Do you like the green rectangle?\n I drew it JUST for you!")

if answer == 'yes':
    tkinter.messagebox.showinfo("The results (positive)", "Me too! Let's let it live.")
if answer == 'no':
    tkinter.messagebox.showinfo("The results (negative)", "aww, okay. I'll delete it.")
    canvas.delete(greenBox)
else:
    tkinter.messagebox.showinfo("WUT.jpeg", "what just happened?")

################################## DROPDOWN MENU SYSTEM ###################################################

menu = Menu(root)
root.config(menu = menu)

def doSomethingCool():
    doSomethingCool.counter += 1
    print("I did it %d times" % doSomethingCool.counter)
doSomethingCool.counter = 0


subMenu = Menu(menu)

menu.add_cascade(label = "File", menu = subMenu)

subMenu.add_command(label = "New Project...", command = doSomethingCool)

subMenu.add_separator()

subMenu.add_command(label = "Exit", command = quit)

editMenu = Menu(menu)
menu.add_cascade(label = "Redo", command = doSomethingCool)



#############################  RANDOM TOOLBAR ##############################

toolbar = Frame(root, bg = "blue")
insertButt = Button(toolbar, text = "Insert coins", command = doSomethingCool)

insertButt.pack(side = LEFT, padx = 2, pady = 2)
printButt = Button(toolbar, text = "Play Game", command = doSomethingCool)

printButt.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)

################################# STATUS BAR #########################################

status = Label(root, text = "This is the status bar. This is where we find out some important information", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)

root.mainloop()
