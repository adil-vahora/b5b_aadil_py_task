from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
list_images=[]

def forward(img_no):

       global forward_button
       global Back_button
       global Exit_button
       global label

       #label.grid_forget()

       label=Label(image=list_images[img_no-1])
       label.grid(row=0,column=0,columnspan=4)

       forward_button=Button(window,text='Forward',
                             command=lambda:forward(img_no+1))

       if img_no==3:
                forward_button=Button(window,text='Forward',
                                      state=DISABLED)

       Back_button=Button(window,text='Back',
                          command=lambda:back(img_no-1))

       forward_button.grid(row=5,column=0)
       Back_button.grid(row=5,column=1)
       Exit_button.grid(row=5,column=2)


def back(img_no):

    global forward_button
    global Back_button
    global Exit_button
    global label


    label=Label(image=list_images[img_no-1])
    label.grid(row=0,column=0,columnspan=4)

    Back_button=Button(window,text='Back',
                       command=lambda:back(img_no-1))

    forward_button=Button(window,text='Forward',
                          command=lambda:forward(img_no+1))

    if img_no==1:
          Back_button=Button(window,text='Back',
                             state=DISABLED)

    forward_button.grid(row=5,column=0)
    Back_button.grid(row=5,column=1)
    Exit_button.grid(row=5,column=2)


# NEW: Select File function
def select_file():

    global list_images
    global label

    file = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg")
        ]
    )

    if file:
        image = ImageTk.PhotoImage(Image.open(file))

        list_images.append(image)

        label.grid_forget()

        label = Label(image=image)
        label.image = image
        label.grid(row=0,column=0,columnspan=4)


window=Tk()

window.title('image')
window.configure(bg='#0F172A')
window.geometry('600x600')







forward_button=Button(
    window,
    text="forward",
    command=lambda:forward(1)
)

Back_button=Button(
    window,
    text="Back",
    command=back,
    state=DISABLED
)

Exit_button=Button(
    window,
    text="Exit",
    command=window.quit
)

# NEW: Select File button
select_button=Button(
    window,
    text="Select File",
    command=select_file
)


forward_button.grid(row=5,column=0)
Back_button.grid(row=5,column=1)
Exit_button.grid(row=5,column=2)
select_button.grid(row=5,column=3)


window.mainloop()