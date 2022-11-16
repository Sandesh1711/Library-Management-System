from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter

class Library:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry('1550x800')

        self.member_var=StringVar()
        self.id_var = StringVar()
        self.first_var = StringVar()
        self.last_var = StringVar()
        self.post_var = StringVar()
        self.address_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.borrowed_var = StringVar()
        self.due_var = StringVar()




    #=============Frame================================
        label_title = Label(self.root,text='Library Management System',fg='black',border=12,relief=GROOVE,font=('Aerial',25,'bold'),bg='powder blue')
        label_title.pack(side=TOP,fill=X)

        frame = Frame(self.root,relief=GROOVE,border=7,bg='powder blue')
        frame.place(x=0,y=60,width=1530,height=400)

        data_left_frame=LabelFrame(frame,text='Member Information',fg='black',border=7,relief=GROOVE,font=('Aerial',20,'bold'),bg='powder blue')
        data_left_frame.place(x=0,y=10,width=750,height=370)

        data_right_frame = LabelFrame(frame, text='Book Details', fg='black', border=7, relief=GROOVE,font=('Aerial', 20,'bold'), bg='powder blue')
        data_right_frame.place(x=755, y=10, width=750, height=370)

        button_frame=Frame(self.root,bd=7,bg='powder blue',relief=GROOVE)
        button_frame.place(x=0,y=450,width=1530,height=80)

        details_frame=Frame(self.root,bd=7,relief=GROOVE,bg='powder blue')
        details_frame.place(x=0,y=530,width=1530,height=268)

#==============Label================================================
        member_type= Label(data_left_frame,text='Member Type',fg='black',font=('Aerial',14,'bold'),padx=2,pady=8,bg='powder blue')
        member_type.grid(row=0,column=0)

        id_type = Label(data_left_frame, text='ID No', fg='black', font=('Aerial', 14, 'bold'), padx=2,pady=8, bg='powder blue')
        id_type.grid(row=1, column=0)

        first_type = Label(data_left_frame, text='First Name', fg='black', font=('Aerial', 14, 'bold'), padx=2,pady=8, bg='powder blue')
        first_type.grid(row=2, column=0)

        last_type = Label(data_left_frame, text='Last Name', fg='black', font=('Aerial', 14, 'bold'), padx=2,pady=8, bg='powder blue')
        last_type.grid(row=3, column=0)

        post_type = Label(data_left_frame, text='Post Code', fg='black', font=('Aerial', 14, 'bold'), padx=2,pady=8, bg='powder blue')
        post_type.grid(row=4, column=0)

        address_type = Label(data_left_frame, text='Address', fg='black', font=('Aerial', 14, 'bold'), padx=2,pady=8, bg='powder blue')
        address_type.grid(row=5, column=0)

        mobile_type = Label(data_left_frame, text='Mobile No', fg='black', font=('Aerial', 14, 'bold'), padx=2,pady=8, bg='powder blue')
        mobile_type.grid(row=6, column=0)

        member_type = Label(data_left_frame, text='Book Id', fg='black', font=('Aerial', 14, 'bold'), padx=2,pady=8, bg='powder blue')
        member_type.grid(row=0, column=3)

        id_type = Label(data_left_frame, text='Book Title', fg='black', font=('Aerial', 14, 'bold'), padx=2, pady=8,bg='powder blue')
        id_type.grid(row=1, column=3)

        first_type = Label(data_left_frame, text='Auther Name', fg='black', font=('Aerial', 14, 'bold'), padx=2, pady=8,bg='powder blue')
        first_type.grid(row=2, column=3)

        last_type = Label(data_left_frame, text='Date Borrowed', fg='black', font=('Aerial', 14, 'bold'), padx=2, pady=8,bg='powder blue')
        last_type.grid(row=3, column=3)

        post_type = Label(data_left_frame, text='Date Due', fg='black', font=('Aerial', 14, 'bold'), padx=2, pady=8,bg='powder blue')
        post_type.grid(row=4, column=3)

#============== Entry Field=========================
        member_entry = ttk.Combobox(data_left_frame,font=('Aerial',12,'bold'),width=20,state='readonly',textvariable=self.member_var)
        member_entry['values']=('Admin Staff','Student','Lecture')
        member_entry.grid(row=0,column=1)

        id_entry=Entry(data_left_frame,font=('Aerial',12,'bold'),width=22,textvariable=self.id_var)
        id_entry.grid(row=1,column=1)

        first_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.first_var)
        first_entry.grid(row=2, column=1)

        last_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.last_var)
        last_entry.grid(row=3, column=1)

        post_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.post_var)
        post_entry.grid(row=4, column=1)

        address_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.address_var)
        address_entry.grid(row=5, column=1)

        mobile_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.mobile_var)
        mobile_entry.grid(row=6, column=1)

        bookid_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.bookid_var)
        bookid_entry.grid(row=0, column=4)

        booktitle_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.booktitle_var)
        booktitle_entry.grid(row=1, column=4)

        authername_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.auther_var)
        authername_entry.grid(row=2, column=4)

        borrowdate_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.borrowed_var)
        borrowdate_entry.grid(row=3, column=4)

        duedate_entry = Entry(data_left_frame, font=('Aerial', 12, 'bold'), width=22,textvariable=self.due_var)
        duedate_entry.grid(row=4, column=4)

