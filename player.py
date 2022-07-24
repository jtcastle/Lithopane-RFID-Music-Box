#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="b8238df70dbf43e0b71ad9c77b00e04a"
CLIENT_SECRET="8efe23e074d94dcbb7e3be80ec3b9174"

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)  
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            if (id==207249286224):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2eAvDnpXP5W0cVtiI0PUxV'])
                                                            #https://open.spotify.com/track/2eAvDnpXP5W0cVtiI0PUxV?si=37cddc3eaba246bb
                sleep(2)
                
            elif (id==209374225414):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:6oCgfSoejr7GypocEELq4a')
                sleep(2)
                
            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()