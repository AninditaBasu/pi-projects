---
layout: template_generalFiles
title: Clock chimes
description: Chime on the hour and the half hour
created: Jan 28, 2025
updated: Jan 30, 2025
---

# {{ page.title }}

There was a time when meadow, grove, and stream, the earth, and every common sight, was apparelled in celestial light. It is not now as it hath been of yore. The things which I have seen I now can see no more. One such thing is a grandfather clock, that let out stately dings on the hour, every hour.

<video width="40%" height="40%" controls>
  <source src="../images/demo_clock.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> 

In this tutorial, I show you how to use a Raspberry Pi 4 computer and an external speaker to simulate the chimes of a grandfather clock. Along the way, I explain how to set up a headless Raspberry Pi computer, and write Python code on it. It doesn't matter if you don't know Python, because I'll provide the entire code for you to copy and use.

-  [Materials](#materials)
-  [Steps](#steps)
-  [Cost](#cost)
-  [Alternatives](#alternatives)

<hr/>

## Materials

For the chimes:

-  A Raspberry Pi 4B computer. This little computer board will hold the code that makes the chimes ring out every half hour and hour. Strictly speaking, you don't need a Raspberry Pi 4B computer; an older model will work excellently too **\*** because this project doesn't need much computing power. But I was already using my Raspberry Pi 4B for something else, so I deployed this project on it. Any Raspberry Pi model that has a 3.5 mm audio port will work **\***.
-  A speaker. For this project, I used a Honeywell soundbar, but you can use any speaker that has a 3.5 mm audio jack and is externally powered through a separate plug point **\*\***.
-  A Raspberry Pi official power adapter. Theoretically, any adapter with a USB-C cable that can plug into the Raspberry should work fine. In practice, it's better to get the official power adapter because it's been tested to deliver the exact power that the Raspberry Pi needs.
-  A microSD card. This tiny card will contain the operating system that your Raspberry Pi will run on.
-  (Optional) Heat sinks. These are little metal blocks that draw the heat away from the chips on the Raspberry Pi board. A Python program for this project should not heat the Raspberry Pi too much, but it is safe practice to use heat sinks.
-  (Optional) An external keyboard and a mouse. These two things are optional, because you can use your laptop keyboard and touchpad to issue commands to the Raspberry Pi computer.

To set up the Raspberry Pi:

-  A laptop (or desktop), with a microSD port. If your laptop does not have this port, you need a microSD card reader that you can plug into laptop. After the Raspberry Pi is set up and the photo frame is working, you'll no longer need the laptop.
-  Administrator privileges on the laptop, so that you can download all the required software on it.
-  An internet connection. After the set up is complete, this project does not need an internet connection.

## Steps

You make the Raspberry Pi ready by installing an operating system on it, and write a script to play the chimes.

Here are the step-by-step guides for these tasks:

1.  (Optional) [Fix the heat sinks](pi_4_attach_heatsink.md) on the Raspberry Pi.
1.  [Make your laptop ready](set_up_laptop.md) for setting up the Raspberry Pi.
1.  [Install an operating system](pi_4_install_os.md) on the Raspberry Pi.
1.  Write the Python code for [playing the chimes](python_clock_chime.md) every hour and every half hour.

{% include mermaid_clock_chime_flowchart.md %}

## Cost

All figures are in Indian Rupees (INR), and inclusive of GST (goods and service tax).

| Item | Amount (INR) |
| :---- | -----------: |
| Raspberry Pi 4 8GB **\*** | 8,999.00 |
| 15.3W USB-C Power Supply - Official (For Raspberry Pi 4) | 672.60 |
| Amazon Basics 32GB MicroSDHC Memory Card with Adapter | 369.00 |
| Aluminium Heat Sink | 35.40 |
| Honeywell Moxie V500 10W Portable USB Wired Soundbar **\*\*** | 789.00 |
| | **10,865.00**|

**\*** You can also use a Raspberry Pi 4 model with lesser RAM. One with 1GB, which is sufficient to run the chiming script, costs INR 3,599.00, which is almost 30% cheaper than the model used in this tutorial. You can use an older Raspberry Pi model too, so long as you can plug a 3.5 mm audio jack in it. Here are some options:
-  Raspberry Pi Zero 2W (INR 1,569.00), with a USB2-to-audio-port coupler. Alternatively, use the mini-HDMI port to connect to a monitor that has inbuilt speakers.
-  Raspberry Pi 3A (INR 2,559.00) or Raspberry Pi 3B (INR 3,598.00), which already have an audio port.

**\*\*** You can use any externally powered speaker that has a 3.5 mm audio jack.

## Alternatives

A battery-operated grandfather clock, like [this one from Titan](https://www.amazon.in/Titan-Classic-Colour-Pendulum-Westminster/dp/B0BDRQMRZY/ref=sr_1_34).