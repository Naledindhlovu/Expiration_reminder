from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from  datetime import date
import time
import sqlite3
from tkinter import filedialog
from tkinter import ttk

t = Toplevel()
t.title('Adding Items')
t.geometry("600x400")
img = Image.open("notify-label.png")
tkimage = ImageTk.PhotoImage(img)
my_tree = ttk.Treeview(t)


# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    # print(get_title,get_msg, tt)

    # Background Colors
    t.configure(background='#87CEEB')

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="ico.ico",
                            toast=True,
                            timeout=10)

img_label = Label(t, image=tkimage).grid()

# Label - Title
#t_label = Label(t, text="Title to Notify",font=("poppins", 10),justify=CENTER)
t_label = Label(t, text = 'Enter Details', font=('Arial',12, 'bold'), bg='white', fg='#87CEEB')
t_label.place(x=250, y=70)

# ENTRY - Title              
title = Entry(t, width="25",font=("poppins", 13))
title.insert(0,"Expiraton Reminder")
title.place(x=1230, y=70)

# Label - Message
m_label = Label(t, text="Product Name", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123, y=175)

# Label - min
time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)

#cal=DateEntry(t,selectmode='day')
#cal.place(x=175, y=180)
#cal.grid(row=1,column=1,padx=15)

time_label = Label(t, text="Best Before", font=("poppins", 10))
time_label.place(x=12, y=220)

cal=DateEntry(t,selectmode='day')
cal.place(x=123, y=220)

def my_upd(): # triggered on Button Click
    l1.config(text=cal.get_date()) # read and display date

l1=Label(t,text='data',bg='yellow')  # Label to display date
l1.place(x=270, y=220)

b1=Button(t,text='Read', command=lambda:my_upd())
b1.place(x=220, y=215)

'''set image'''

lbl_show_pic = Label(t, bg='#45aaf2')
btn_browse = Button(t, text='Select Image',bg='grey', fg='#ffffff',
                       font=('verdana',10))
cap_image = Button(t, text='Capture Image',bg='grey', fg='#ffffff',
                       font=('verdana',10))

def selectPic():
    global img
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                           filetypes=(("png images","*.png"),("jpg images","*.jpg")))
    img = Image.open(filename)
    img = img.resize((200,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbl_show_pic['image'] = img

def capture():
    from noti import capImg

btn_browse['command'] = selectPic

cap_image['command'] = capture

lbl_show_pic.place(x=350, y=170)
btn_browse.place(x=175, y=260)
btn_browse.place(x=200, y=260)


# Button
but = Button(t, text="set reminder", font=("poppins", 10, "bold"), fg="#ffffff", bg="#87CEEB", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=320)

t.resizable(0,0)
t.mainloop()

