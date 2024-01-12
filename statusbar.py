import tkinter as tk

class StatusBar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent, border=1, relief=tk.SUNKEN)
        self.label = tk.Label(master=self, text="")
        self.label.grid(row=0, column=0, sticky=tk.W)
        self.grid(row=1, column=0, sticky=tk.EW)
        
    def setText(self, newText):
        self.label.config(text=newText)

    def clearText(self):
        self.label.config(text="")
