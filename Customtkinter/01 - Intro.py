from customtkinter import *

window= CTk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
# window.wm_attributes('-fullscreen',True)
# window._set_appearance_mode('system')
window.geometry(f'{width}x{height}+0+0')
btn = CTkButton(window,text= 'click')
btn.pack()
window.mainloop()