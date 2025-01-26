---
layout: template_generalFiles
title: Write the Python code for displaying the photos
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+.
---

{% include mermaid_photo_frame_flowchart.md %}

# {{ page.title }}

A digital photo frame reads photo files from a storage device, and displays them on the screen for a specified time. For the photo frame that you're building, this job will be done by a Python program.

The operating system that you installed on the Raspberry Pi already includes Python, as well as an integrated development environment (IDE) that makes it easier for you to write, run, and edit Python programs. This IDE is the Thonny IDE. You'll use Thonny to write the photo frame program.

1.  Switch on the Raspberry Pi.
1.  If you don't have an external keyboard or mouse, log in remotely to your Raspberry Pi by using Connect:
    1.  On your laptop, open `https://connect.raspberrypi.com/` and sign in.
	1.  On the Devices page, click **Connect via > Screen sharing**, and wait for a few seconds for the remote session to start. You should then see the Raspberry Pi desktop in your laptop browser window.
1.  Install any patches, fixes, and upgrades that might have been made to the operating system by opening the Raspberry Pi terminal window and running the following two commands one after the other:
    -  `sudo apt-get update`
	-  `sudo apt-get upgrade`
1.  Open Thonny by clicking the Raspberry Pi icon near the top left, and then clicking **Programming > Thonny**.
1.   

<hr/>

## The code

```python

{% include pyscript_photo_frame.py %}

```

<br/>
<span style="font-size:75%;">You can also [download the raw Python file](https://raw.githubusercontent.com/AninditaBasu/pi-projects/refs/heads/main/_includes/pyscript_photo_frame.py).</span>

## The visual representation

The following class diagram shows the functions in the code, their interactions, and the variables they define, use, or return.

{% include mermaid_pyscript_photo_frame_class_diagram.md %}

The following entity relationship diagram shows the relationship between the functions, objects, and variables in the code.

{% include mermaid_pyscript_photo_frame_er_diagram.md %}

## The explanation

Notice the first four lines of the code.

```python
import os
import time
from PIL import Image, ImageTk
import tkinter as tk
```
