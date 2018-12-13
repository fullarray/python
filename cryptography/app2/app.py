from tkinter import *
def stopProg(e):
    root.destroy()
    
root=Tk()
button1=Button(root,
 text="Hello World click to close")
button1.pack()
button1.bind('<Button-1>',stopProg)
root.mainloop()

from tkinter import *
from Crypto.Cipher import AES

#Encrypt
def Encrypt(e):
    label1.configure(text="Decrypt", fg="green")
    #root.destroy()

#Decrypt
def Decrypt(e):
    #obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    label1.configure(text="Encrypt", fg="red")

#Import tkinter library into the program   
root=Tk()

encrypt=Button(root,text="Encrypt")
encrypt.pack(side = RIGHT)
encrypt.bind('<Button-1>',Encrypt)


decrypt=Button(root,text="Decrypt")
decrypt.pack(side = LEFT)
decrypt.bind('<Button-1>',Decrypt)


label1=Label(root,text="Plain Text", fg="brown")
label1.pack()

E1 = Entry(root, bd = 5)
E1.pack(side = RIGHT)

root.mainloop()
