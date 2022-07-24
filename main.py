#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import time

import board
import neopixel
pixel_pin = board.D21
num_pixels = 7
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.9, auto_write=False, pixel_order=ORDER
)

from led_test import rainbow_cycle

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="b8238df70dbf43e0b71ad9c77b00e04a"
CLIENT_SECRET="8efe23e074d94dcbb7e3be80ec3b9174"

rainbow_cycle(0.003)  # rainbow cycle with 1ms delay per step
time.sleep(1)
pixels.fill((0, 0, 0))
pixels.show()

passenger = 154263183460
come_from_away = 838186393673
dodie = 634963910889
lucy = 358005825702
v = 494303731913
volume_3 = 291047694379
volume_2 = 425282461896
volume_1 = 1044730765411



while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        current_id = None
        sp.transfer_playback(device_id=DEVICE_ID, force_play=False) 
        while True:
            sleep (2)
            print("Waiting for record scan...")
            id= reader.read()[0]

            
#             pixels.fill((159, 226, 191))
#             pixels.show()
#             print("backlight on")

            print("Card Value is:",id)
            print("Current ID is:",current_id)
 
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            if (id==passenger and current_id !=passenger):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:37i9dQZF1DZ06evO05fCDu')
                current_id = passenger
                pixels.fill((255, 75, 0))
                pixels.show()
                sleep(2)
                
            elif (id==come_from_away and current_id != come_from_away):

                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6SisHkIpxo4JN5kRcBEv9Z')
                current_id = come_from_away
                pixels.fill((35, 83, 155))
                pixels.show()
                sleep(2)
                
            elif (id==dodie and current_id != dodie):

                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:37i9dQZF1DZ06evO19h0GO')
                current_id = dodie
                pixels.fill((255, 255, 0))
                pixels.show()
                sleep(2)
                
            elif (id==v and current_id != v):

                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:60jW88F1DKAuJ3FM5sVkMM')
                current_id = v
                pixels.fill((189, 5, 1))
                pixels.show()
                sleep(2)
                
            elif (id==volume_3 and current_id != volume_3):

                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:6oCgfSoejr7GypocEELq4a')
                current_id = volume_3
                pixels.fill((77, 158, 58))
                pixels.show()
                sleep(2)
                
            elif (id==volume_1 and current_id != volume_1):

                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:2DigbtNaXBNdVlgJ4n5XnA')
                current_id = volume_1
                pixels.fill((242, 124, 12))
                pixels.show()
                sleep(2)
                
            elif (id==volume_2 and current_id != volume_2):

                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:4tCN6uwVLz1pmx1vNrEANP')
                current_id = volume_2
                pixels.fill((77, 255, 25))
                pixels.show()
                sleep(2)
                
            elif (id==lucy and current_id != lucy):

                # playing a song
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:37i9dQZF1DZ06evO2fcjIt')
                current_id = lucy
                pixels.fill((255, 0, 0))
                pixels.show()
                sleep(2)
                
#             elif (id==come_from_away and current_id != come_from_away):
# 
#                 # playing a song
#                 sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2eAvDnpXP5W0cVtiI0PUxV'])
#                 current_id = come_from_away
#                 sleep(2)
#                 
#             elif (id==come_from_away and current_id != come_from_away):
# 
#                 # playing a song
#                 sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2eAvDnpXP5W0cVtiI0PUxV'])
#                 current_id = come_from_away
#                 sleep(2)
#                 
#             elif (id==209374225414):
#                 
#                 # playing an album
#                 sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:6oCgfSoejr7GypocEELq4a')
#                 sleep(2)
            
            # continue adding as many "elifs" for songs/albums that you want to play
            
            else:
                print("pass")
                pass

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()