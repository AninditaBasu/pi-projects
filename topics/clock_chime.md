---
layout: template_generalFiles
title: Chiming clock
description: Chime on the hour and the half hour
created: Jan 28, 2025
updated: Jan 28, 2025
---

# {{ page.title }}

In this tutorial, I show you how to use a Raspberry Pi 4 computer and an external speaker to simulate the chimes of a grandfather clock. Along the way, I explain how to set up a headless Raspberry Pi computer, and write Python code on it. It doesn't matter if you don't know Python, because I'll provide the entire code for you to copy and use.

-  [Materials](#materials)
-  [Steps](#steps)
-  [Cost](#cost)

<hr/>

## Materials

For the chimes:

-  A Raspberry Pi 4B computer. This little computer board will hold the code that makes the chimes ring out every half hour and hour. Structky speaking, you don't need a Raspberry Pi 4B computer; an older model will work excellently too because this project doesn't need much computing power. But I was already using my Raspberry Pi 4B for something else, so I deployed this project on on it.
-  A speaker. For this project, I used a Honeywell soundbar, but you can use any speaker that has a 3.5mm audio jack and is externally powered through a separate plugpoint.
-  A Raspberry Pi official power adapter. Theoretically, any adapter with a USB-C cable that can plug into the Raspberry should work fine. In practice, it's better to get the official power adapter because it's been tested to deliver the exact power that the Raspberry Pi needs (which is 3A).
-  A microSD card. This tiny card will contain the operating system that your Raspberry Pi will run on.
-  (Optional) Heat sinks. These are little metal blocks that draw the heat away from the processor and the network chip. A photo frame program running on the Raspberry Pi should not heat the computer much, but it is safe practice to use heat sinks.
-  (Optional) An external keyboard and a mouse. These two things are optional, because you can use your laptop keyboard and touchpad to issue commands to the Raspberry Pi.

To set up the Raspberry Pi:

-  A laptop (or desktop), with a microSD port. If your laptop does not have this port, you need a microSD card reader that you can plug into laptop. After the Raspberry Pi is set up and the photo frame is working, you'll no longer need the laptop.
-  Administrator privileges on the laptop, so that you can download all the required software on it.
-  An internet connection. After the set up is complete, this project does not need an internet connection.

## Steps

You make the Raspberry Pi ready by installing an operating system on it, and write a script to play the chimes.

Here are the step-by-step guides for these tasks:

1.  (Optional) Fix the heat sinks on the Raspberry Pi.
1.  [Make your laptop ready](set_up_laptop.md) for setting up the Raspberry Pi.
1.  Install an operating system on the Raspberry Pi.
1.  Write the Python code for playing the chimes every hour and every half hour.

## Cost

All figures are in Indian Rupees (INR), and inclusive of GST (goods and service tax).

| Item | Amount (INR) | Notes |
| ---- | -----------: | ------ |
| Raspberry Pi 4 Model B |  | You can use an older model too. Raspberry Pi Zero, for example, which costs significantly less. |
| 12.5W Official Raspberry Pi Micro USB Power Supply | 708.00 | |
| Raspberry Pi Official 32GB V3.0 , A2 Class Micro SD | 398.84 | |
| Aluminium Heat Sink | 35.40 | |
| Honeywell Moxie V500 10W Portable USB Wired Soundbar  | 789.00 | You can use any externally powered speaker that has an audio jack |

| | **.**|