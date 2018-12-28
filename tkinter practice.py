from tkinter import *

root = Tk()

one = Label(root, text = "One", bg = "red", fg = "white")
one.pack() #notice how the pack isn't given any parameters

two = Label(root, text = "Two", bg = "green", fg = "black")
two.pack(fill = X) # this fills the 'bg' color along the x coordinates

three = Label(root, text = "Three", bg = "blue", fg = "white")
three.pack(side = LEFT, fill = Y) #this fills the 'bg' color along the y coordinates

root.mainloop()

"""Notice (after you run the program) how the vertical blue strip collides with the green? See what happens if you
switch up the code and define one, three, and two in that order.(just cut and paste)

This is all apart of a library called "tkinter" which is for making GUI programs in python (already included).
I'm practicing with this at the moment, and wanted to show you what i'm learning"""