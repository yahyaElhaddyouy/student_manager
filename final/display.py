import tkinter
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    
window = customtkinter.CTk()
window.title("display form")
window.geometry('550x430')

add_user_img = customtkinter.CTkImage(light_image=Image.open("./assets/icons/add_user1.png"),
                                  dark_image=Image.open("./assets/icons/add_user1.png"),
                                  size=(20, 20))
edit_user_img = customtkinter.CTkImage(light_image=Image.open("./assets/icons/edit_user1.png"),
                                  dark_image=Image.open("./assets/icons/edit_user1.png"),
                                  size=(20, 20))
remove_user_img = customtkinter.CTkImage(light_image=Image.open("./assets/icons/delete_user.png"),
                                  dark_image=Image.open("./assets/icons/delete_user.png"),
                                  size=(20, 20))
show_user_img = customtkinter.CTkImage(light_image=Image.open("./assets/icons/show_user.png"),
                                  dark_image=Image.open("./assets/icons/show_user.png"),
                                  size=(20, 20))
    
dis = tkinter.Frame(bg='#333333')
button_add=  customtkinter.CTkButton(dis,text='Add student',hover=True,image=add_user_img)
button_del =  customtkinter.CTkButton(dis,text='Delete student',hover=True,image=remove_user_img)
button_mod =  customtkinter.CTkButton(dis,text='Edit student',hover=True,image=edit_user_img)
button_show =  customtkinter.CTkButton(dis,text='Show student',hover=True,image=show_user_img)
button_add.place(relx=0.5, rely=0.3,anchor=tkinter.CENTER)
button_del.place(relx=0.5, rely=0.4,anchor=tkinter.CENTER)
button_mod.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)
button_show.place(relx=0.5, rely=0.6,anchor=tkinter.CENTER)           
dis.pack(fill='both',expand=1)
    
window.mainloop()