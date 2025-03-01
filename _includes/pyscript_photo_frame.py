import os
import time
import tkinter as tk
from PIL import Image, ImageTk

# Function to get a list of image files from a directory and its subdirectories
def get_image_files(directory):
    image_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.gif'}
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(tuple(image_extensions)):
                image_files.append(os.path.join(root, file))
    return image_files

# Main function to run the digital photo frame
def digital_photo_frame():
    # Directories to scan for images
    local_dir = os.getcwd()  # Current working directory
    usb_dir = '/media/pi/'  # The USB mount path in the Raspberry Pi
    # Collect all image files
    images = get_image_files(local_dir) + get_image_files(usb_dir)
    if not images:
        print("Couldn't find any image files in the specified directories.")
        return
    # Create a Tkinter window
    root = tk.Tk()
    root.title('Raspberry Pi Photo Frame') # The title doesn't matter; it won't be displayed
    # Fullscreen settings (optional)
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda e: root.destroy())  # Exit fullscreen with the Esc key
    # Label to display the image
    label = tk.Label(root)
    label.pack(expand=True, fill=tk.BOTH)
    # Function to update the displayed image
    def update_image(index):
        img_path = images[index]
        img = Image.open(img_path)
        img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo
        root.after(10000, update_image, (index + 1) % len(images))  # Change the image every 10 seconds
    # Start displaying the first image
    update_image(0)
    # Run the Tkinter event loop
    root.mainloop()

# Run the script
if __name__ == "__main__":
    digital_photo_frame()
