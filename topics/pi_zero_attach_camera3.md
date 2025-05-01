---
layout: template_generalFiles
title: Attach Camera Module 3 to Raspberry Pi Zero W
description: Attach the camera module to the Raspberry Pi Zero by using the golden cable.
pimodel: Raspberry Pi Zero W
created: Apr 20, 2025
updated: Apr 25, 2025
---

{% include mermaid_security_cam_flowchart.md %}

# {{ page.title }}

The 12-megapixel Camera Module 3 is the latest official camera module. 

<a href = "../images/camera_3_cables.jpeg"><img src = "../images/camera_3_cables.jpeg" width="50%" /></a><br/>
<span style="font-size:75%;">To see a larger image, click the image.</span>

When you buy the camera module, you get two connector cables:
-  A white one, which is a 40-pin-to-40-pin cable and made for the Raspberry Pi 3 and Raspberry Pi 4 models.
-  A golden one, which is a 40-pin-to-22-pin cable and made for the Raspberry Pi 5 and Raspberry Pi Zero models.

In the image, you also see a shorter golden cable. I bought this separately; it's also a 40-pin-to-22-pin cable but shorter.

For this project, you must attach the camera module to the {{page.pimodel}} with the golden cable.
 
1.  Turn the camera module upside down, with the lens facing down. You see a metal clip. Loosen the clip by pulling down the two tiny clamps at the ends.
1.  Insert the broad end of the golden cable into this clip, taking care that the metal connectors are facing down (that is, towards the lens side). <img src = "../images/camera3_1.jpeg" width="50%" />
1.  Push the clamps down, so that the clip sits firmly back in its place.
1.  On the {{page.pimodel}}, pull out the camera clip. It's located near the power port.
1.  Insert the narrower end of the cable, with the metal connectors facing the bottom side of the Raspberry Pi. Push the clamps down firmly.
1.  Verify that the camera is working as expected:
    1.  Switch on the Raspberry Pi.
	1.  Open a terminal window and run the following command: `libcamera-jpeg -o test.jpg`.
1.  Open **File Manager** (it's one of the icons near the top). You should see a file called `test.jpg`. This means that the camera module was detected and is working fine.
1.  If you're not immediately proceeding to the next step, shut down the Raspberry Pi by typing the following command on the terminal: `sudo shutdown -h now`. You should be disconnected from Raspberry Pi and the terminal window should disappear.  Wait till the green light on the Raspberry Pi board stops flashing, and then switch off the power supply.

<hr/>

I found this [YouTube video](https://www.youtube.com/watch?v=uWOlf4aECC8) to be helpful; it shows which clips to pull, push, and connect to.

<hr/>

After the camera is in place, [write the bash code](bash_security_camera.md) for the surveillance setup.
