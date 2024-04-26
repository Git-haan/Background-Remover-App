import tkinter as tk 
from tkinter import filedialog
from PIL import Image, ImageTk
from rembg import remove
import os
import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

class RemoverApp(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title('Background Remover App')
        self.geometry('700x500')
        self.configure(bg="EFEFEF")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.frame = customtkinter.CTkFrame(self, fg_color='transparent')
        self.frame.grid()

        self.label = customtkinter.CTkLabel(self.frame, text='Background Remover App', font=(' ', 20))
        self.label.grid(row=0, column=0, pady=(0,20), columnspan=2, sticky='nsew')

        self.input_canvas = customtkinter.CTkCanvas(self.frame, width=300, height=300, bg='black')
        self.input_canvas.grid(row=1, column=0, padx=10, pady=10)

        self.output_canvas = customtkinter.CTkCanvas(self.frame, width=300, height=300, bg='black')
        self.output_canvas.grid(row=1, column=1, padx=10, pady=10)

        self.upload_button = customtkinter.CTkButton(self.frame, text='Upload Image', command=self.upload_image)
        self.upload_button.grid(row=2, column=0, padx=10, pady=30, columnspan=2, sticky='nsew')

    def upload_image(self):
        print('Uploading Image...')
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg *.png *.jpeg')])

        if file_path:
            self.file_path = file_path

        self.input_image = Image.open(self.file_path).resize((300,300))
        self.input_photo = ImageTk.PhotoImage(self.input_image)

        self.input_canvas.create_image(0,0, image=self.input_photo, anchor='nw')
        print('Uploaded Image')

        self.upload_button.configure(text='Remove Background', command=self.remove_background)

    def remove_background(self):
        print('Removing Background...')
        output_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG Files', '*.png')])

        if output_path:
            with open(self.file_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)

        self.output_image = Image.open(output_path).resize((300,300))
        self.output_photo = ImageTk.PhotoImage(self.output_image)

        self.output_canvas.create_image(0,0, image=self.output_photo, anchor='nw')
        print('Background Removed')

        self.upload_button.configure(text='Upload Image', command=self.upload_image)

if __name__ == '__main__':
    app = RemoverApp()
    app.mainloop()
