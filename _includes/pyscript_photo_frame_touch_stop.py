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
    usb_dir = '/media/pi/'  # Adjust the USB mount path as per your setup
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
    root.bind("<Escape>", lambda e: root.destroy())  # Exit fullscreen with Escape key
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
        root.after(10000, update_image, (index + 1) % len(images))  # Change image every 10 seconds
    # Add a blue button for touchscreen stop functionality
    def stop_program(event):
        root.destroy()
    # Create an overlay in the top-left corner (25x25 pixels) to detect touch
    touch_exit_area = tk.Frame(root, width=25, height=25, bg="blue")  # Blue for visibility purposes
    touch_exit_area.place(x=0, y=0)
    touch_exit_area.bind("<Button-1>", stop_program)  # Bind left mouse button or touchscreen press
    # Start displaying the first image
    update_image(0)
    # Run the Tkinter event loop
    root.mainloop()

# Run the digital photo frame script
if __name__ == "__main__":
    digital_photo_frame()
