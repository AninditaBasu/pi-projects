#!/bin/bash
SAVE_PATH="/home/oracle/Videos"
mkdir -p "$SAVE_PATH"

while true; do
  TIMESTAMP=$(date +%Y%m%d_%H%M%S)
  libcamera-vid --nopreview --width 640 --height 480 --bitrate 1000000 --timeout 60000 -o "$SAVE_PATH/ve_$TIMESTAMP.h264" &
  wait
done