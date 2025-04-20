---
layout: template_generalFiles
title: Security camera
description: Surveillance camera setup with Raspberry Pi Zero and Camera Module 3
created: Apr 20, 2025
updated: Apr 20, 2025
---

# {{ page.title }}

Lakshman, as the story goes, didn't sleep a wink for 14 years. During the day, he'd hunt with his elder brother, the exiled prince Ram, and during the night, he'd stand outside the leaf-hut he'd built for the prince and his wife, keeping an eye out for wandering evil elements. 

What if you too had your very own kid brother, like Lakshman, constantly keeping vigil outside your door?


<video width="40%" height="40%" controls>
  <source src="../images/security_camera.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> 

In this tutorial, I show you how to use a Raspberry Pi Zero WH computer and a Camera Module 3 to build a surveillance camera. Along the way, I explain how to set up a headless Raspberry Pi computer, and write a bash script on it.

-  [Materials](#materials)
-  [Steps](#steps)
-  [Cost](#cost)
-  [Alternatives](#alternatives)

<hr/>

## Materials

For the security camera:

-  A Raspberry Pi Zero W computer. This little computer board will hold the code that makes the chimes ring out every half hour and hour. The Raspberry Pi Zero is the smallest computer in the Raspberry Pi stable, and it is good enough for this project.
-  A Raspberry Pi Camera Module 3. For this project, I could've used an older camera module such as the Camera Module 2, which is lighter on the system resources (and the Raspberry Pi Zero hardly has any), but it doesn't support the `libcamera` package, which is going to be the officially supported package now .
-  A Raspberry Pi official power adapter. Theoretically, any adapter with a microUSB cable that can plug into the Raspberry Pi should work fine. In practice, it's better to get the official power adapter because it's been tested to deliver the exact power that the Raspberry Pi needs.
-  A microSD card. This tiny card will contain the operating system that your Raspberry Pi will run on.
-  (Optional) An external keyboard and a mouse. These two things are optional, because you can use your laptop keyboard and touchpad to issue commands to the Raspberry Pi computer.

To set up the Raspberry Pi:

-  A laptop (or desktop), with a microSD port. If your laptop does not have this port, you need a microSD card reader that you can plug into laptop. After the Raspberry Pi is set up and the photo frame is working, you'll no longer need the laptop.
-  Administrator privileges on the laptop, so that you can download all the required software on it.
-  An internet connection. After the set up is complete, this project does not need an internet connection.

## Steps

You make the Raspberry Pi ready by installing an operating system on it, and write a script to play the chimes.

Here are the step-by-step guides for these tasks:

1.  [Make your laptop ready](set_up_laptop.md) for setting up the Raspberry Pi.
1.  [Install an operating system](pi_zero_install_os.md) on the Raspberry Pi.
1.  Write the bash script code for recording videos.
1.  (Optional) Refine the project.

{% include mermaid_security_cam_flowchart.md %}

## Cost

All figures are in Indian Rupees (INR), and inclusive of GST (goods and service tax).

| Item | Amount (INR) |
| :---- | -----------: |
| Raspberry Pi Zero WH| 1,728.33 |
| 12.75W Micro USB Power Supply - Official | 720.88 |
| SanDisk 32GB MicroSDHC Memory Card | 418.35 |
| Raspberry Pi Camera Module 3 | 2,819.64 |
| | **5,687.20**|


## Alternatives

Any of the plug-and-play security cameras available off the shelf. They're more expensive, but have all the bells and whistles.