from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from currency_data import live_curr_data
from file_reader import data

options = sorted([i for i in data.keys()])


def currency_calculation(amount, selected_option, target_option):
    try:
        return str(
            float(amount) * (float(live_curr_data[data[target_option]]) / float(live_curr_data[data[selected_option]])))
    except:
        str("")


def initialize_gui():
    window = Tk()

    # set up the geometry of the GUI
    window.title("Currency Converter")
    window.geometry('540x190')

    def comboBox_state_change(event):
        if str(event.widget) == ".!combobox":
            input1.delete(0, 'end')
            input1.insert(0, currency_calculation(input2.get(), clicked2.get(), clicked1.get()))
        if str(event.widget) == ".!combobox2":
            input2.delete(0, 'end')
            input2.insert(0, currency_calculation(input1.get(), clicked1.get(), clicked2.get()))

    def entry_widget_state_change(key):
        if str(key.widget) == ".!entry":
            input1_new_key = key.char
            if str(key.char).isdigit():
                input2.delete(0, 'end')
                input2.insert(0, currency_calculation(input1.get() + input1_new_key, clicked1.get(), clicked2.get()))
            else:
                input2.delete(0, 'end')
                input2.insert(0, currency_calculation(input1.get()[0:-1], clicked1.get(), clicked2.get()))

        if str(key.widget) == ".!entry2":
            input2_new_key = key.char
            if str(key.char).isdigit():
                input1.delete(0, 'end')
                input1.insert(0, currency_calculation(input1.get() + input2_new_key, clicked1.get(), clicked2.get()))
            else:
                input1.delete(0, 'end')
                input1.insert(0, currency_calculation(input1.get()[0:-1], clicked1.get(), clicked2.get()))

    # labels for inputting the amounts
    input1 = Entry(window, width=20, justify="left")
    input1.place(x=15, y=150, anchor="sw")
    input1.bind("<Key>", entry_widget_state_change)
    input2 = Entry(window, width=20, justify="left")
    input2.place(x=15, y=180, anchor="sw")
    input2.bind("<Key>", entry_widget_state_change)

    # set the data type of the labels+dropdown menu
    clicked1 = StringVar()
    clicked2 = StringVar()

    # initial menu text
    clicked1.set("Euro")
    input1.insert(0, live_curr_data[data["Euro"]])
    clicked2.set("United States Dollar")
    input2.insert(0, live_curr_data[data["United States Dollar"]])

    # Create Dropdown menus
    drop1 = ttk.Combobox(window, width=26, textvariable=clicked1)
    drop1['values'] = options
    drop1.place(x=150, y=151, anchor="sw")
    drop1.bind("<<ComboboxSelected>>", comboBox_state_change)
    drop2 = ttk.Combobox(window, width=26, textvariable=clicked2)
    drop2['values'] = options
    drop2.place(x=150, y=181, anchor="sw")
    drop2.bind("<<ComboboxSelected>>", comboBox_state_change)

    def switch_btn_click():
        temp = StringVar()
        temp_input = StringVar()
        temp.set(clicked1.get())
        temp_input.set(input1.get())
        clicked1.set(clicked2.get())
        input1.delete(0, 'end')
        input1.insert(0, input2.get())
        clicked2.set(temp.get())
        input2.delete(0, 'end')
        input2.insert(0, temp_input.get())

    # putting image in the switch currency button
    image = Image.open("images/icon-rotate-13.jpg")
    btn_img = ImageTk.PhotoImage(image.resize((20, 20)))

    # creating the switch currency button
    btn = Button(window, image=btn_img, command=switch_btn_click)
    btn.place(x=283, y=108, anchor="center")

    window.mainloop()


if __name__ == '__main__':
    initialize_gui()
