from tkinter import *
import time

root = Tk()
root.title("Timer")
root.geometry("400x400")

def parse_second():
    sec=entries_second.get()
    return sec
    
def parse_minute():
    min=entries_first.get()
    return min

def clear():
	list = root.grid_slaves()
	for l in list:
		l.destroy()

def canvas_display():
	clear()
	w = Canvas(root, width=200, height=100)
	w.pack()
	for i in range(5):
		root.after(500)
		w.create_text(100, 50, text=i)
		root.after(500)
		w.delete("all")
	
#LABEL
label1=Label(text="Minutes", font=("Times New Roman", 16))
label1.grid(row=0, column=0)

label2=Label(text="Seconds", font=("Times New Roman", 16))
label2.grid(row=1, column=0)

#ENTRIES
entries_first=Entry()
entries_first.grid(row=0, column=1)

entries_second=Entry()
entries_second.grid(row=1, column=1)

#BUTTONS
button1=Button(text="Click Me", command=canvas_display, compound=CENTER)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()