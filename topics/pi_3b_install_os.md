---
layout: template_generalFiles
title: Install an operating system on Raspberry Pi 3B+
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+.
---

# {{ page.title }}

Do you see the microSD card near the center of the image? 

<img src="../images/frame_front.jpeg" width="75%" />

The operating system will be downloaded on to that card, and then inserted into the microSD slot of the Raspberry Pi. That's what will get this little computer up and running, and make it available for you to do the last steps of the photo frame project.

<hr/>

The steps to install an operating system for Raspberry Pi are:

1. On your laptop or desktop, format the microSD card and download Pi's operating system to it. A Rspberry Pi runs on 
2.  Insert the microSD card to the Pi's board, plus the power adapter to a wall socket and insert the cable into the USB-C power slot of the PI, and turn the wall switch on. The light on the Raspberry Pi board should glow green, and the display screen should first show a rectangle of rainbow colours, and then finally show you the Raspberry Pi desktop screen.
3.  Update the operating system.

Now that your Pi is ready to be used as a computer, you can proceed to creating the Python script that will read the files on the Raspberry Pi, and show them on the display screen.