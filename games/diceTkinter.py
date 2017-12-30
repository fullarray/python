import tkinter
import random

class DiceFrm(tkinter.Frame):
	def __init__(self, master):
		super().__init__(master)
		die = tkinter.Button(self, text="Roll", command=self.roll)
		die.pack()
		self.roll_result = tkinter.StringVar()
		label = tkinter.Label(self, textvariables=self.roll_result)
		label.pack()
		self.pack()
	
	def roll(self):
		self.roll_result.set(random.randint(1, 6))
	
root = tkinter.Tk()
DiceFrm(master=root).mainloop()
