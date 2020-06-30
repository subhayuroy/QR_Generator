from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

window = Tk()
window.title("QR Code Generator")

def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrImage = myQr.xbm(scale=6)
        global photo
        photo = BitmapImage(data=qrImage)
    else:
        messagebox.showinfo("Error!", "Please enter the subject")
    try:
        showCode()
    except:
        pass

def showCode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="Showing QR code for: " + subject.get())

def save():
    dir = path1 = os.getcwd() + "\\QR Codes" #folder to save all teh codes
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qrImage = myQr.png(os.path.join(dir, name.get() + ".png"), scale=6)
        else:
            messagebox.showinfo("Error!", "Filename cannot be empty")
    except:
        messagebox.showinfo("Error!", "Please generate the code first")
