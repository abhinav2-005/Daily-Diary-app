import datetime
import tkinter as tk
from sql import *
from tkinter import messagebox


class Main():

    def background(self):
        self.bg = tk.Tk()
        self.bg.geometry("500x500")
        self.bg.title("Dialy Diary app")
        self.title = tk.Label(self.bg,text="Welcome to Daily Diary app",font=("Times New Romean",20))

        def new_entry():
            def new_entry_operation():
                information = self.entry1.get()
                con1 = s.get_connectoin()
                cursor = con1.cursor()
                quary = f"INSERT INTO new_entry(date,info) values(%s,%s)"
                data = (date,information)
                cursor.execute(quary,data)
                con1.commit()
                cursor.close()
                con1.close()
                messagebox.showinfo("Success","Done")
                self.new_entry_bg.destroy()
       
            self.new_entry_bg = tk.Tk()
            self.new_entry_bg.geometry("500x500")
            self.new_entry_bg.title("New Entry")
            self.label1 = tk.Label(self.new_entry_bg,text="New entry",font=("Times New Roman",15))
            self.label1.pack()
            self.label2 = tk.Label(self.new_entry_bg,text="Dear diary,")
            self.label2.place(x = 0,y = 50)
            self.label3 = tk.Label(self.new_entry_bg,text="-------------------------------------------------------------------------------")
            self.label3.place(x = 0,y = 75)
            date = datetime.date.today()
            time = str(datetime.datetime.now())[10:16].strip()
            self.label4 = tk.Label(self.new_entry_bg,text=f"{date}")
            self.label4.place(x = 0,y = 100)
            self.label5 = tk.Label(self.new_entry_bg,text=f"{time}")
            self.label5.place(x = 0,y = 115)
            self.entry1 = tk.Entry(self.new_entry_bg,width=20)
            self.entry1.place(x=0,y =150,width=490,height=300)
            self.button1 = tk.Button(self.new_entry_bg,text="Submit",command=new_entry_operation)
            self.button1.place(x = 185,y = 470)
            self.new_entry_bg.mainloop()

        def previous_entry():
            def previous_operation():
                date = entry.get()
                con2 = s.get_connectoin()
                cursor2 = con2.cursor()
                quary2 = "SELECT info FROM new_entry where date = %s"
                cursor2.execute(quary2,(date,))
                info = cursor2.fetchall()
                con2.commit()
                cursor2.close()
                con2.close()
            
                if len(info) >= 1:
                    flabel = tk.Label(self.bg,text=info[0][0],font=("TImes New Roman",10))
                    flabel.place(x = 120,y = 200)
                    label1 = tk.Label(self.bg,text=f"{date}:",font=("Times New ROman",10))
                    label1.place(x = 50,y = 200)
                else:
                    messagebox.showinfo("Error","No previous Entries")
            label1 = tk.Label(self.bg,text="Enter Date",font=("Times New Roman",10))
            label1.place(x = 50,y=120)

            entry = tk.Entry(self.bg,width=25)
            entry.place(x=130,y=120)

            button = tk.Button(self.bg,text="Done",command=previous_operation)
            button.place(x=310,y=120)
        
        def delete_entry():
                def delete_operation():
                    date = entry.get()
                    con3 = s.get_connectoin()
                    cursor3 = con3.cursor()
                    quary3 = "DELETE FROM  new_entry where date = %s"
                    cursor3.execute(quary3,(date,))
                    con3.commit()
                    cursor3.close()
                    con3.close()
                    messagebox.showinfo("Success","Successfully Deleted")

                label1 = tk.Label(self.bg,text="Enter Date",font=("Times New ROman",10))
                label1.place(x = 50,y = 120)

                entry = tk.Entry(self.bg,width=25)
                entry.place(x=130,y=120)

                button = tk.Button(self.bg,text="Done",command=delete_operation)
                button.place(x=310,y=120)

        self.button1 = tk.Button(self.bg,text="Add New Entry",command=new_entry)
        self.button1.place(x=100,y=50)
        self.button2 = tk.Button(self.bg,text="View Previous Entry",command=previous_entry)
        self.button2.place(x=200,y=50)
        self.button3 = tk.Button(self.bg,text="Delete an Entry",command=delete_entry)
        self.button3.place(x=325,y=50)
        self.title.pack()
        self.loop()


    def loop(self):
        self.bg.mainloop()

m = Main()
m.background()