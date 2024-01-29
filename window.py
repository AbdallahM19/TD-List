import tkinter as tk
root = tk.Tk()
root.title("TD-List")
root.geometry("400x400")
label = tk.Label(root, text="my tasks: ",font=('Times new roman', 22))
label.pack(padx=10, pady= 10)
#textbox = tk.Text(root, height= 5 ,font=('Times new roman', 16))
#textbox.pack()

#my_entry = tk.Entry(root)
#my_entry.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

buttonframe.columnconfigure(2, weight=1)
#buttonframe.columnconfigure(3, weight=1)

button1 = tk.Button(buttonframe, text="Add task ", font=('Times new roman', 16))
button1.grid(row=0, column=0, sticky=tk.W+tk.E)

button2 = tk.Button(buttonframe, text="Remove task", font=('Times new roman', 16))
button2.grid(row=0, column=1, sticky=tk.W+tk.E)

button3 = tk.Button(buttonframe, text="print task", font=('Times new roman', 16))
button3.grid(row=1, column=0, sticky=tk.W+tk.E)

button4 = tk.Button(buttonframe, text="Write an affiramation", font=('Times new roman', 16))
button4.grid(row=1, column=1, sticky=tk.W+tk.E)

button5 = tk.Button(buttonframe, text="Quit", font=('Times new roman', 16))
button5.grid(row=2, column=0, sticky=tk.W+tk.E)




buttonframe.pack()

root.mainloop()
