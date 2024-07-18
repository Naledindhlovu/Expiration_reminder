from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract
import tkinter.messagebox as msg

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

root = Tk()
root.title('Image to Text')
root.geometry("1100x700")


###########images########################
heading = PhotoImage(file="C:\\Users\\Mosa\\Downloads\\image-to-text-main\\image-to-text-main\\heading.png")
upload_img = PhotoImage(file="C:\\Users\\Mosa\\Downloads\\image-to-text-main\\image-to-text-main\\upload_img.png")
extract_img = PhotoImage(file="C:\\Users\\Mosa\\Downloads\\image-to-text-main\\image-to-text-main\\extract_img.png")
#############################################################

# Frame start here #####################3
frame_1 = Frame(root, bg="#01539D")
frame_1.place(x=0, y=0, height=400, width=1100)

heading_lb = Label(frame_1, image=heading, bg='#01539D', bd=0)
heading_lb.place(x=60, y=40)

frame_2 = Frame(root, bg="#EFA37F")
frame_2.place(x=0, y=400, height=300, width=1100)


uploaded_img = Label(frame_1, bd=0)

#############################################################


def extract(path):
    file = open("new_tests.txt", "a+")
    file.write("")
    file.close()
    real_image = cv2.imread(path)
    Sample_img = cv2.cvtColor(real_image, cv2.COLOR_BGR2RGB)
    file = open("new_tests.txt", "a")
    texts = pytesseract.image_to_data(Sample_img)
    # print(texts)
    mytext = ""
    prevy = 0
    for cnt, text in enumerate(texts.splitlines()):
        if cnt == 0:
            continue
        text = text.split()
        if len(text) == 12:
            x, y, w, h = int(text[6]), int(text[7]), int(text[8]), int(text[9])
            if (len(mytext) == 0):
                prey = y
            if (prevy - y >= 10 or y - prevy >= 10):
                print(mytext)
                file.write(mytext)
                file.write("\n")
                Label(frame_2, text=mytext, font=('Times', 15, 'bold'),
                      bg="#01539D", fg="white").pack()
                mytext = ""
            mytext = mytext + text[11] + " "
            prevy = y
    Label(frame_2, text=mytext, font=(
        'Times', 15, 'bold'), bg="red", fg="white").pack()
    msg.showinfo("Sucess", "Your text has been saved in file.")
    


def extract_btn(path):
    extractBtn = Button(frame_1, image=extract_img, command=lambda: extract(path), bg="#01539D", bd=0, pady=15,
                        padx=15, font=('Times', 15, 'bold'))
    extractBtn.place(x=90, y=280)


def upload():
    try:
        path = filedialog.askopenfilename()
        timage = Image.open(path)
        timage = timage.resize((400, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(timage)
        uploaded_img.configure(image=img)
        uploaded_img.timage = img
        extract_btn(path)
    except Exception as es:
        print(es)


Button(frame_1, image=upload_img, command=upload, bg='#01539D', bd=0,
       font=('Times', 15, 'bold')).place(x=60, y=150)
# newline.configure(text='\n')
# newline.pack()
uploaded_img.place(x=600, y=100)
root.mainloop()
