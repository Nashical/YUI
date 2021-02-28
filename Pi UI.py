from tkinter import *

def on_escape(event=None):
    print("escaped")
    mywin.destroy()

class MyAppClass(Frame):
    
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.create_label()
    self.create_button()
    
  def create_label(self):
    self.lattrs = Label(self)
    self.lattrs["text"] = "Click Him"
    self.lattrs.grid()
    
  def create_button(self):
    self.battrs = Button(self)
    self.battrs["text"] = "Click Me"
    self.battrs["command"] = self.my_event
    self.battrs.grid()
    
  def my_event(self):
    print ("Thanks for watching.")
    
mywin = Tk()
mywin.configure(background='black')
mywin.attributes("-fullscreen", True)
mywin.bind("<Escape>", on_escape)
mywin.title("Rasp PI GUI")

mywin.after(5000, mywin.destroy)

myapp = MyAppClass(mywin)
mywin.mainloop()
