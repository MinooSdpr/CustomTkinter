
# https://customtkinter.tomschimansky.com/documentation/

from customtkinter import *
def clear_checkbox():
    check.deselect()
    show_text.set('Not good ok?')
def select():
    check.select()
    show_text.set("Well... I'm good now")
window = CTk()
window.geometry('500x300')
state=StringVar(value='yes')
show_text = StringVar(value='Feel good?')
check=CTkCheckBox(window,textvariable=show_text,onvalue='yes',
                  offvalue='no',variable=state)
check.pack(pady=20)
btn_clear = CTkButton(window,text='clear',command=clear_checkbox)
btn_clear.pack()
btn_select = CTkButton(window,text='select',command=select)
btn_select.pack(pady=17)

window.mainloop()