from optparse import Option
import tkinter as tk
from tkinter.font import BOLD
import pandas as pd
import time

class Manager:
    """[summary]
    """
    def __init__(self, frame=None):
        """[summary]

        Args:
            frame ([type], optional): [description]. Defaults to None.
        """
        self.frame = frame
        
        self.interface()
        
    def interface(self):
        """[summary]
        """
        self.name_label = tk.Label(font=BOLD, text = "F, L name", bg = "black", fg="white").grid(column=0, row=0)
        self.year_labal = tk.Label(font=BOLD, text = "Year", bg = "black", fg="white").grid(column=0, row=1)
        self.title_labal = tk.Label(font=BOLD, text = "Title", bg = "black", fg="white").grid(column=0, row=2)
        self.publisher_labal = tk.Label(font=BOLD, text = "Publisher", bg = "black", fg="white").grid(column=0, row=3)
        self.URL_labal = tk.Label(font=BOLD, text = "URL", bg = "black", fg="white").grid(column=0, row=4)
        self.reference_type_labal = tk.Label(font=BOLD, text = "Reference Type", bg = "black", fg="white").grid(column=2, row=0)
        self.keyword_labal = tk.Label(font=BOLD, text = "Keyword", bg = "black", fg="white").grid(column=2, row=1)
        self.page_labal = tk.Label(font=BOLD, text = "Page", bg = "black", fg="white").grid(column=2, row=2)
        self.authority_labal = tk.Label(font=BOLD, text = "Authority", bg = "black", fg="white").grid(column=2, row=3)
        self.content_labal = tk.Label(font=BOLD, text = "Content", bg = "black", fg="white").grid(column=2, row=4)


        self.name_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
        self.name_input.grid(column=1, row=0)
        self.year_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
        self.year_input.grid(column=1, row=1)
        self.title_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
        self.title_input.grid(column=1, row=2)
        self.publisher_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
        self.publisher_input.grid(column=1, row=3)
        self.URL_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
        self.URL_input.grid(column=1, row=4)
        self.keyword_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
        self.keyword_input.grid(column=3, row=1)
        self.page_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
        self.page_input.grid(column=3, row=2)
        self.authority_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
        self.authority_input.grid(column=3, row=3)
        self.content_input = tk.Entry(font=BOLD, background="black",fg="white", insertbackground="cyan")
        self.content_input.grid(column=3, row=4)

            
        Options = tk.StringVar()
        self.reference_type_input = tk.OptionMenu(frame, Options,
                                            "Book = lastname; Initials. (y). title. publisher.", 
                                            "Ebook = lastname; Initials. (y). title. publisher. URL.", 
                                            "online article = lastname; Initials. (Y; M D). title. publisher. URL.", command=self.callback)
        self.reference_type_input.config(font=BOLD, bg="black",fg="white", width=17)
        self.reference_type_input["menu"].config(bg="black", fg="white")
        self.reference_type_input.grid(column=3, row=0)
        Options.set("hello")



        self.search_textBox = tk.Text(width=300, height=35, bg="black", fg="cyan", insertbackground="cyan")
        self.search_textBox.place(x=10,y=200)
        
        # self.assign_value()
        
        self.addButton = tk.Button(self.frame, text = "Add", command = self.add, bg="black", fg="orange", font=BOLD).grid(column=6, row=2)

        self.searchButton = tk.Button(self.frame, text = "Search", command = self.search, bg="black", fg="orange", font=BOLD).grid(column=6, row=4)
    
    
    def callback(self,selection):
        """[summary]

        Args:
            selection ([type]): [description]
        """
        self.reference_type = selection
    
    
    def assign_value(self):
        """[summary]
        """
        self.name = self.name_input.get()
        self.year = self.year_input.get()
        self.title = self.title_input.get()
        self.publisher= self.publisher_input.get()
        self.URL = self.URL_input.get()
        self.keyword = self.keyword_input.get()
        self.page = self.page_input.get()
        self.authority = self.authority_input.get()
        self.content = self.content_input.get()
        
        self.create_time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
        self.modified_time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
        self.get_apa()
    

    def clear_entry(self):
        """[summary]
        """
        self.name_input.delete(0,tk.END)
        self.year_input.delete(0,tk.END)
        self.title_input.delete(0,tk.END)
        self.publisher_input.delete(0,tk.END)
        self.URL_input.delete(0,tk.END)
        # reference_type_input
        self.keyword_input.delete(0,tk.END)
        self.page_input.delete(0,tk.END)
        self.authority_input.delete(0,tk.END)
        self.content_input.delete(0,tk.END)
        

    def add(self):
        """Add data into Reference_Note.csv file.
        """
        self.assign_value()
        with open("Reference_Note.csv", 'a') as f:
            self.row_data = "\n"+ \
                            self.name + ", " + \
                            self.year + ", " + \
                            self.title + ", " + \
                            self.publisher + ", " + \
                            self.URL + ", " + \
                            self.reference_type.split(" = ")[0] + ", " + \
                            self.keyword + ", " + \
                            self.page + ", " + \
                            self.authority + ", " + \
                            self.content + ", " + \
                            self.create_time + ", " + \
                            self.modified_time + ", " + \
                            self.apa_reference + ", " + \
                            self.apa_intext_citation
            f.write(self.row_data)
            
            
        self.successfulLabel = tk.Label(frame, text = "Successful", bg="black", fg="cyan", font=BOLD)
        self.successfulLabel.grid(column=6, row=3)
        self.successfulLabel.after(1000, self.successfulLabel.destroy)
        
        self.clear_entry()
        
        # clear data and insert data just added in search_textBox
        self.search_textBox.delete('1.1',tk.END)
        df = pd.read_csv("Reference_Note.csv")
        # pd.set_option('display.max_columns', None)
        
        self.search_textBox.insert(tk.END, df[-1:])

        
    def search(self):
        """Search data in the data set
        """
        self.assign_value()
        
        df = pd.read_csv("Reference_Note.csv", names=["name", "year", "title", "publisher", "URL", "reference_type", "keyword", "page", "authority", "content", "create_tim", "modified_tim", "apa_referenc", "apa_intext_citation"])
        # pd.set_option('display.max_columns', None)
        self.search_textBox.delete('1.1',tk.END)
        
        self.row_data_key = ["name", 
                             "year", 
                             "title", 
                             "publisher", 
                             "URL", 
                             "reference_type", 
                             "keyword", 
                             "page", 
                             "authority", 
                             "content", 
                             "create_time", 
                             "modified_time", 
                             "apa_reference", 
                             "apa_intext_citation"
                              ]
        self.row_data_value = [self.name, 
                               self.year, 
                               self.title, 
                               self.publisher, 
                               self.URL, 
                               self.reference_type, 
                               self.keyword, 
                               self.page, 
                               self.authority, 
                               self.content, 
                               self.create_time, 
                               self.modified_time, 
                               self.apa_reference, 
                               self.apa_intext_citation
                               ] 
        self.clear_entry()
        if self.name != "":
            self.search_textBox.insert(tk.END, df.loc[df[::-1].loc[df["value"] == self.value].index[:]])
        if self.year != "":
            self.search_textBox.insert(tk.END, df[df["year"].str.contains(self.year)])
        if self.title != "":
            self.search_textBox.insert(tk.END, df[df["title"].str.contains(self.title)])
        if self.publisher != "":
            self.search_textBox.insert(tk.END, df[df["publisher"].str.contains(self.publisher)])
        if self.URL != "":
            self.search_textBox.insert(tk.END, df[df["URL"].str.contains(self.URL)])
        if self.reference_type != "":
            self.search_textBox.insert(tk.END, df[df["reference_type"].str.contains(self.reference_type)])
        if self.keyword != "":
            self.search_textBox.insert(tk.END, df[df["keyword"].str.contains(self.keyword)])
        if self.page != "":
            self.search_textBox.insert(tk.END, df[df["page"].str.contains(self.page)])
        if self.authority != "":
            self.search_textBox.insert(tk.END, df[df["authority"].str.contains(self.authority)])
        if self.content != "":
            self.search_textBox.insert(tk.END, df[df["content"].str.contains(self.content)])
        if self.create_time != "":
            self.search_textBox.insert(tk.END, df[df["create_time"].str.contains(self.create_time)])
        if self.modified_time != "":
            self.search_textBox.insert(tk.END, df[df["modified_time"].str.contains(self.modified_time)])
        if self.apa_reference != "":
            self.search_textBox.insert(tk.END, df[df["apa_reference"].str.contains(self.apa_reference)])
        if self.apa_intext_citation != "":
            self.search_textBox.insert(tk.END, df[df["apa_intext_citati"].str.contains(self.apa_intext_citati)])


    
    def get_apa(self):
        """[summary]
        """
        self.name.replace(",", ";")
        self.year.replace(",", ";")
        self.title.replace(",", ";")
        self.publisher.replace(",", ";")
        self.URL.replace(",", ";")
        
        self.apa_reference = ""
        self.apa_intext_citation = ""
        apa_lastname = self.name.split(" ")[-1]
        apa_firstname = self.name.split(" ")[::-1][0]
        if len(self.year) == 4:
            apa_year = self.year.split(" ")[0]
        elif 8 <= len(self.year) <= 10:
            apa_month = self.year.split(" ")[1] 
            apa_day = self.year.split(" ")[2]
        apa_title = self.title
        apa_publisher = self.publisher
        apa_URL = self.URL
        

        if self.reference_type == "Book = lastname; Initials. (y). title. publisher.":
            self.apa_reference = apa_lastname + "; " + apa_firstname + ". " + \
                                 "(" + apa_year + "). " + \
                                 apa_title + ". " + \
                                 apa_publisher + "."
            self.apa_intext_citation = "(" + apa_lastname + "; " + apa_year + ")"
            
        elif self.reference_type == "Ebook = lastname; Initials. (y). title. publisher. URL.":
            self.apa_reference = apa_lastname + "; " + apa_firstname + ". " + \
                                 "(" + apa_year + "). " + \
                                 apa_title + ". " + \
                                 apa_publisher + ". " + \
                                 apa_URL + "."
            self.apa_intext_citation = "(" + apa_lastname + "; " + apa_year + ")"
            
        elif self.reference_type == "online article = lastname; Initials. (Y; M D). title. publisher. URL.":
            self.apa_reference = apa_lastname + "; " + apa_firstname + ". " + \
                                 "(" + apa_year + "; " + apa_month + " " + apa_day + "). " + \
                                 apa_title + ". " + \
                                 apa_publisher + ". " + \
                                 apa_URL + "."
            self.apa_intext_citation = "(" + apa_lastname + ";" + apa_month + " " + apa_day + "; " + apa_year + ")"

    


if __name__ == "__main__":
     
    frame = tk.Tk()
    manager = Manager(frame)
    frame.title("Manager")
    frame.geometry('1600x1000')
    frame.configure(background="black")
    
    frame.mainloop()
