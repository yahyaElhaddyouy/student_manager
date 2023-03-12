import display as dis
import customtkinter


def log():
    import tkinter
    from tkinter import messagebox
   
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    
    window = customtkinter.CTk()
    window.title("Login form")
    window.geometry('550x430')  
    # window.configure(bg='#333333')

    def login():
        username = "gingo"
        password = "12345"
        if username_entry.get()==username and password_entry.get()==password:
            # messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            dis.display()
            frame.pack_forget()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    frame = tkinter.Frame()


    
    # Creating widgets
    login_button = customtkinter.CTkButton(window,text='login',command=login,hover=True)
    label = customtkinter.CTkLabel(window,text='Login',font=('Arial',30))
    username_label = customtkinter.CTkLabel(window,text='Username',font=('Arial',16))
    password_label = customtkinter.CTkLabel(window,text='Password',font=('Arial',16))
    password_entry = customtkinter.CTkEntry(master=window,
                               placeholder_text="Password",
                               width=150,
                               height=27,
                               border_width=2,
                               corner_radius=10,
                               show='*')
    username_entry = customtkinter.CTkEntry(master=window,
                               placeholder_text="Username",
                               width=150,
                               height=27,
                               border_width=2,
                               corner_radius=10)
    
    # Placing widgets on the screen
    label.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
    login_button.place(relx=0.7, rely=0.76, )
    username_label.place(relx=0.2,rely=0.3)
    password_label.place(relx=0.2,rely=0.45)
    username_entry.place(relx=0.4,rely=0.31)
    password_entry.place(relx=0.4,rely=0.45)
    frame.pack()

    window.mainloop()