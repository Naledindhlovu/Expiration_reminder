from tkinter import *
from matplotlib.pyplot import text
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from  datetime import date, datetime
import time
import sqlite3
from tkinter import filedialog
from tkinter import ttk
import cv2
import tkinter as tk

import pyttsx3
import easyocr

engine=pyttsx3.init()

t = tk.Toplevel()
t.title('Adding Items')
t.attributes('-fullscreen', True)
img = Image.open("notify-label.png")
tkimage = ImageTk.PhotoImage(img)
my_tree = ttk.Treeview(t)

global exText, exText1
exText = StringVar()
exText1 = StringVar()
exText=""

#Text To Speech

# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    get_date = cal.get()
    # print(get_title,get_msg, tt)

    # Background Colors
    t.configure(background='#87CEEB')

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:

        productName = str(get_msg)
        expiryDate = str(get_date)

        insert_image(productName,expiryDate)

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

img_label = Label(t, image=tkimage)
img_label.place(relx=0.5, rely=0.05,anchor=CENTER)

# Label - Title
#t_label = Label(t, text="Title to Notify",font=("poppins", 10),justify=CENTER)
t_label = Label(t, text = 'Enter Details', font=('Arial',12, 'bold'), bg='white', fg='#87CEEB')
t_label.place(relx=0.5, rely=0.1,anchor=CENTER)

# ENTRY - Title              
title = Entry(t, width="25",font=("Times", 13))
title.insert(0,"Expiraton Reminder")
title.place(x=2230, y=70)

# Label - Message
m_label = Label(t, text="PRODUCT NAME", font=("Times", 10))
m_label.place(relx=0.3, rely=0.15,anchor=CENTER)

# ENTRY - Message
msg = Entry(t, width="40", font=("Times", 13),textvariable=exText1)
msg.insert(0,exText)
msg.place(relx=0.5, rely=0.15,anchor=CENTER)

#Drop Down

category = ["Canned","Dairy Product","Vegetable","Fruit"]
lab1 =Label(t,text="SELECT CATEGORY")
cate = ttk.Combobox(t,values=category,width=30)
cate.place(relx=0.5, rely=0.2,anchor=CENTER)

m_label = Label(t, text="SELECT CATEGORY", font=("Times", 10))
m_label.place(relx=0.35, rely=0.2,anchor=CENTER)

# Label - Time
time_label = Label(t, text="SET TIME (min)", font=("Times", 10))
time_label.place(relx=0.4, rely=0.25,anchor=CENTER)

# ENTRY - Time
time1 = Entry(t, width="5", font=("Times", 13))
time1.place(relx=0.5, rely=0.25,anchor=CENTER)

#cal=DateEntry(t,selectmode='day')
#cal.place(x=175, y=180)
#cal.grid(row=1,column=1,padx=15)

time_label = Label(t, text="BEST BEFORE", font=("Times", 10))
time_label.place(relx=0.4, rely=0.3,anchor=CENTER)

cal=DateEntry(t,selectmode='day',mindate=datetime.now())
cal.place(relx=0.5, rely=0.3,anchor=CENTER)

def my_upd(): # triggered on Button Click
    l1.config(text=cal.get_date()) # read and display date

l1=Label(t,text='Date Preview',bg='yellow')  # Label to display date
l1.place(relx=0.6, rely=0.3,anchor=CENTER)

b1=Button(t,text='Read', command=lambda:my_upd())
b1.place(relx=0.55, rely=0.3,anchor=CENTER)

'''set image'''

def textToSpeech():
    engine.say(exText1.get())
    engine.runAndWait()
    engine.stop()

lbl_show_pic = Label(t, bg='#45aaf2')
btn_browse = Button(t, text='Select Image',bg='grey', fg='#ffffff',
                       font=('verdana',10))
cap_image = Button(t, text='Capture Image',bg='grey', fg='#ffffff',
                       font=('verdana',10))
extract_btn = Button(t, text='Speak Text',bg='grey', fg='#ffffff',
                         font=('verdana',10), command=textToSpeech)

def selectPic():
    global img
    global filename
    
    filename = filedialog.askopenfilename(title="SELECT IMAGE", filetypes=( ("png", "*.png"), ("jpg" , "*.jpg"), ("Allfile", "*.*")))
    #filename = filedialog.askopenfilenames(title="SELECT IMAGE", filetypes=( ("png", "*.png"), ("jpg" , "*.jpg"), ("Allfile", "*.*")))
    img = Image.open(filename)
    img = img.resize((300,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbl_show_pic['image'] = img
    #extract_btn['command'] = 
 
    extract(filename)
    t.deiconify()

#capturing image
#def capture():
    # t.withdraw()
    # cam = cv2.VideoCapture(0)
    
    # cv2.namedWindow("test")
    
    # img_counter = 0
    
    # while True:
    #     ret, frame = cam.read()
    #     if not ret:
    #         print("failed to grab frame")
    #         break
    #     cv2.imshow("test", frame)
    
    #     k = cv2.waitKey(1)
    #     if k%256 == 27:
    #         # ESC pressed
    #         t.deiconify()
    #         print("Escape hit, closing...")
    #         break
    #     elif k%256 == 32:
    #         # SPACE pressed
    #         img_name = "opencv_frame_{}.png".format(img_counter)
    #         cv2.imwrite(img_name, frame)
    #         print("{} written!".format(img_name))
    #         img_counter += 1
    
    # cam.release()
    
    # cv2.destroyAllWindows()

def capture():
    import file

btn_browse['command'] = selectPic
cap_image['command'] = capture

lbl_show_pic.place(relx=0.5, rely=0.45,anchor=CENTER)
btn_browse.place(relx=0.5, rely=0.6,anchor=CENTER)
cap_image.place(relx=0.5, rely=0.65,anchor=CENTER)
extract_btn.place(relx=0.7, rely=0.15,anchor=CENTER)

#Image need to be conver into binary before insert into database
def convert_image_into_binary(filename):
    with open(filename, 'rb') as file:
        photo_image=file.read()
    return photo_image

#inserting data
def insert_image(productName,expiryDate):
    image_database = sqlite3.connect("Image_data.db")
    data = image_database.cursor()
    
    for image in filename:
       insert_photo   = convert_image_into_binary(image)
       data.execute("INSERT INTO products(productName,expiryDate,Image) Values('" + str(productName) + "','" + str(expiryDate) + "',:image)", 
                 {'image': insert_photo })

    image_database.commit()
    image_database.close()


#create database
def create_database():
    image_database = sqlite3.connect("Image_data.db") 
    data = image_database.cursor()

    data.execute("CREATE TABLE IF NOT EXISTS products(barcode INTEGER PRIMARY KEY AUTOINCREMENT, productName TEXT, expiryDate TEXT, Image BLOB)")

    image_database.commit()
    image_database.close()

create_database()

# extracting data from image

def extract(path):
    
    reader = easyocr.Reader(['en'])

    results = reader.readtext(path)

    text = ''

    for result in results:
        text += result[1] + ' '
        
    exText = text 
    messagebox.showinfo("Sucess", "text extracted")
    msg.insert(0,exText)

# Button
but = Button(t, text="set reminder", font=("poppins", 10, "bold"), fg="#ffffff", bg="#87CEEB", width=20,
             relief="raised",
             command=get_details)
but.place(relx=0.5, rely=0.7,anchor=CENTER)

Quit = tk.Button(t, text = "Back", width="10", command = t.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='white', fg='black',relief='groove', justify = 'center', pady='5')
Quit.place(anchor ='sw',rely=1,relx=0.9)

t.resizable(0,0)
t.mainloop()
