---
layout: template_generalFiles
title: Fix heat sinks to Raspberry Pi 3B+
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+.
---

# {{ page.title }}

A heat sink is a metal square object that is attached to a RAspberry Pi board by means of thermal paste. It draws the heat away from the processor, and the controllers for the USB and ethernet. A photo frame program running on a Raspberry Pi 3B+ should not heat the little computer too much, but it is safe practice to use heat sinks. The three small corrugated squares that you see in the bottom quadrant of the image are the heat sinks. 

<img src="../images/frame_front.jpeg" width="75%" />

Notice that the image has three heat sinks.  A Raspberry Pi Model 3B+ needs only two of those. It's the Raspberry Pi 4 model that would've needed all three heat sinks, but because these heat sinks hardly cost anything, shops in my corner of the world usually sell them in sets of 3.

For your photo frame project, you must attach a heat sink each to the CPU chip and the network chip of the Pi board. The one that goes over the CPU chip is the larger one; the one to use on the ethernet board is the smaller one.
 
1.  Peel off the adhesive strip at the back of the heat sink, all the while taking care that you don't touch the sticky part that the strip was covering. The sticky part is the thermal paste that will hold the sink in place.
1.  Press the sink ever so slightly on to the chip on the Pi board.

<hr/>

Here's an YouTube video that shows you the steps in detail:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Xg5n56x9Y7A?si=tw5MF9EhXMR4aG-e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

After the heat sinks are in place:

-  If you already have an external keyboard and mouse, [install an operating system](pi_3b_install_os.md) on your Raspberry Pi.
-  If you don't have an external keyboard and mouse (or if you want to do this step anyway because there's no harm if you do), [set up Pi Connect](pi_piconnect.md).