---
layout: template_generalFiles
title: Install an operating system on Raspberry Pi 3B+
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+.
---

# {{ page.title }}

Do you see the microSD card near the center of the image? 

<img src="../images/frame_front.jpeg" width="75%" />

The operating system will be downloaded on to that card, which will then be inserted into the microSD slot of the Raspberry Pi. That's what will get this little computer up and running, and make it available for you for the final steps of the photo frame project.

<hr/>

The steps to install an operating system for Raspberry Pi are:

1. On your laptop or desktop, format the microSD card and download Pi's operating system to it. Raspberry Pi computers all run on  operating systems that are based on the open-source Debian OS. This tutorial uses an OS that's based on Debian Bookworm and made for Raspberry Pi 3B+. The recommended method of downloading an OS is by using Raspberry Pi Imager. To download the OS to the card, follow the steps in the official documentation for [installing an operating system](https://www.raspberrypi.com/documentation/computers/getting-started.html#raspberry-pi-imager).
1.  Insert the microSD card to the Pi's board, plug in the power adapter to a wall socket, and insert the cable into the USB-C power slot of the Raspberry Pi. If you're going to use an external keyboard and mouse, insert the USB receivers for these devices into the USB ports of the Pi.
1. Turn on the power switch of the wall socket. The light on the Raspberry Pi board should glow green, and the display screen should first show a rectangle of rainbow colours, and then finally show you the Raspberry Pi desktop screen.
1.  If you already have an external keyboard and mouse, proceed to the next step. If you don't, (or if you want to do this step anyway because there's no harm if you do), [set up Raspberry Pi Connect](pi_piconnect.md). If you install Raspberry Pi Connect, you can log in to the Pi from any other computer, and use that computer's keyboard and mouse to control the Pi. To set up Raspberry Pi Connect, see the official documentation: [Raspberry Pi Connect (Beta)](https://www.raspberrypi.com/documentation/services/connect.html).
1.  Shut down the Raspberry Pi by clicking the Raspberry Pi icon near the top left and then clicking **Shutdown > Shutdown**. Then, switch off the power supply to the Pi.

Now that your Pi is ready to be used as a computer, you can proceed to [creating the Python script](python_photo_frame.md) that will read the photos on the Raspberry Pi, and show them on the display screen.

<hr/>

## Troubleshooting
