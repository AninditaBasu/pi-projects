---
layout: template_generalFiles
title: Security system
description: Surveillance setup with Raspberry Pi Zero W and Camera Module 3
created: Apr 20, 2025
updated: May 3, 2025
---

# {{ page.title }}

Lakshman<sup>\*</sup>, as the story goes, didn't sleep a wink for 14 years. During the day, he'd hunt with his elder brother, the exiled prince Ram, and during the night, he'd stand outside the leaf-hut he'd built for the prince and his wife, keeping an eye out for wandering evil elements. 

What if you too had your very own kid brother, like Lakshman, constantly keeping vigil outside your door?

<table>
<tr>
<th>Interior</th><th>Exterior</th>
</tr>
<tr>
<td>
<video width="40%" height="40%" controls>
  <source src="../images/security_cam_interior.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
</td>
<td>
<video width="60%" height="60%" controls>
  <source src="../images/security_cam_exterior_longshot.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
</td>
</tr>
</table>
 

In this tutorial, I show you how to use a Raspberry Pi Zero WH computer and a Camera Module 3 to build a surveillance camera. Along the way, I explain how to set up a headless Raspberry Pi computer, and write a bash script on it.

-  [Materials](#materials)
-  [Steps](#steps)
-  [Cost](#cost)
-  [Alternatives](#alternatives)

<hr/>

## Materials

For the security camera:

-  A Raspberry Pi Zero WH computer. This little computer board will hold the code that makes the videos of your surroundings. The Raspberry Pi Zero is the smallest computer in the Raspberry Pi stable, and it is good enough for this project. The *W* in the name means it is WiFi enabled. The *H* in the name means the header pins are soldered into the Raspberry Pi board. This project does not need the *H* version but I got one just in case I want to use the header pins for something later.
-  A Raspberry Pi Camera Module 3. For this project, I could've used an older camera module such as the Camera Module 2, which is lighter on the system resources (and the Raspberry Pi Zero hardly has any), but it doesn't support the `libcamera` package, which is going to be the officially supported package now .
-  A Raspberry Pi official power adapter. Theoretically, any adapter with a microUSB cable that can plug into the Raspberry Pi should work fine. In practice, it's better to get the official power adapter because it's been tested to deliver the exact power that the Raspberry Pi needs.
-  A microSD card. This tiny card will contain the operating system that your Raspberry Pi will run on.

To set up the Raspberry Pi:

-  A laptop (or desktop), with a microSD port. If your laptop does not have this port, you need a microSD card reader that you can plug into laptop. After the Raspberry Pi is set up and the camera is working, you'll no longer need the laptop unless you want to access the setup again.
-  Administrator privileges on the laptop, so that you can download all the required software on it.
-  An internet connection. After the set up is complete and the camera switched on, this project does not need an internet connection till you access the setup again to transfer video files to another computer.

## Steps

You make the Raspberry Pi ready by installing an operating system on it, and write a script to continuously record videos.

Here are the step-by-step guides for these tasks:

1.  [Make your laptop ready](set_up_laptop.md) for setting up the Raspberry Pi.
1.  [Install an operating system](pi_zero_install_os.md) on the Raspberry Pi.
1.  [Write the bash script](bash_security_camera.md) for recording videos.
1.  (Optional) [Refine the project](security_camera_refine.md).

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

Any of the plug-and-play security cameras available off the shelf. They may or may not be more expensive, and might have all the bells and whistles.

The push for this project came from two factors:

-  The unavailablity ("temporary", I was told for 3 months before I lost patience) of a branded security camera solution from a well-known telecom company.
-  My unwillingness to go in for the easily available off-the-shelf security cameras. These are all local brands and do not guarantee good performance.

<hr>

\*: Lakshman is a prince of Ayodhya and a younger brother to the heir, Ram, according to the Indian epic, Ramayana. When Ram and his wife Sita were exiled, Lakshman accompanied them to keep guard.