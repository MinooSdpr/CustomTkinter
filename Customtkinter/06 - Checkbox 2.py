from customtkinter import *
def check_gender():
    if male.get()=='male':
        female.deselect()
    if female.get()=='female':
        male.deselect()
window = CTk()
window.geometry('500x500')
male = CTkCheckBox(window,onvalue='male',offvalue='off',text='male',
                   command=check_gender)
female = CTkCheckBox(window,onvalue='female',offvalue='off',text='female',
                     command=check_gender)
male.pack(side=RIGHT)
female.pack(side=RIGHT)

window.mainloop()