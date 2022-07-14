from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Image Viewer')

img_1 = ImageTk.PhotoImage(Image.open('images/img1.png'))
img_2 = ImageTk.PhotoImage(Image.open('images/img2.png'))
img_3 = ImageTk.PhotoImage(Image.open('images/img3.png'))

images = [img_1, img_2, img_3]
start = 0

label = Label(image=images[start])
label.grid(row=0, column=0, columnspan=3)

def forward(img_num):
    global label
    global forward_button
    global back_button
    global status
    if img_num == len(images) - 1:
        label.grid_forget()
        label = Label(image=images[img_num])
        label.grid(row=0, column=0, columnspan=3)

        forward_button = Button(root, text='>>', state=DISABLED)
        forward_button.grid(row=1, column=2, pady=20)

        back_button = Button(root, text='<<', command=lambda: back(img_num-1))
        back_button.grid(row=1, column=0, pady=20)

        status = Label(root, text='Image ' + str(img_num+1) + ' of ' + str(len(images)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    else:
        label.grid_forget()
        label = Label(image=images[img_num])
        label.grid(row=0, column=0, columnspan=3)

        forward_button = Button(root, text='>>', command=lambda: forward(img_num+1))
        forward_button.grid(row=1, column=2, pady=20)

        back_button = Button(root, text='<<', command=lambda: back(img_num-1))
        back_button.grid(row=1, column=0, pady=20)

        status = Label(root, text='Image ' + str(img_num+1) + ' of ' + str(len(images)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
        


def back(num):
    global label
    global forward_button
    global back_button
    global status
    if num == 0:
        label.grid_forget()
        label = Label(image=images[num])
        label.grid(row=0, column=0, columnspan=3)

        forward_button = Button(root, text='>>', command=lambda: forward(num+1))
        forward_button.grid(row=1, column=2, pady=20)

        back_button = Button(root, text='<<', state=DISABLED)
        back_button.grid(row=1, column=0, pady=20)

        status = Label(root, text='Image ' + str(num+1) + ' of ' + str(len(images)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    else:
        label.grid_forget()
        label = Label(image=images[num])
        label.grid(row=0, column=0, columnspan=3)

        forward_button = Button(root, text='>>', command=lambda: forward(num+1))
        forward_button.grid(row=1, column=2, pady=20)

        back_button = Button(root, text='<<', command=lambda: back(num-1))
        back_button.grid(row=1, column=0, pady=20)

        status = Label(root, text='Image ' + str(num+1) + ' of ' + str(len(images)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)



back_button = Button(root, text='<<', state=DISABLED)
exit_button = Button(root, text='Exit', command=root.quit)
forward_button = Button(root, text='>>', command=lambda: forward(start+1))

status = Label(root, text='Image 1 of ' + str(len(images)), bd=1, relief=SUNKEN, anchor=E)

back_button.grid(row=1, column=0, pady=20)
exit_button.grid(row=1, column=1, pady=20)
forward_button.grid(row=1, column=2, pady=20)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()