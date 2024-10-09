from customtkinter import *
# def set_color(choice):
#     name.configure(fg_color=choice)
# def chooseTheme(choice):
#     #print(choice)
#     set_appearance_mode(choice)
# window = CTk()
# window.geometry('500x500')
# state=StringVar(value='system')
# modlist = ['dark','light','system']
# combo=CTkComboBox(window,values=modlist,variable=state,command=chooseTheme)
# combo.pack(pady=20)
# ###############
# colors = ['red','silver','blue']
# color=StringVar(value='default')
# combo_color=CTkComboBox(window,values=colors,variable=color,command=set_color)
# combo_color.pack(pady=20)
# name=CTkButton(window,text='click')
# name.pack()
# window.mainloop()
########################################
def set_color(choice):
    btn_setcolor.configure(fg_color=choice)
def insert_color():
    text = color_input.get()
    if text not in colors:
        colors.append(text)
    combo_color.configure(values=colors)
    color_input.delete(0,END)
window = CTk()
window.geometry('500x500')

color_input = CTkEntry(window,placeholder_text='color: ')

colors = ['red','silver','blue']
color=StringVar(value='default')
combo_color=CTkComboBox(window,values=colors,variable=color,
                        corner_radius=50,command=set_color,dropdown_hover_color='#FF00AA')
btn_setcolor = CTkButton(window,text='set new color',command=insert_color)
combo_color.pack(pady=20)
color_input.pack(pady=10)
btn_setcolor.pack()
window.mainloop()