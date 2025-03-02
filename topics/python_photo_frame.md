---
layout: template_generalFiles
title: Write the Python code for displaying the photos
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+
created: Jan 19, 2025
updated: Jan 27, 2025
---

{% include mermaid_photo_frame_flowchart.md %}

# {{ page.title }}

A digital photo frame reads photo files from a storage device, and displays them on the screen for a specified time. For the photo frame that you're building, this job will be done by a Python program.

The operating system that you installed on the Raspberry Pi already includes Python, as well as an integrated development environment (IDE) that makes it easier for you to write, run, and edit Python programs. This IDE is the Thonny IDE. You'll use Thonny to write the photo frame program.

-  [The steps](#the-steps)
-  [The code, raw](#the-code-raw)
-  [The code, visually represented](#the-code-visually-represented)
-  [The code, explained](#the-code-explained)
-  [Troubleshooting](#troubleshooting)

<hr/>

## The steps

1.  Plug in the USB drive containing your photos to the Raspberry Pi, and switch it on.
1.  If you don't have an external keyboard or mouse, log in remotely to your Raspberry Pi by using Connect:
    1.  On your laptop, open `https://connect.raspberrypi.com/` and sign in.
	1.  On the Devices page, click **Connect via > Screen sharing**, and wait for a few seconds for the remote session to start. You should then see the Raspberry Pi desktop in your laptop browser window.
1.  Install any patches, fixes, and upgrades that might have been made to the operating system by opening the Raspberry Pi terminal window (the console icon near the top left) and running the following two commands one after the other:
    -  `sudo apt-get update`
	-  `sudo apt-get upgrade`
1.  Open Thonny by clicking the Raspberry Pi icon near the top left, and then clicking **Programming > Thonny**.
{% include thonny_venv.md %}
1.  Open a new file by clicking **File > New**. Copy into it the code from [The code, raw](#the-code-raw) section of this page. Then, edit line 20 to change `usb_dir = '/media/pi/'` to `usb_dir = '/media/<yourPiUserName>/'`. For example, if the user name that you specified when setting up the Raspberry Pi was `oracle`, line 20 in the code should be `usb_dir = '/media/oracle/'`.
1.  Install a Python package called `Pillow` in the virtual environment. To do so, click **Tools > Manage packages**, search for `Pillow`, and click **Install**.
1.  Save the file, and click the **Run** icon. You should see your photos being picked up and displayed one after the other.

<video width="40%" height="40%" controls>
  <source src="../images/demo_frame.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Your photo frame is now ready. You can leave it as is now, or you might choose to [refine it](photo_frame_refine.md). 

<hr/>

## The code, raw

```
{% include pyscript_photo_frame.py %}
```

<br/>
<span style="font-size:75%;">You can also [download the raw Python file](https://raw.githubusercontent.com/AninditaBasu/pi-projects/refs/heads/main/_includes/pyscript_photo_frame.py).</span>

## The code, visually represented

The following class diagram shows the functions in the code, their interactions, and the variables they define, use, or return.

{% include mermaid_pyscript_photo_frame_class_diagram.md %}

The following entity relationship diagram shows the relationship between the functions, objects, and variables in the code.

{% include mermaid_pyscript_photo_frame_er_diagram.md %}

## The code, explained

Notice the first four lines of the code.

```
import os
import time
import tkinter as tk
from PIL import Image, ImageTk
```

This is where you import all the libraries and packages needed for this project. {% include python_library.md %}

Some libraries are included by default in every Python installation. The libraries called `os`, `time`, and `tkinter`, called in the first three lines, are such libraries. Some other libraries are ones that you manually install in the virtual environment of your project. The `pillow` library, called here as `PIL`, is one such library. It is a library for handling images.

Take a look at this part of the code:

```
image_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.gif'}
```

All the possible photo extensions are listed here, but if you think any is missing, go ahead and add it here. If any of your photos use extensions spelt in uppercase letters (for example, `.JPEG` or `.PNG`), it's a good idea to add them to this list too.

See this bit of the code:

```
# Fullscreen settings (optional)
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda e: root.destroy())  # Exit fullscreen with the Esc key
```

You would've noticed that the display takes up the entire screen. Now, what if you need to stop the program from running? None of the Raspberry Pi controls are displayed anywhere. To take care of this eventuality, the `Esc` key of the keyboard has been bound to the action to stop the program midway.

Take a look at this bit, which controls the time for which a photo is displayed:

```
root.after(10000, update_image, (index + 1) % len(images))  # Change the image every 10 seconds
```

The number `10000` is in milliseconds. It means, every photo is displayed for 10 seconds. You can change this value to whatever you want the time lag between photos to be.

## Troubleshooting

If `Pillow` does not show up in the search results when you try to install it through **Tools > Manage packages**:

{% include thonny_install_packages.md %}

You should now be able to see `Pillow` in the list of installed packages.