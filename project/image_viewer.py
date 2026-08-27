from tkinter import *
from PIL import ImageTk, Image

def forward(img_no):
       global forward_button
       global Back_button
       global Exit_button
       global label

       label.grid_forget()
       label=Label(image=list_images[img_no-1])
       label.grid(row=0,column=0,columnspan=4)

       forward_button=Button(window,text='Forward',bg='#2563EB',fg='white',command=lambda:forward(img_no+1))

       if img_no==4:
                 forward_button=Button(window,text='Forward',state=DISABLED)

       Back_button=Button(window,text='Back',bg='#2563EB',fg='white',command=lambda:back(img_no-1))

       forward_button.grid(row=5,column=0)
       Back_button.grid(row=5,column=2)
       Exit_button.grid(row=5,column=1)


def back(img_no):
    global forward_button
    global Back_button
    global Exit_button
    global label


    label.grid_forget()
    label=Label(image=list_images[img_no-1])
    label.grid(row=0,column=0,columnspan=4)

    Back_button=Button(window,text='Back',bg='#2563EB',fg='white',command=lambda:back(img_no-1))
    forward_button=Button(window,text='Forward',bg='#2563EB',fg='white',command=lambda:forward(img_no+1))

    if img_no==1:
          Back_button=Button(window,text='Back',state=DISABLED)

    forward_button.grid(row=5,column=0)
    Back_button.grid(row=5,column=2)
    Exit_button.grid(row=5,column=1)


window=Tk()
window.title('image')
window.configure(bg='#0F172A')
window.geometry('600x600')

i1=ImageTk.PhotoImage(Image.open('sa1.jpg'))
i2=ImageTk.PhotoImage(Image.open('sa2.jpg'))
i3=ImageTk.PhotoImage(Image.open('sa3.jpg'))
i4=ImageTk.PhotoImage(Image.open('sa4.jpg'))

list_images=[i1,i2,i3,i4]

label = Label(image=i1)
label.grid(row=0,column=0,columnspan=4)

forward_button= Button(window,text="Forward",bg='#2563EB',fg='white',command=lambda:forward(2))

Back_button= Button(window,text="Back",bg='#2563EB',fg='white',command=back,state=DISABLED)

Exit_button= Button(window,text="Exit",bg='#DC2626',fg='white',command=window.quit)

forward_button.grid(row=5,column=0)
Back_button.grid(row=5,column=2)
Exit_button.grid(row=5,column=1)


window.mainloop()