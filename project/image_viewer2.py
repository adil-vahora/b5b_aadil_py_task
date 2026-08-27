from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


def select_img():

       files = filedialog.askopenfilenames(
               title="Select Images",
               filetypes=[
                   ("Image Files", "*.png *.jpg *.jpeg *.gif")
               ]
           )

       for file in files:
       
               image = Image.open(file)
               image.thumbnail((500, 450))
       
               photo = ImageTk.PhotoImage(image)
               list_images.append(photo)

       if len(list_images)>0:

               label.config(image=list_images[0])

               Back_button.config(state=DISABLED)

               if len(list_images)==1:
                     forward_button.config(state=DISABLED)
               else:
                     forward_button.config(state=NORMAL)


def forward(img_no):

       global forward_button
       global Back_button
       global Exit_button
       global label

       label.grid_forget()

       label=Label(window,image=list_images[img_no-1],bg='black')
       label.grid(row=0,column=0,columnspan=4)

       forward_button=Button(
              window,
              text='Forward',
              bg='#2563EB',
              fg='white',
              command=lambda:forward(img_no+1)
       )

       if img_no==len(list_images):
                 forward_button=Button(
                        window,
                        text='Forward',
                        bg='#2563EB',
                        fg='white',
                        state=DISABLED
                 )

       Back_button=Button(
              window,
              text='Back',
              bg='#2563EB',
              fg='white',
              command=lambda:back(img_no-1)
       )

       forward_button.grid(row=5,column=0)
       Back_button.grid(row=5,column=2)
       Exit_button.grid(row=5,column=1)
       select_button.grid(row=5,column=3)


def back(img_no):

    global forward_button
    global Back_button
    global Exit_button
    global label

    label.grid_forget()

    label=Label(window,image=list_images[img_no-1],bg='black')
    label.grid(row=0,column=0,columnspan=4)

    Back_button=Button(
           window,
           text='Back',
           bg='#2563EB',
           fg='white',
           command=lambda:back(img_no-1)
    )

    forward_button=Button(
           window,
           text='Forward',
           bg='#2563EB',
           fg='white',
           command=lambda:forward(img_no+1)
    )
    
    if img_no==1:
          Back_button=Button(
                 window,
                 text='Back',
                 bg='#2563EB',
                 fg='white',
                 state=DISABLED
          )

    forward_button.grid(row=5,column=0)
    Back_button.grid(row=5,column=2)
    Exit_button.grid(row=5,column=1)
    select_button.grid(row=5,column=3)


window=Tk()

window.title('image')

window.configure(bg='#0F172A')

window.geometry('600x600')


list_images=[]


label=Label(
       window,
       bg='#0F172A'
)

label.grid(row=0,column=0,columnspan=4)


forward_button=Button(
       window,
       text="Forward",
       bg='#2563EB',
       fg='white',
       command=lambda:forward(2),
       state=DISABLED
)

Back_button=Button(
       window,
       text="Back",
       bg='#2563EB',
       fg='white',
       command=back,
       state=DISABLED
)

Exit_button=Button(
       window,
       text="Exit",
       bg='#DC2626',
       fg='white',
       command=window.quit
)

select_button=Button(
       window,
       text="Select",
       command=select_img,
       bg='green',
       fg='white'

)


forward_button.grid(row=5,column=0)

Back_button.grid(row=5,column=2)

Exit_button.grid(row=5,column=1)

select_button.grid(row=5,column=3)


window.mainloop()