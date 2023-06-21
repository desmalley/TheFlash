import os
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk

def drop(event):
    filepath = event.data
    # Remove the braces {} and strip leading/trailing whitespace
    filepath = filepath.replace('{', '').replace('}', '').strip()

    if os.path.isfile(filepath):
        print(f'Successfully dropped file: {filepath}')

        # Open, resize, and display the image
        image = Image.open(filepath)
        image.thumbnail((100, 100))  # Change to desired thumbnail size
        photo = ImageTk.PhotoImage(image)

        # Create a new label with the image
        image_label = tk.Label(root, image=photo)
        image_label.image = photo  # Keep a reference to the image to avoid garbage collection
        image_label.pack()

    else:
        print(f'Error: {filepath} is not a valid file')

root = TkinterDnD.Tk()
root.withdraw()
root.title('Drag and Drop')
root.geometry('200x200')

label = tk.Label(root, text='Drag File Here')
label.pack(expand=True, fill='both')

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

root.deiconify()
root.mainloop()
