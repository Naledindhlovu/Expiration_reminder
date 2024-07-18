import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Item list")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)
appName = "Expiration Reminder"

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def delete(data):
    conn = sqlite3.connect("Image_data.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS products(barcode INTEGER PRIMARY KEY AUTOINCREMENT, productName TEXT, expiryDate TEXT, Image BLOB)")

    cursor.execute("DELETE FROM products WHERE barcode = '" + str(data) + "'")
    conn.commit()


def read():
    conn = sqlite3.connect("Image_data")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS products(barcode INTEGER PRIMARY KEY AUTOINCREMENT, productName TEXT, expiryDate TEXT, Image BLOB)")

    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    conn.commit()
    return results

read()

def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

titleLabel = Label(root, text=appName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
buttonDelete.grid(row=3, column=9, columnspan=1)

def add_data():
    from noti import notifierpy

buttonAdd = Button(
    root, text="Add", padx=5, pady=5, width=5,
    bd=3, font=('Times', 15), bg="#e62e00", command=add_data)
buttonAdd.grid(row=4, column=9, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("barcode", "productName", "expiryDate", "Image")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("barcode", anchor=W, width=100)
my_tree.column("productName", anchor=W, width=200)
my_tree.column("expiryDate", anchor=W, width=150)
my_tree.column("Image", anchor=W, width=150)
my_tree.heading("barcode", text="barcode", anchor=W)
my_tree.heading("productName", text="productName", anchor=W)
my_tree.heading("expiryDate", text="expiryDate", anchor=W)
my_tree.heading("Image", text="Image", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()

