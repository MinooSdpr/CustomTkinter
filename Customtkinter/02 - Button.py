from customtkinter import *

window = CTk()
window.geometry('500x500')
window.title('Button')
btn = CTkButton(window,text='click',width=45,height=10,corner_radius=15,border_width=3,
                border_color='black',border_spacing=6,
                hover_color=('#88008B','#556B7A'),text_color='black',
                )
btn.pack()
window.mainloop()