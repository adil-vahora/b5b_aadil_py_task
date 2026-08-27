from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


# Select images
def select_images():

    global list_images
    global current_image
    global label

    files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.gif")
        ]
    )

    if not files:
        return

    # Add new images to the existing images
    for file in files:

        image = Image.open(file)
        image.thumbnail((500, 450))

        photo = ImageTk.PhotoImage(image)
        list_images.append(photo)

    # If this is the first selection
    if current_image >= len(list_images):
        current_image = 0

    label.config(image=list_images[current_image])

    update_buttons()


# Forward
def forward():

    global current_image

    if current_image < len(list_images) - 1:

        current_image += 1

        label.config(image=list_images[current_image])

    update_buttons()


# Back
def back():

    global current_image

    if current_image > 0:

        current_image -= 1

        label.config(image=list_images[current_image])

    update_buttons()


# Enable / Disable buttons
def update_buttons():

    if len(list_images) == 0:

        forward_button.config(state=DISABLED)
        Back_button.config(state=DISABLED)

        return

    if current_image == len(list_images) - 1:

        forward_button.config(state=DISABLED)

    else:

        forward_button.config(state=NORMAL)

    if current_image == 0:

        Back_button.config(state=DISABLED)

    else:

        Back_button.config(state=NORMAL)


# Main window
window = Tk()

window.title("Image Viewer")
window.geometry("700x650")

# Professional background
window.configure(bg="#1E1E2E")


# List of images
list_images = []

current_image = 0


# Image display
label = Label(
    window,
    bg="#1E1E2E"
)

label.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=30
)


# Select Images button
select_button = Button(
    window,
    text="Select Images",
    command=select_images,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8,
    relief=FLAT,
    cursor="hand2"
)

select_button.grid(
    row=4,
    column=0,
    columnspan=3,
    pady=15
)


# Forward button
forward_button = Button(
    window,
    text="Forward →",
    command=forward,
    bg="#3A86FF",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=12,
    pady=6,
    relief=FLAT,
    cursor="hand2",
    state=DISABLED
)

forward_button.grid(
    row=5,
    column=0,
    padx=10,
    pady=10
)


# Back button
Back_button = Button(
    window,
    text="← Back",
    command=back,
    bg="#3A86FF",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=12,
    pady=6,
    relief=FLAT,
    cursor="hand2",
    state=DISABLED
)

Back_button.grid(
    row=5,
    column=1,
    padx=10,
    pady=10
)


# Exit button
Exit_button = Button(
    window,
    text="Exit",
    command=window.quit,
    bg="#E63946",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=12,
    pady=6,
    relief=FLAT,
    cursor="hand2"
)

Exit_button.grid(
    row=5,
    column=2,
    padx=10,
    pady=10
)

window.mainloop()