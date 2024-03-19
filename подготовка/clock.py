from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.geometry('300x300')
photo = Image.open('C:\кухарев\-----------------main\подготовка\icon_clock.png')
resize_photo = photo.resize((50, 50))
photo = ImageTk.PhotoImage(resize_photo)
window.iconbitmap()
window.title('Будильник')
window.resizable(False, False)

bt = Button(window,
            height = 50,
            image = photo,
            )
bt.place(x = 100,
         )

window.mainloop()