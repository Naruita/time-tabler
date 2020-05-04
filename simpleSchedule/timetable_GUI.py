from tkinter import Tk, Button, LEFT, RIGHT, TOP, BOTTOM, X, Menu, Label, SUNKEN, W
from timetablemaker import make
from timed_link import execute

root = Tk()
root.title("It's the Time Tabler.")

maker = Button(root, text="Make time table", command=make)
maker.pack(side=LEFT)
execute = Button(root, text="Run", command=execute)
execute.pack(side=RIGHT)

status_bar = Label(root, text="Status bar", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, padx=2, fill=X)

root.mainloop()