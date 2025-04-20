---
layout: template_generalFiles
title: Security camera
description: Surveillance camera setup with Raspberry Pi Zero and Camera Module 3
created: Apr 20, 2025
updated: Apr 20, 2025
---

# {{ page.title }}

Now that your surveillance camera is working, consider the following enhancements.

-  [Never lose a frame](#never-lose-a-frame)
-  [Keep cool](#keep-cool)

## Never lose a frame

You might have noticed that the videos have timestamps like this:

```
ve_20250420_122534.h264
ve_20250420_122644.h264
ve_20250420_122753.h264
ve_20250420_122903.h264
```

You're losing about 9 to 10 seconds between each video.

```
ve_20250420_122534  → 12:25:34
ve_20250420_122644  → 12:26:44  → +1 min 10 sec
ve_20250420_122753  → 12:27:53  → +1 min 9 sec
ve_20250420_122903  → 12:29:03  → +1 min 10 sec
``` 


Even though you're capturing 1-minute videos, the next one doesn't start immediately at the end of the previous one. Rather, there's a small delay while one `libcamera-vid` command finishes and the next one starts. But a lot can happen in 10 seconds! To not lose any frames, use a background recording, by tweaking the bash script a bit.

```
#!/bin/bash
SAVE_PATH="/home/oracle/Videos"
mkdir -p "$SAVE_PATH"

while true; do
  TIMESTAMP=$(date +%Y%m%d_%H%M%S)
  libcamera-vid --nopreview --width 640 --height 480 --bitrate 1000000 --timeout 60000 -o "$SAVE_PATH/ve_$TIMESTAMP.h264" &
  wait
done
``` 

Notice the following difference:

```
  libcamera-vid --nopreview --width 640 --height 480 --bitrate 1000000 --timeout 60000 -o "$SAVE_PATH/ve_$TIMESTAMP.h264" &
  wait

```

Here:

-  `----timeout 60000`: This sets how long the video recording lasts in milliseconds. 60000 ms means 60 seconds (1 minute). You can change this to however long you want each video segment to be.
-  `&`: This little symbol at the end means the command should be run in the background, so that the script doesn't pause while the video is recording; rather, it moves on and prepares for the next loop.
-  `wait`: This pauses the script for the timeout duration until tha background command finishes. When the video recording ends, the script continues.

This change slightly reduces how long it takes for the next loop to begin. It is by no means seamless, but it at least reduces the 10s delay to about 2s to 3s.

## Keep cool

Security cameras don't sleep. This means that the Raspberry Pi computer will be running continuously, days on end. If you live in an area like mine, where summer temperatures can cross 50 degrees Centigrade, you'd like to ensure that the camera hanging outside doesn't get too hot (Lakshman was known to be extremely hot-tempered). Consider using an [aluminium heat sink](https://www.waveshare.com/zero-heatsink.htm) made specially for Raspberry Pi Zero W.