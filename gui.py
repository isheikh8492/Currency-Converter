import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from currency_data import live_curr_data
from file_reader import data
import urllib.request
from tkinter import Tk
import dateutil.relativedelta
import datetime
import urllib.request
import json
import dateutil.relativedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import tkinter as tkr
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

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
    window.geometry('600x210')

    def graph():
        target_currency = str(data[clicked2.get()])
        init_currency = str(data[clicked1.get()])
        start_date = datetime.date.today()
        end_date = start_date + dateutil.relativedelta.relativedelta(months=-1)
        delta = datetime.timedelta(days=1)
        y_values = []
        while end_date <= start_date:
            with urllib.request.urlopen("http://data.fixer.io/api/" + str(
                    end_date) + "?access_key=2179433ad61d935639f9bc75e180bdf0&base=EUR&symbols=" + init_currency + "," + target_currency) as url:
                json_data = json.loads(url.read().decode())
                y_values.append((float(json_data['rates'][target_currency]) / float(json_data['rates'][init_currency])))
                end_date += delta
        start_date = datetime.date.today()
        end_date = start_date + dateutil.relativedelta.relativedelta(months=-1)
        x_values = []
        while end_date <= start_date:
            x_values.append(end_date)
            end_date += delta

        # ax = plt.gca()
        # formatter = mdates.DateFormatter("%Y-%m-%d")
        # ax.xaxis.set_major_formatter(formatter)
        # locator = mdates.DayLocator()
        # ax.xaxis.set_major_locator(locator)
        # x_ticks = np.arange(x_values[len(x_values) - 1], x_values[0], datetime.timedelta(days=-15))
        # plt.xticks(x_ticks)
        # plt.plot(x_values, y_values)

        fig = plt.Figure(figsize=(3, 2), dpi=75)
        ax = fig.add_subplot(111)
        ax.plot(x_values, y_values)
        ax.set_xticks(np.arange(x_values[len(x_values) - 1], x_values[0], datetime.timedelta(days=-15)))
        fig.tight_layout()
        chart = FigureCanvasTkAgg(fig, window)
        chart.get_tk_widget().place(x=370, y=20, anchor="nw")

    def head_line():
        var = StringVar()
        small_label = Label(window, textvariable=var, font="none 10")
        var.set("1 " + clicked1.get() + " is equal to ")
        small_label.place(x=10, y=10, anchor="nw")
        l_var = StringVar()
        large_label = Label(window, textvariable=l_var, font="none 25")
        l_var.set(
            str(round(float(live_curr_data[data[clicked2.get()]]) / float(live_curr_data[data[clicked1.get()]]), 4)))
        large_label.place(x=10, y=35, anchor="nw")
        cl_var = StringVar()
        c_large_label = Label(window, textvariable=cl_var, font="none 20")
        cl_var.set(clicked2.get())
        c_large_label.place(x=10, y=85, anchor="nw")

    def comboBox_state_change(event):
        if str(event.widget) == ".!combobox":
            input1.delete(0, 'end')
            input1.insert(0, currency_calculation(input2.get(), clicked2.get(), clicked1.get()))
        if str(event.widget) == ".!combobox2":
            input2.delete(0, 'end')
            input2.insert(0, currency_calculation(input1.get(), clicked1.get(), clicked2.get()))
        head_line()
        graph()

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
                input1.insert(0, currency_calculation(input2.get() + input2_new_key, clicked2.get(), clicked1.get()))
            else:
                input1.delete(0, 'end')
                input1.insert(0, currency_calculation(input2.get()[0:-1], clicked2.get(), clicked1.get()))

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

    head_line()
    graph()

    window.mainloop()


if __name__ == '__main__':
    initialize_gui()
