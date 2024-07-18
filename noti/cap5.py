import sqlite3
from tkinter import * 
from tkinter import filedialog

root = Tk()

#File dialog to select files
def filedialogs():
    global get_image
    get_image = filedialog.askopenfilenames(title="SELECT IMAGE", filetypes=( ("png", "*.png"), ("jpg" , "*.jpg"), ("Allfile", "*.*")))

#Image need to be conver into binary before insert into database
def conver_image_into_binary(filename):
    with open(filename, 'rb') as file:
        photo_image = file.read()
    return photo_image

def insert_image():
    image_database = sqlite3.connect("Image_data.db")
    data = image_database.cursor()
    
    for image in get_image:
       insert_photo   = conver_image_into_binary(image)
       data.execute("INSERT INTO products(productName,expiryDate,Image) Values('milk','2000-sep-17',:image)", 
                 {'image': insert_photo })

    image_database.commit()
    image_database.close()


#Create database in current file and create table if not exist

def create_database():
    image_database = sqlite3.connect("Image_data.db") 
    data = image_database.cursor()

    data.execute("CREATE TABLE IF NOT EXISTS products(barcode INTEGER PRIMARY KEY AUTOINCREMENT, productName TEXT, expiryDate TEXT, Image BLOB)")

    image_database.commit()
    image_database.close()

create_database()


select_image = Button(root, text="Select Image", command=filedialogs)
select_image.grid(row=0, column=0, pady=(100, 0), padx=100)

save_image = Button(root, text="Save", command=insert_image)
save_image.grid(row=1, column=0)


root.mainloop()