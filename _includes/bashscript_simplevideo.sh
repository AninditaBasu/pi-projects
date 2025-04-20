#!/bin/bash
SAVE_PATH="/home/oracle/Videos"
mkdir -p "$SAVE_PATH"

DURATION=$((60 * 1000))  # 1 minute in milliseconds
while true; do
  TIMESTAMP=$(date +%Y%m%d_%H%M%S)
  libcamera-vid --nopreview --width 640 --height 480 --bitrate 1000000 --timeout $DURATION -o "$SAVE_PATH/ve_$TIMESTAMP.h264"
done