from customtkinter import CTk,CTkFont,CTkLabel

root = CTk()
root.title('Label and font')
root.geometry('500x400')
font=CTkFont(family='B Titr',size=24)
l = CTkLabel(root,text= 'سلام بر شما',width=50,
             height= 10,text_color='red',font=font,fg_color='#003322')
l.pack()
root.mainloop()