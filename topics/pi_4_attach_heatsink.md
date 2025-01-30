---
layout: template_generalFiles
title: Fix heat sinks to Raspberry Pi 4
description: Chime on the hour and the half hour
created: Jan 30, 2025
updated: Jan 30, 2025
---

{% include mermaid_clock_chime_flowchart.md %}

# {{ page.title }}

A heat sink is a metal square object that is attached to a Raspberry Pi board by means of thermal paste. It draws the heat away from the processor, the USB controller, and the ethernet controller. A chiming program running on a Raspberry Pi 4B should not heat the little computer too much, but it is safe practice to use heat sinks. 

The three small corrugated squares that you see at the bottom left of the image are heat sinks. In the Raspberry Pi world, these corrugations are known as fins.

<a href = "../images/pi_3.jpeg"><img src = "../images/pi_3.jpeg" width="50%" /></a><br/>
<span style="font-size:75%;">To see a larger image, click the image.</span>

You must attach heat sinks to the CPU chip, the USB chip, and the network chip of the Raspberry Pi board. The one that goes over the CPU chip is the largest one; the one to use on the ethernet board is the smallest one.
 
1.  Peel off the adhesive strip at the back of the heat sink, all the while taking care that you don't touch the sticky part that the strip was covering. The sticky part is the thermal paste that will hold the sink in place.
1.  Press the sink ever so slightly on to the chip on the Pi board.

<hr/>

Here's an YouTube video that shows you the steps in detail:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Xg5n56x9Y7A?si=tw5MF9EhXMR4aG-e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<hr/>

After the heat sinks are in place, [prepare your laptop](set_up_laptop.md) for the Raspberry Pi setup.
