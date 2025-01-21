---
layout: template_generalFiles
title: Write the Python code for displaying the photos
description: Pull photos from a local storage (SD card, USB drive) or cloud storage, and display them with a time lag on a Raspberry Pi 3B+.
---

{% include mermaid_photo_frame.md %}

# {{ page.title }}

A digital photo frame reads photo files from a storage device, and displays them on the screen for a specified time. For the photo frame that you're building, this job will be done by a Python program.

The operating system that you installed on the Raspberry Pi already includes Python, as well as an integrated development environment (IDE) that makes it easier for you to write, run, and edit Python programs. This IDE is the Thonny IDE. You'll use Thonny to write the photo frame program.

1.  Switch on the Raspberry Pi.
1.  Download any updates to the operating system by running the following command: `sudo apt-get update`.
1.  Apply these downloads to the operating system by running the following command: `sudo apt-get upgrade`.
1.  Open Thonny by clicking the Raspberry Pi icon near the top left, and then clicking **Programming > Thonny**.
1.   

<hr/>

## The code

```python
{% include pyscript_photo_frame.py %}
```

> You can also [download the raw Python file](https://raw.githubusercontent.com/AninditaBasu/pi-projects/refs/heads/main/_includes/pyscript_photo_frame.py).

## The explanation

