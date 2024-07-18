import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()

frame = tk.Frame(root, bg='#45aaf2')

lbl_pic_path = tk.Label(frame, text='Image Path:', padx=25, pady=25,
                        font=('verdana',16), bg='#45aaf2')
lbl_show_pic = tk.Label(frame, bg='#45aaf2')
entry_pic_path = tk.Entry(frame, font=('verdana',16))
btn_browse = tk.Button(frame, text='Select Image',bg='grey', fg='#ffffff',
                       font=('verdana',16))


def selectPic():
    global img
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                           filetypes=(("png images","*.png"),("jpg images","*.jpg")))
    img = Image.open(filename)
    img = img.resize((200,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbl_show_pic['image'] = img
    entry_pic_path.insert(0, filename)


btn_browse['command'] = selectPic

frame.pack()

lbl_pic_path.grid(row=0, column=0)
entry_pic_path.grid(row=0, column=1, padx=(0,20))
lbl_show_pic.grid(row=1, column=0, columnspan="2")
btn_browse.grid(row=2, column=0, columnspan="2", padx=10, pady=10)

root.mainloop()