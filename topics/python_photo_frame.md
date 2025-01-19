---
layout: template_generalFiles
title: Write the Python code for displaying the photos
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+.
---

# {{ page.title }}

A digital photo frame reads photo files from a storage device, and displays them on the screen for a specified time. For the photo frame that you're building, this job will be done by a Python program.

The operating system that you installed on the Raspberry Pi already includes Python, as well as an integrated development environment (IDE) that makes it easier for you to write, run, and edit Python programs. This IDE is the Thonny IDE. You'll use Thonny to write the photo frame program.

1.  Switch on the Raspberry Pi. If you're [using Raspberry Pi Connect](pi_piconnect.md), wait for a few seconds till the green light stops flashing on the Pi board, and then connect to the Pi through screen sharing.
1.  Update the operating system by running the following command: `sudo apt-get update`.
1.  Upgrade all of the installed packages by running the following command: `sudo apt-get upgrade`.
1.  Open Thonny by clicking the Raspberry Pi icon near the top left, and then clicking **Programming > Thonny**.
1.   

<hr/>

## The code

```python
{% include pyscript_photo_frame.py %}
```

> You can also [download the raw Python file](https://raw.githubusercontent.com/AninditaBasu/pi-projects/refs/heads/main/_includes/pyscript_photo_frame.py).

## The explanation


<hr/>

Now that your digital photo frame is working, consider the following enhancements:

-  Disable the screen blanking function of the Raspberry Pi. The screen can turn completely black after a period of inactivity. This means, if you start the Python program and then leave it on to loop through your pictures continuously, what will happen is that the screen will eventually turn blank. The Pi computer is still on, and the Python program is still running, but the screen is black because of inactivity. To prevent this from happening, [disable screen blanking](https://raspberrytips.com/disable-sleep-mode-raspberry-pi/).
-  Add a touch button to stop the Python script. The script you're using now can be stopped by pressing the `Esc` key on a keyboard, but you might not always have the USB receiver for the keyboard plugged into the Raspberry Pi. Stop the script might become necessary in the following situations:
   -  To power down the Raspberry Pi.
   -  To load more photos on to the flash drive, in which case you must eject the drive, load the files into it, and then insert it back into the Raspberry Pi.
 A Python script that has a touch button function is here: [code with stop-on-touch function](https://raw.githubusercontent.com/AninditaBasu/pi-projects/refs/heads/main/_includes/pyscript_photo_frame_touch_stop.py). Notice lines 44 through 50, which include a function to stop the script on touch input or a click of the left mouse button.
-  Have the Python display loop also include photos from a cloud drive.
-  Put the entire assembly into a case or stand. Doing so not only protects the computer boards from dust, but also gives support to the assembly so that it can stand on its own, without you having to use books or other such objects as props. I used a [Multicomp Pro case] (https://www.amazon.in/Robotism-Official-Screen-Display-Raspberry/dp/B09KTRT3KF/ref=sr_1_3), which was the only case available in my part of the world. Other options are a [Pimoroni stand](https://shop.pimoroni.com/products/raspberry-pi-7-touchscreen-display-frame?variant=6337432065) or a 3-D printed case from the [designs at thingiverse.com](https://www.thingiverse.com/search?q=raspberry+touchscreen+display&page=1).


