from tkinter import *
from PIL import ImageTk, Image
import os


def change_picture():
    global count
    img_label.config(image = img_array[count%len(img_array)])
    count = count+1


count = 1
root = Tk()
root.title('Butterfly_WallPaper')
root.iconbitmap('Butterfly-PNG-3.ico')
root.minsize(100,200)
root.geometry('450x650')
root.configure(background='dark violet')
files = os.listdir('butterfly_pictures')
img_array = []
for file in files:
    img = Image.open(os.path.join('butterfly_pictures',file))
    resized_img = img.resize((300,500))
    img_array.append(ImageTk.PhotoImage(resized_img))
img_label=Label(root,image = img_array[0])
img_label.pack(pady=(40,40))
text_label=Button(root,text='NEXT',bg='black',fg='white',width=42,height=3,command=change_picture)
text_label.pack(pady=(0,10))
root.mainloop()
