from cProfile import label
from curses.panel import bottom_panel
from re import S
import tkinter as tk
from tkinter.font import BOLD
from turtle import color, width, window_height
from webbrowser import BackgroundBrowser
from click import command
from numpy import size
import pandas as pd
from time import strftime


frame = tk.Tk()
frame.title("Interface")
frame.geometry('1600x1000')
frame.configure(background="black")


# Title 10
title_labal = tk.Label(font=BOLD, text = "Title", bg = "black", fg="white").grid(column=0, row=0)
year_labal = tk.Label(font=BOLD, text = "Year", bg = "black", fg="white").grid(column=0, row=1)
lastname_labal = tk.Label(font=BOLD, text = "Last Name", bg = "black", fg="white").grid(column=0, row=2)
firstname_labal = tk.Label(font=BOLD, text = "First Name", bg = "black", fg="white").grid(column=0, row=3)
content_labal = tk.Label(font=BOLD, text = "Content", bg = "black", fg="white").grid(column=0, row=4)
reference_type_labal = tk.Label(font=BOLD, text = "Reference Type", bg = "black", fg="white").grid(column=2, row=0)
description_labal = tk.Label(font=BOLD, text = "Description", bg = "black", fg="white").grid(column=2, row=1)
authority_labal = tk.Label(font=BOLD, text = "Authority", bg = "black", fg="white").grid(column=2, row=2)
keyword_labal = tk.Label(font=BOLD, text = "Keyword", bg = "black", fg="white").grid(column=2, row=3)
publisher_labal = tk.Label(font=BOLD, text = "Publisher", bg = "black", fg="white").grid(column=2, row=4)






title_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
title_input.grid(column=1, row=0)
year_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
year_input.grid(column=1, row=1)
lastname_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
lastname_input.grid(column=1, row=2)
firstname_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
firstname_input.grid(column=1, row=3)
content_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
content_input.grid(column=1, row=4)
# reference_type_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=3, row=0)

description_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
description_input.grid(column=3, row=1)

authority_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
authority_input.grid(column=3, row=2)

keyword_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
keyword_input.grid(column=3, row=3)

publisher_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
publisher_input.grid(column=3, row=4)


reference_type_input = tk.OptionMenu(frame, tk.StringVar(),"Yellow", "Pink", "RED", "Brown", "Black", "Blue")
reference_type_input.config(font=BOLD, bg="black",fg="white", width=17)
reference_type_input["menu"].config(bg="black", fg="white")
reference_type_input.grid(column=3, row=0)


search_textBox = tk.Text(width=180, height=35, bg="black", fg="cyan", insertbackground="cyan")
search_textBox.place(x=10,y=200)


############################################################################################

def get_apa():
    title = title_input.get()
    year = year_input.get()
    lastname = lastname_input.get()
    firstname= firstname_input.get()
    content = content_input.get()
    reference_type = tk.StringVar().get()
    description = description_input.get()
    authority = authority_input.get()
    keyword = keyword_input.get()
    publisher = publisher_input.get()
    
    apa = ""
    return apa

def add():
    """Add data into Reference_Note.csv file.
    """
    title = title_input.get()
    year = year_input.get()
    lastname = lastname_input.get()
    firstname= firstname_input.get()
    content = content_input.get()
    reference_type = tk.StringVar().get()
    description = description_input.get()
    authority = authority_input.get()
    keyword = keyword_input.get()
    publisher = publisher_input.get()
    # 
    create_time = str(strftime("%Y-%m-%d %H:%M:%S"))
    modified_time = str(strftime("%Y-%m-%d %H:%M:%S"))
    apa = get_apa()
    
    with open("/home/eric/Documents/__testing__  essay_reference/Reference_Note.csv", 'a') as f:
        row_data = "\n"+ title+", "+year+", "+lastname+", "+firstname+", "+content+", "+reference_type+", "+description+", "+authority+", "+keyword+", "+publisher+", "+create_time+", "+modified_time+", "+apa
        f.write(row_data)
    
    title_input.delete(0,tk.END)
    year_input.delete(0,tk.END)
    lastname_input.delete(0,tk.END)
    firstname_input.delete(0,tk.END)
    content_input.delete(0,tk.END)
    # reference_type_input
    description_input.delete(0,tk.END)
    authority_input.delete(0,tk.END)
    keyword_input.delete(0,tk.END)
    publisher_input.delete(0,tk.END)
    
    successLabel = tk.Label(frame, text = "Successful", bg="black", fg="cyan", font=BOLD).grid(column=6, row=3)
    
    

def search():
    """Search data in the data set
    """
    title = title_input.get()
    year = year_input.get()
    lastname = lastname_input.get()
    firstname= firstname_input.get()
    content = content_input.get()
    reference_type = tk.StringVar().get()
    description = description_input.get()
    authority = authority_input.get()
    keyword = keyword_input.get()
    publisher = publisher_input.get()
    # 
    create_time = str(strftime("%Y-%m-%d %H:%M:%S"))
    modified_time = str(strftime("%Y-%m-%d %H:%M:%S"))
    apa = get_apa()
    
    
    df = pd.read_csv("/home/eric/Documents/__testing__  essay_reference/Reference_Note.csv")
    search_textBox.insert(tk.END, df)
    pass


# add button
addButton = tk.Button(frame, text = "Add", command = add, bg="black", fg="orange", font=BOLD).grid(column=6, row=2)

searchButton = tk.Button(frame, text = "Search", command = search, bg="black", fg="orange", font=BOLD).grid(column=6, row=4)






frame.mainloop()
