from customtkinter import *
from tkinter.messagebox import showinfo
def check_btn():
    text=name.get()
    showinfo(f'عددی که وارد کردید{text}است')
def delete_age():
    name.delete(0,END)
window = CTk()
window.geometry('500x300')
myfont = CTkFont(family='B Yekan',size=24,weight='bold')
lbl_name=CTkLabel(window,text='چه عددی در ذهن شماست؟',font=myfont)
name = CTkEntry(window,corner_radius=7,width=100,placeholder_text='number')
btn = CTkButton(window,text='تشخیص بده',font=myfont,corner_radius=10,command=check_btn)
del_btn = CTkButton(window,text='پاک کردن',font=myfont,corner_radius=10,command=delete_age)
lbl_name.pack(pady=10)
name.pack(pady=19)
btn.pack(pady=20)
del_btn.pack()
window.mainloop()