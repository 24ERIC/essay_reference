from cProfile import label
import tkinter as tk
from tkinter.font import BOLD
from turtle import color
import pandas as pd

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





title_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=1, row=0)
year_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=1, row=1)
lastname_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=1, row=2)
firstname_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=1, row=3)
content_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=1, row=4)
reference_type_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=3, row=0)
description_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=3, row=1)
authority_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=3, row=2)
keyword_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=3, row=3)
publisher_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan").grid(column=3, row=4)






############################################################################################

def add():
    """Add data into Reference_Note.csv file.
    """
    title = title_input.get(1.0, "end-1c")
    year = year_input.get(1.0, "end-1c")
    lastname = lastname_input.get(1.0, "end-1c")
    firstname= firstname_input.get(1.0, "end-1c")
    content = content_input.get(1.0, "end-1c")
    reference_type = reference_type_input.get(1.0, "end-1c")
    description = description_input.get(1.0, "end-1c")
    authority = authority_input.get(1.0, "end-1c")
    keyword= keyword_input.get(1.0, "end-1c")
    publisher= publisher_input.get(1.0, "end-1c")
    with open("Reference_Note.csv", 'a') as f:
        f.write( "\n"+title+", "+year+", "+lastname+", "+firstname+", "+content+", "+reference_type+", "+description+", "+authority+", "+keyword+", "+publisher)
    
    
def get_apa():
    pass



# add button

addButton = tk.Button(frame,text = "Add", command = add, bg="black", fg="orange", font=BOLD).grid(column=6, row=2)




# successLabel = tk.Label(frame, text = "")
# successLabel.grid(column=6, row=3)



frame.mainloop()
