from tkinter import PhotoImage, filedialog
from PIL import Image, ImageTk
import qrcode
import tkinter as tk

window=tk.Tk()
window.geometry("600x500")
window.configure(bg="#9CA13A")
window.resizable(False,False)
qr=qrcode.QRCode(
    version=5,
    box_size=10,
    border=5
)

def browse():
    try:
        myFile = filedialog.asksaveasfile(mode='wb', defaultextension='.png')
        img.save(myFile)
        L2=tk.Label(window,text="Successfully Downloaded",font=(25))
        L2.place(x=100,y=450)
        
    except:
        L2=tk.Label(window, text="Error",font=(25))
        L2.place(x=100,y=450)

def generate():
    global img
    qr.add_data(dt.get())
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    img1=img.resize((260,260))
    img1=ImageTk.PhotoImage(img1)
    Lab=tk.Label(window,image=img1)
    Lab.place(x=100,y=120)
    b2=tk.Button(window, text="Download",width=8,height=1,font=(25),command=browse)
    b2.place(x=190,y=400)
    b2.configure(bg="darkgreen")
    qr.clear()
    img1.save()
    
l1=tk.Label(window, text="Enter the data",font=(25))
l1.place(x=0,y=25)
dt=tk.Entry(window,font=(25),width=30)
dt.place(x=150,y=25)
b1=tk.Button(window, text="Submit",command=generate)
b1.place(x=200,y=60)

window.mainloop()