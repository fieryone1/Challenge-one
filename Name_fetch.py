import requests, bs4
import customtkinter as ctk
from PIL import Image,ImageTk
from io import BytesIO
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title=("Name_fetch")
        self.geometry('1000x800')
        
        for i in range(8):
            self.columnconfigure(i, weight=1,uniform='a')
            self.rowconfigure(i, weight=1,uniform='a')

        #create widgets
        self.entry_var=ctk.StringVar()
        self.entry = ctk.CTkEntry(self,textvariable=self.entry_var, placeholder_text="Enter an ID")
        self.entry.grid(row=0, column=0, columnspan=8, padx=20, pady=20, sticky="nsew")

        self.button = ctk.CTkButton(self, text="Fetch Name", command=self.fetch_details)
        self.button.grid(row=1, column=0, columnspan=8, padx=20, pady=20, sticky="nsew")
        
        self.output_text = ctk.CTkLabel(self, height=200,text="enter an id", font=("Arial", 25))
        self.output_text.grid(row=2, column=0, columnspan=8, padx=20, pady=20, sticky="nsew")

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.grid(row=3,rowspan=5, column=1, columnspan=5, padx=20, pady=20, sticky="nsew")
       
        
        self.mainloop()
    def fetch_details(self):
        try:
            soup=bs4.BeautifulSoup(requests.get(f'https://www.ecs.soton.ac.uk/people/{self.entry_var.get()}').text,"lxml") #fetch the page and find the name
            name=soup.head.find('meta', property="og:title")['content']
            
            try:                                                                                #some pages do not have images 
                img_tag=soup.find('img')['src']
                image_url=f'https://www.southampton.ac.uk/{img_tag}'
                image_data=Image.open(BytesIO(requests.get(image_url).content))
                width,height=image_data.size
                aspect_ratio=width/height
                max_height=430
                max_width=max_height*aspect_ratio
                image_data=image_data.resize((int(max_width),max_height),Image.LANCZOS)   
                tk_image=ImageTk.PhotoImage(image_data)
                self.image_label.configure(image=tk_image)
            except:
                self.image_label.configure(image=None)



            
            self.output_text.configure(text=f'{name}\n{self.entry_var.get()}@soton.ac.uk')

        except:
            self.output_text.configure(text="Invalid ID")
            self.image_label.configure(image=None)

App()