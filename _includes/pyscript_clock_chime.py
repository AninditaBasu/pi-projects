import time
from datetime import datetime
import pygame

# Initialize pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
sound_file = 'ding.wav'
chime_sound = pygame.mixer.Sound(sound_file)

def play_chime(times):
    """Play the chime the specified number of times."""
    for _ in range(times):
        chime_sound.play()
        time.sleep(2)  # A 2-second delay between chimes

try:
    print('Chiming on the hour and half-hour. Press Ctrl+C to stop.')
    while True:
        now = datetime.now()
        current_minute = now.minute
        current_second = now.second

        if current_minute == 30:
            # Chime once for the half-hour
            print('Chiming once for the half-hour.')
            play_chime(1)
            # Sleep until the top of the next hour
            sleep_time = (60 - current_minute) * 60 - current_second
            time.sleep(sleep_time)
        elif current_minute == 0:
            # Chime the number of times equal to the hour
            chime_count = now.hour % 12 or 12  # Use 12 for midnight and noon
            print(f'Chiming {chime_count} times for the hour {now.hour}.')
            play_chime(chime_count)
            # Sleep until the half-hour
            sleep_time = 30 * 60 - current_second
            time.sleep(sleep_time)
        else:
            # Determine whether to sleep until the half-hour or the hour
            if current_minute < 30:
                sleep_time = (30 - current_minute) * 60 - current_second
            else:
                sleep_time = (60 - current_minute) * 60 - current_second
            time.sleep(sleep_time)

except KeyboardInterrupt:
    print('\nStopped chiming.')
