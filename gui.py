from tkinter import *
from file_reader import data
from PIL import ImageTk, Image

options = sorted([i for i in data.keys()])


def initialize_gui():
    window = Tk()

    # set up the geometry of the GUI
    window.title("Currency Converter")
    window.geometry('540x190')

    # labels for inputting the amounts
    input1 = Entry(window, width=20, justify="left")
    input1.place(x=15, y=150, anchor="sw")
    input2 = Entry(window, width=20, justify="left")
    input2.place(x=15, y=180, anchor="sw")

    # set the data type of the labels+dropdown menu
    clicked1 = StringVar()
    clicked2 = StringVar()

    # initial menu text
    clicked1.set("United States Dollar")
    clicked2.set("Euro")

    # Create Dropdown menus
    drop1 = OptionMenu(window, clicked1, *options)
    drop1.place(x=150, y=156, anchor="sw")
    drop2 = OptionMenu(window, clicked2, *options)
    drop2.place(x=150, y=186, anchor="sw")

    def swtch_btn_click():
        temp = StringVar()

        temp.set(clicked1.get())
        clicked1.set(clicked2.get())
        clicked2.set(temp.get())




    # putting image in the switch currency button
    image = Image.open("images/icon-rotate-13.jpg")
    btn_img = ImageTk.PhotoImage(image.resize((20, 20)))

    # creating the switch currency button
    btn = Button(window, image=btn_img, command=swtch_btn_click)
    btn.place(x=283, y=108, anchor="center")

    window.mainloop()


if __name__ == '__main__':
    initialize_gui()
