"""
# pyPicDeMo

This application was developed through a collaborative effort between Damien and ChatGPT. Damien guided the project with specific requirements and design choices, while ChatGPT provided code implementation and technical assistance. Together, we created a user-friendly tool for managing photos by allowing users to easily move or delete images within a specified folder.

This project is released under an open-source license and is freely available for modification and distribution.

# Contributors:
- Damien: Project concept, design decisions, and guidance.
- ChatGPT: Code implementation and technical support.

# This file is part of the pyPicDeMo project.
#
# pyPicDeMo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyPicDeMo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyPicDeMo. If not, see <https://www.gnu.org/licenses/>.

"""

import os
import shutil
from tkinter import Tk, Label, Button, filedialog, Frame, LEFT, BOTTOM
from PIL import Image, ImageTk
from send2trash import send2trash
import json

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)
move_to_folder = config["move_to_folder"]

class PhotoManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Manager")
        
        # Set a consistent window size
        self.master.geometry("850x900")

        # Main canvas for the image
        self.canvas = Label(master)
        self.canvas.pack(expand=True, fill="both")

        # Label for displaying the filename
        self.filename_label = Label(master, text="", font=("Arial", 12))
        self.filename_label.pack(pady=10)

        # Create a Frame for the buttons and pin it to the bottom right
        self.button_frame = Frame(master)
        self.button_frame.pack(side=BOTTOM, anchor="e", padx=20, pady=20)

        self.move_button = Button(self.button_frame, text="MOVE", command=self.move_photo)
        self.move_button.pack(side=LEFT, padx=5)

        self.delete_button = Button(self.button_frame, text="DELETE", command=self.delete_photo)
        self.delete_button.pack(side=LEFT, padx=5)

        self.browse_button = Button(self.button_frame, text="Browse Folder", command=self.browse_folder)
        self.browse_button.pack(side=LEFT, padx=5)

        self.photos = []
        self.current_index = 0

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.photos = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            self.current_index = 0
            self.show_photo()

    def show_photo(self):
        if self.current_index < len(self.photos):
            photo_path = self.photos[self.current_index]
            image = Image.open(photo_path)

            # Resize the image to fit within 800x800 while keeping aspect ratio
            image.thumbnail((800, 800), Image.Resampling.LANCZOS)
            photo_image = ImageTk.PhotoImage(image)
            
            self.canvas.config(image=photo_image)
            self.canvas.image = photo_image
            
            # Display the filename below the image
            self.filename_label.config(text=os.path.basename(photo_path))
        else:
            self.canvas.config(image='')
            self.filename_label.config(text="DONE!")

    def move_photo(self):
        if self.current_index < len(self.photos):
            original = self.photos[self.current_index]
            destination = os.path.join(move_to_folder, os.path.basename(original))

            # Handle duplicate files by adding a suffix
            base, extension = os.path.splitext(destination)
            counter = 1
            while os.path.exists(destination):
                destination = f"{base}_{counter}{extension}"
                counter += 1

            print(f"Moving {original} to {destination}")
            shutil.move(original, destination)
            self.current_index += 1
            self.show_photo()

    def delete_photo(self):
        if self.current_index < len(self.photos):
            photo_path = os.path.normpath(self.photos[self.current_index])
            print(f"Deleting {photo_path}")
            send2trash(photo_path)
            self.current_index += 1
            self.show_photo()

root = Tk()
my_gui = PhotoManager(root)
root.mainloop()