#====================Button======================================================
        add_button = Button(button_frame,text='ADD',font=('Aerial',20,'bold'),bg='blue',fg='white',padx=2,width=14,command=self.add)
        add_button.grid(row=0,column=0)

        show_button = Button(button_frame, text='SHOW', font=('Aerial', 20, 'bold'), bg='blue', fg='white', padx=2,width=14)
        show_button.grid(row=0, column=1)

        update_button = Button(button_frame, text='UPDATE', font=('Aerial', 20, 'bold'), bg='blue', fg='white', padx=2,width=14,command=self.update)
        update_button.grid(row=0, column=2)

        delete_button = Button(button_frame, text='DELETE', font=('Aerial', 20, 'bold'), bg='blue', fg='white', padx=2,width=14,command=self.delete)
        delete_button.grid(row=0, column=3)

        clear_button = Button(button_frame, text='CLEAR', font=('Aerial', 20, 'bold'), bg='blue', fg='white', padx=2,width=14,command=self.clear)
        clear_button.grid(row=0, column=4)

        exit_button = Button(button_frame, text='EXIT', font=('Aerial', 20, 'bold'), bg='blue', fg='white', padx=2,width=14,command=self.exit)
        exit_button.grid(row=0, column=5)

#=================Info===========================================

        table_frame=Frame(details_frame,bd=7,relief=GROOVE,bg='powder blue')
        table_frame.place(x=0,y=2,width=1510,height=250)

        xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(table_frame,column=('membertype','idno','firstname','lastname','postcode','address','mobileno','bookid','booktitle','authername','dateborrowed','datedue'),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading('membertype',text='Member Type')
        self.library_table.heading('idno', text='Id No')
        self.library_table.heading('firstname', text='First Name')
        self.library_table.heading('lastname', text='Last Name')
        self.library_table.heading('postcode', text='Post Code')
        self.library_table.heading('address', text='Address')
        self.library_table.heading('mobileno', text='Mobile Number')
        self.library_table.heading('bookid', text='Book Id')
        self.library_table.heading('booktitle', text='Book Title')
        self.library_table.heading('authername', text='Auther Name')
        self.library_table.heading('dateborrowed', text='Date Borrowed')
        self.library_table.heading('datedue', text='Date Due')

        self.library_table['show']='headings'
        self.library_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
        curr=conn.cursor()
        curr.execute("insert into data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.id_var.get(),
            self.first_var.get(),
            self.last_var.get(),
            self.post_var.get(),
            self.address_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.borrowed_var.get(),
            self.due_var.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success",'Member has been inserted')

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='library')
        curr=conn.cursor()
        curr.execute("select * from data")
        rows=curr.fetchall()
        if rows!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert('',END,values=i)
                conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row=content['values']
        self.member_var.set(row[0]),
        self.id_var.set(row[1]),
        self.first_var.set(row[2]),
        self.last_var.set(row[3]),
        self.post_var.set(row[4]),
        self.address_var.set(row[5]),
        self.mobile_var.set(row[6]),
        self.bookid_var.set(row[7]),
        self.booktitle_var.set(row[8]),
        self.auther_var.set(row[9]),
        self.borrowed_var.set(row[10]),
        self.due_var.set(row[11])

    def clear(self):
        self.member_var.set(''),
        self.id_var.set(''),
        self.first_var.set(''),
        self.last_var.set(''),
        self.post_var.set(''),
        self.address_var.set(''),
        self.mobile_var.set(''),
        self.bookid_var.set(''),
        self.booktitle_var.set(''),
        self.auther_var.set(''),
        self.borrowed_var.set(''),
        self.due_var.set('')


    def exit(self):
        iexit = tkinter.messagebox.askyesno('Library Management System',"Do you want to exit ?")
        if iexit>0:
            self.root.destroy()
            return


    def update(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='library')
        curr = conn.cursor()
        curr.execute("update data set member_type=%s,first_name=%s,last_name=%s,post_code=%s,address=%s,mobile_no=%s,book_id=%s,book_title=%s,auther_name=%s,date_borrowed=%s,date_due=%s where id_no=%s",
                     (self.member_var.get(),self.first_var.get(),self.last_var.get(),self.post_var.get(),self.address_var.get(),self.mobile_var.get(),self.bookid_var.get(),self.booktitle_var.get(),self.auther_var.get(),self.borrowed_var.get(),self.due_var.get(),self.id_var.get()))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("Success","Member has been updated")


    def delete(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='library')
        curr = conn.cursor()
        query="delete from data where id_no=%s"
        value=(self.id_var.get(),)
        curr.execute(query,value)
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("Success","Member has been deleted.")




if __name__ == '__main__':
    root=Tk()
    obj=Library(root)
    root.mainloop()


