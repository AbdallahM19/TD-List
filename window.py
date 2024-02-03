from tkinter import *

root = Tk()
root.title("TD-List")
root.geometry("400x400")
label = Label(root, text="my tasks: ",font=('Times new roman', 22))
label.pack(padx=10, pady= 10)
#textbox = Text(root, height= 5 ,font=('Times new roman', 16))
#textbox.pack()

#my_entry = Entry(root)
#my_entry.pack()

buttonframe = Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

buttonframe.columnconfigure(2, weight=1)
#buttonframe.columnconfigure(3, weight=1)

button1 = Button(buttonframe, text="Add task ", font=('Times new roman', 16)).grid(row=0, column=0, sticky=W+E)

button2 = Button(buttonframe, text="Remove task", font=('Times new roman', 16)).grid(row=0, column=1, sticky=W+E)

button3 = Button(buttonframe, text="print task", font=('Times new roman', 16)).grid(row=1, column=0, sticky=W+E)

button4 = Button(buttonframe, text="Write an affiramation", font=('Times new roman', 16)).grid(row=1, column=1, sticky=W+E)

button5 = Button(buttonframe, text="Quit", font=('Times new roman', 16)).grid(row=2, column=0, sticky=W+E)




buttonframe.pack()

root.mainloop()
