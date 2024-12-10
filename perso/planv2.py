#coding:utf-8
import tkinter as tk

class Application(tk.Frame):
    elements=[]
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.frame=tk.Frame(self)
        """option frame tk"""
        self.frame["bg"]="white"
        #self.frame["command"]=self.objets_frame
        self.frame["height"]=400
        self.frame["width"]=800
        self.frame.pack(side="left")



    def say_hi(self):
        print("hi there, everyone!")
    def objet_frame(self):
            pass

    def update_label(*args):
        var_label2.set(var_entry.get())



root = tk.Tk()
app = Application(master=root)

app.mainloop()
