---
layout: template_generalFiles
title: Install an operating system on Raspberry Pi 3B+
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+.
pimodel: Raspberry Pi 3
baseos: Debian Bookworm
pios: Raspberry Pi OS 64-bit (A port of Debian Bookworm with the Raspberry Pi Desktop)
created: Jan 18, 2025
updated: Jan 24, 2025
---

{% include mermaid_photo_frame_flowchart.md %}

# {{ page.title }}

Do you see the black microSD card near the bottom center of the image, right next to the three heat sinks? 

<a href = "../images/pi_3.jpeg"><img src = "../images/pi_3.jpeg" width="50%" /></a><br/>
<span style="font-size:75%;">To see a larger image, click the image.</span>

The operating system will be downloaded on to that card, which will then be inserted into the microSD slot of the Raspberry Pi. That's what will get this little computer up and running, and make it available for you for the final steps of your project.

<hr/>

## Steps

{% include install_os.md %}
1.  Insert the microSD card to the Raspberry Pi's board, plug in the power adapter to a wall socket, and insert the cable into the USB-C power slot of the Raspberry Pi. If you're going to use an external keyboard and mouse, insert the USB receivers for these devices into the USB ports of the Raspberry Pi.
1.  Turn on the power switch of the wall socket. The light on the Raspberry Pi board should glow green, and the display screen should first show a rectangle of rainbow colours, and then finally show you the Raspberry Pi desktop screen.
1.  If you don't have an external keyboard and mouse, log in to the Raspberry Pi from your laptop:
    1.  Find the IP address of your nework gateway. To do so, on your laptop, open the command prompt, and type `ipconfig`. Then, note down the value that's displayed as **Default Gateway**.
    1.  Start Angry IP Scanner. For the first box in the **IP Range** field, specify the value of the default gateway that you noted down in the previous step. For the second field, specify a number that's about 15-20 stops away. For example, if your default gateway is `192.168.4.1`, specify the end range to be something around `192.168.4.15`, so that the scan doesn't take too long. (The assumption here is that you don't already have more than 15-20 devices connected to your network!) Click **Start** and wait for the scan to be over. Then, in the **Hostname** column, look for the name of your Raspberry Pi. This is the name that you specified as the hostname in the OS Customisation settings while downloading the operating system on the microSD card. When you've spotted this hostname, look for the entry in the **IP** column. You need this value in the next step.
	1.  On your laptop, start PuTTY and enter the IP address of your Raspberry Pi. This is the value that you noted down in your previous step. Click **Open**. When prompted for login credentials, enter the user name and password that you specified in the OS Customisation settings while downloading the operating system on the microSD card. You should now see a prompt like this: `<hostname>@<username>:~ $`. For example, if your hostname is `delphi` and user name is `oracle`, you'll see `delphi@oracle:~ $`It means you're now logged in to your Raspberry Pi and everything's working as expected.
1.  Update the operating system that you installed on the microSD card. You used Raspberry Pi Imager for downloading the operating system but it might not contain the latest patches, fixes, and upgrades. Pull these things in:
    1.  Open a terminal window. If you're logged in through your laptop, you're already in the terminal window. If you're using an external keyboard and mouse, move the mouse over the icons at the top left, locate the one labelled **Terminal**, and click it.
    1.  To see if there are any updates to the operating system, run the following command: `sudo apt-get update`. The local cache of the Raspberry Pi is updated with the package information for the package repositories. You're shown a list of the these packages, and now it's up to you to upgrade them to their latest versions.
    1.  Upgrade the software shown on the list by running the following command: `sudo apt-get upgrade`. When prompted for permission to proceed with the upgrade, answer in the affirmative. The actual updates for the installed software and the operating system are now downloaded and installed on your Raspberry Pi.	
1.  If you don't have an external mouse or keyboard, set up Raspberry Pi Connect so that you can control the Raspberry Pi through a laptop through the Raspberry Pi's desktop GUI itself. You're already logged into the Raspberry Pi through your laptop via SSH, but you can use only the terminal window when you're so logged in; you can't use the Raspberry Pi's desktop GUI. With the Connect software, you can log into your Raspberry Pi through any browser, and use it through its desktop environment.
    1.  Install Connect by running the following command in the terminal window: `sudo apt install rpi-connect`.
	1.  Start Connect by running the following command in the terminal: `rpi-connect on`.
	1.  Generate a link that will connect your Raspberry Pi computer with your Connect account by running the following command from the terminal: `rpi-connect signin`. You're shown a sign-in URL on the terminal.
	1.  On your laptop, open a browser, type the URL shown on the Raspberry Pi terminal window, and follow the onscreen prompts to complete the signin and authentication process.
	1.  In the same browser window, specify a name to identify your device, and click **Create device and sign in**. 
1.  If you're not immediately proceeding to the next step (where you write the Python program), shut down the Raspberry Pi.
    1.  If you're using an external mouse, close the terminal window. Then click the Raspberry Pi icon near the top left and click **Shutdown > Shutdown**. Wait till the green light on the Raspberry Pi board stops flashing, and then switch off the power supply.
	1.  If you're logged in through your laptop, type the following command on the terminal: `sudo shutdown -h now`. You should be disconnected from Raspberry Pi and the terminal window should disappear.  Wait till the green light on the Raspberry Pi board stops flashing, and then switch off the power supply.

Now that your Raspberry Pi is ready to be used as a computer, you can proceed to creating the Python script that [displays your photo collection](python_photo_frame.md).

