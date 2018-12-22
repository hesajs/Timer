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

def parse_display():
    display = Text(master=root, height=12, width=15)
    display.grid(row=3, column=1)
    counter=1
    for i in range(1, int(parse_second())+1):
        time.sleep(1)
        display.insert(END, counter%60)
        counter+=1 

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
button1=Button(text="Click Me", command=parse_display)
button1.grid(row=3, column=1)

root.mainloop()