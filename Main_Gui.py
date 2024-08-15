import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk


window = ttk.Window(themename="cyborg")
window.title("Main Page")
window.geometry("900x600")

# # colamn configeration
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)

# # row configeration
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
# window.rowconfigure(2, weight=1)


# styles
style = ttk.Style()
style.configure("info.TLabelframe",foreground="#6EACDA",bordercolor="black")
style.configure("info.TButton",background="#6EACDA",bordercolor="#6EACDA",lightcolor="#6EACDA",focuscolor="#6EACDA",darkcolor="#6EACDA")
style.configure("info.TRadiobutton", foreground="#black",font="Bold")
style.configure("success.TRadiobutton", foreground="white",font="Bold")
style.map('info.TButton', foreground=[('disabled', 'black'),('active', 'black')] , background=[('disabled', 'white'),('active', '#f0f8ff')]   )

#*****


# Frame botom pages
Info_frame=ttk.Labelframe(window, style='info.TLabelframe',width=200)
Info_frame.place(x=350,y=0)


B_1=ttk.Button(Info_frame, text='Page 1', style='info.TButton',width=10).grid(row=0,column=0,sticky=N,padx=10,pady=5)
B_2=ttk.Button(Info_frame, text='Page 2', style='info.TButton',width=10).grid(row=0,column=1,sticky=N,padx=10,pady=5)
B_3=ttk.Button(Info_frame, text='Page 3', style='info.TButton',width=10).grid(row=0,column=2,sticky=N,padx=10,pady=5)
B_4=ttk.Button(Info_frame, text='Page 4', style='info.TButton',width=10).grid(row=0,column=3,sticky=N,padx=10,pady=5)
B_5=ttk.Button(Info_frame, text='Page 5', style='info.TButton',width=10).grid(row=0,column=4,sticky=N,padx=10,pady=5)

#*****

# masege
Hellow_masege=ttk.Label(window,text="Online Shopping",font="roboto 35 bold",foreground="#6EACDA").place(x=500,y=100)
Hellow_masege_2=ttk.Label(window,text="""Welcome to our online store!
We are delighted to have you join our family.team is here to
and exclusive offers. Don’t forget to subscribe  help 
If you have any questions or need assistance, our support 
Happy shopping!
""",font="roboto 10 bold",foreground="#E2E2B6").place(x=500,y=170)

#*****

# images

image_orginal=Image.open('2222.png').resize((60,60))
image_tk= ImageTk.PhotoImage(image_orginal)

img_label= ttk.Label(window,image=image_tk).place(x=20,y=5)


image_orginal2=Image.open('on20.png').resize((340,340))
image_tk2= ImageTk.PhotoImage(image_orginal2)

img_label_2= ttk.Label(window,image=image_tk2).place(x=80,y=150)


image_orginal3=Image.open('11111.png').resize((300,300))
image_tk3= ImageTk.PhotoImage(image_orginal3)

img_label_3= ttk.Label(window,image=image_tk3).place(x=520,y=280)

#*****


window.mainloop()
