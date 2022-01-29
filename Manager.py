from cProfile import label
import tkinter as tk
from turtle import color
import pandas as pd

frame = tk.Tk()
frame.title("Interface")
frame.geometry('1600x1000')
frame.configure(background="black")


# Title 10
title_labal = tk.Label(frame, text = "Title")
year_labal = tk.Label(frame, text = "Year")
lastname_labal = tk.Label(frame, text = "Last Name")
firstname_labal = tk.Label(frame, text = "First Name")
content_labal = tk.Label(frame, text = "Content")
reference_type_labal = tk.Label(frame, text = "Reference Type")
description_labal = tk.Label(frame, text = "Description")
authority_labal = tk.Label(frame, text = "Authority")
keyword_labal = tk.Label(frame, text = "Keyword")
publisher_labal = tk.Label(frame, text = "Publisher")



title_labal.grid(column=0, row=0)
year_labal.grid(column=0, row=1)
lastname_labal.grid(column=0, row=2)
firstname_labal.grid(column=0, row=3)
content_labal.grid(column=0, row=4)
reference_type_labal.grid(column=2, row=0)
description_labal.grid(column=2, row=1)
authority_labal.grid(column=2, row=2)
keyword_labal.grid(column=2, row=3)
publisher_labal.grid(column=2, row=4)


title_input = tk.Entry()
year_input = tk.Entry()
lastname_input = tk.Entry()
firstname_input = tk.Entry()
content_input = tk.Entry()
reference_type_input = tk.Entry()
description_input = tk.Entry()
authority_input = tk.Entry()
keyword_input = tk.Entry()
publisher_input = tk.Entry()


title_input.grid(column=1, row=0)
year_input.grid(column=1, row=1)
lastname_input.grid(column=1, row=2)
firstname_input.grid(column=1, row=3)
content_input.grid(column=1, row=4)
reference_type_input.grid(column=3, row=0)
description_input.grid(column=3, row=1)
authority_input.grid(column=3, row=2)
keyword_input.grid(column=3, row=3)
publisher_input.grid(column=3, row=4)

title_input.config(state=tk.NORMAL, font=10,fg="white")
year_input.config(state=tk.NORMAL, font=10, fg="white")
lastname_input.config(state=tk.NORMAL, font=10, fg="white")
firstname_input.config(state=tk.NORMAL, font=10, fg="white")
content_input.config(state=tk.NORMAL, font=10, fg="white")
reference_type_input.config(state=tk.NORMAL, font=10, fg="white")
description_input.config(state=tk.NORMAL, font=10, fg="white")
authority_input.config(state=tk.NORMAL, font=10, fg="white")
keyword_input.config(state=tk.NORMAL, font=10, fg="white")
publisher_input.config(state=tk.NORMAL, font=10, fg="white")

title_input.configure(background="black")
year_input.configure(background="black")
lastname_input.configure(background="black")
firstname_input.configure(background="black")
content_input.configure(background="black")
reference_type_input.configure(background="black")
description_input.configure(background="black")
authority_input.configure(background="black")
keyword_input.configure(background="black")
publisher_input.configure(background="black")


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

addButton = tk.Button(frame,
                        text = "Add", 
                        command = add)
addButton.grid(column=6, row=2)




# successLabel = tk.Label(frame, text = "")
# successLabel.grid(column=6, row=3)



frame.mainloop()
