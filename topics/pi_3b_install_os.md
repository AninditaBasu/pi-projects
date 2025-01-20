---
layout: template_generalFiles
title: Install an operating system on Raspberry Pi 3B+
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+.
pimodel: Raspberry Pi 3
baseos: Debian Bookworm
pios: Raspberry Pi OS 64-bit (A port of Debian Bookworm with the Raspberry Pi Desktop)
---

# {{ page.title }}

Do you see the black microSD card near the bottom center of the image, right next to the three heat sinks? 

<img src="../images/pi_3.jpeg" width="75%" />

The operating system will be downloaded on to that card, which will then be inserted into the microSD slot of the Raspberry Pi. That's what will get this little computer up and running, and make it available for you for the final steps of the photo frame project.

<hr/>

## Steps

{% include install_os.md %}
1.  Insert the microSD card to the Raspberry Pi's board, plug in the power adapter to a wall socket, and insert the cable into the USB-C power slot of the Raspberry Pi. If you're going to use an external keyboard and mouse, insert the USB receivers for these devices into the USB ports of the Raspberry Pi.
1. Turn on the power switch of the wall socket. The light on the Raspberry Pi board should glow green, and the display screen should first show a rectangle of rainbow colours, and then finally show you the Raspberry Pi desktop screen.
1.  If you already have an external keyboard and mouse, shut down the Raspberry Pi by clicking the Raspberry Pi icon near the top left and then clicking **Shutdown > Shutdown**. If you don't have an external keyboard and mouse, log in to the Raspberry Pi from your laptop:
    1.  Find the IP address of your nework gateway. To do so, on your laptop, open the command prompt, and type `ipconfig`. Then, note down the value that's displayed as **Default Gateway**.
    1.  Start Angry IP Scanner. For the first box in the **IP Range** field, specify the value of the default gateway that you noted down in the previous step. For the second field, specify a number that's about 15-20 stops away. For example, if your default gateway is `192.168.1.0`, specify the end range to be something around `192.168.1.15`, so that the scan doesn't take too long. (The assumption here is that you don't have more than 15-20 devices already connected to your network!) Click **Start** and wait for the scan to be over. Then, in the **Hostname** column, look for the name of your Raspberry Pi. This is the name that you specified as the hostname in the OS Customisation settings while downloading the operating system on the microSD card. When you've spotted this hostname, look for the entry in the **IP** column. You need this value in the next step.
	1.  On your laptop, start PuTTY and enter the IP address of your Raspberry Pi. This is the value that you noted down in your previous step. Click **Open**. When prompted for login credentials, enter the user name and password that you specified in the OS Customisation settings while downloading the operating system on the microSD card. You should now see a prompt like this: `<hostname>@<username>:~ $`. It means you're now logged in to your Raspberry Pi and everything's working as expected.
	1.  Shut down the Raspberry Pi by typing the following command on the terminal: `sudo shutdown -h now`. You should be disconnected from Raspberry Pi and the terminal window should disappear.
1.  Switch off the power supply to the Raspberry Pi.

Now that your Raspberry Pi is ready to be used as a computer, you can proceed to [creating the Python script](python_photo_frame.md) that displays your photo collection.

<hr/>

