---
layout: template_generalFiles
title: Attach a touch display to Raspberry Pi 3B+
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+.
---

# {{ page.title }}

The Raspberry Pi is what they call an SBC (a single board computer). It has neither a screen where you can see the output of your commands, nor a keyboard through which you can issue commands. It is just a barebones computer, with no peripheral devices such as keyboard, mouse, monitor, speaker, or microphone. To use a Raspberry Pi as a computer, you must manually attach these peripherals to it. In this tutorial, you're building a photo frame, so the barest minimum peripheral device that you need is a screen.

This is what I started with.

| Front view | Back view |
| ---------- | --------- |
| ![View from the front](../images/frame_front.jpeg "View from the front") |![View from the back](../images/frame_back.jpeg "View from the back") |

To mount the display screen on to the computer board, you loosen the four screws at the four ends of the board at the back of the frame, place the Raspberry Pi on to it, and put the screws back in place. You then connect these two objects by means of two wires (red and black) and a cable (the white straight strip). You don't need the shiny curved strip also shown in the picture; it came as standard packaging with the display and is used in Raspberry Pi 4 models. The model being used here is Raspberry Pi 3B+, though, so the straight white strip is the one to use.

How to attach the display screen to the computer board is explained well in this YouTube video: 

<iframe width="560" height="315" src="https://www.youtube.com/embed/SyhJctufiRI?si=Hv3bjPuczohvv8ES" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

If you'd rather read some written instructions rather than watch a video, see this official guide from the good folks at Raspberry Org: [Touch Display](https://www.raspberrypi.com/documentation/accessories/display.html).

After the display screen is mounted on the computer board, affix the heat sinks to the board.
