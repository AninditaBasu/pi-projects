---
layout: template_generalFiles
title: Digital photo frame
---

# {{ page.title }}

A digital photo frame is an LED device that can display pictures. It's similar to an LCD TV, inasmuch as you can plug in a USB flash drive to the TV's port and view the pictures. A photo frame is, however, not as large as a typical TV. Quite a few digital frames also have speakers, just like TVs do, so that you can view movie clips on it as well. Unlike a TV, where you must scroll through the pictures manually, a digital photo frame can be configured to display pictures in a continuous loop, advancing to the next picture after a specified time period.

In this tutorial, I show you how to use a Raspberry Pi 3B+ computer and a Raspberry Pi Touch Display to make a digital photo frame. Along the way, I explain how to set up a headless Raspberry Pi computer, connect it to a touch display, and then run Python on it.

## Materials required

For the frame:

-  A Raspberry Pi 3B+ computer. This little computer board will hold the code that displays the images.
-  A Raspberry Pi 7" official touch display. This screen is where the images are displayed.
-  A Raspberry Pi official power adapter. Theoretically, any adapter with a USB-C cable that can plug into the Raspberry should work fine. In practice, it's better to get the official power adapter because it's been tested to deliver the exact power that the Raspberry Pi needs (which is 3A).
-  A microSD card. This tiny card will contain the operating system that your Raspberry Pi will run on.
-  A USB drive. This flash drive will contain your images.

To set up the Raspberry Pi:

-  A laptop or desktop, with a microSD port. If your machine does not have this port, you need a microSD card reader that you can plug into your machine.
-  An internet connection.

After the Raspberry Pi is set up and the photo frame is working, you'll no longer need the laptop (or desktop). You can also choose to run the photo frame in an isolated manner, in which case you won't need the internet connection either. 

## Set up the Raspberry Pi







