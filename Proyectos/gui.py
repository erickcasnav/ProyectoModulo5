from tkinter import*
root = Tk()
root.title("Erick Castro")
root.geometry("450x300+200+200")
labeltext = StringVar()
labeltext.set("Modulo 5")
a=Label(root,text=labeltext.get())
a.pack()
root.mainloop()