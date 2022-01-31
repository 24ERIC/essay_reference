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


        self.reference_type_input = tk.OptionMenu(frame, tk.StringVar(),
                                            "Book = lastname, Initials. (year). title. edition. publisher.", 
                                            "Ebook = lastname, Initials. (Year). title. publisher. URL ", 
                                            "online article = Last name, Initials. (Year, Month Day). Article title. Publication Name. URL")
        self.reference_type_input.config(font=BOLD, bg="black",fg="white", width=17)
        self.reference_type_input["menu"].config(bg="black", fg="white")
        self.reference_type_input.grid(column=3, row=0)



        self.search_textBox = tk.Text(width=300, height=35, bg="black", fg="cyan", insertbackground="cyan")
        self.search_textBox.place(x=10,y=200)
        
        # self.assign_value()
        
        self.addButton = tk.Button(self.frame, text = "Add", command = self.add, bg="black", fg="orange", font=BOLD).grid(column=6, row=2)

        self.searchButton = tk.Button(self.frame, text = "Search", command = self.search, bg="black", fg="orange", font=BOLD).grid(column=6, row=4)
    
    
    def assign_value(self):
        """[summary]
        """
        self.name = self.name_input.get()
        self.year = self.year_input.get()
        self.title = self.title_input.get()
        self.publisher= self.publisher_input.get()
        self.URL = self.URL_input.get()
        self.reference_type = tk.StringVar().get()
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
        
        with open("/home/eric/Documents/__testing__  essay_reference/Reference_Note.csv", 'a') as f:
            self.row_data = "\n"+ \
                            self.name + ", " + \
                            self.year + ", " + \
                            self.title + ", " + \
                            self.publisher + ", " + \
                            self.URL + ", " + \
                            self.reference_type + ", " + \
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
        df = pd.read_csv("/home/eric/Documents/__testing__  essay_reference/Reference_Note.csv")
        pd.set_option('display.max_columns', None)
        
        self.search_textBox.insert(tk.END, df[-1:])

        
    def search(self):
        """Search data in the data set
        """
        self.assign_value()
        
        df = pd.read_csv("/home/eric/Documents/__testing__  essay_reference/Reference_Note.csv")
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
                             "create_tim", 
                             "modified_tim", 
                             "apa_referenc", 
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
        for key, value in zip(self.row_data_key, self.row_data_value):
            self.clear_entry()
            self.search_textBox.insert(tk.END, df.loc[df[::-1].loc[df[key] == value].index[:]])

    
    def get_apa(self):
        
        
        self.apa_reference = "apar"
        self.apa_intext_citation = "apa"




if __name__ == "__main__":
     
    frame = tk.Tk()
    manager = Manager(frame)
    frame.title("Manager")
    frame.geometry('1600x1000')
    frame.configure(background="black")
    
    frame.mainloop()
