# songs.py

import pywhatkit
import webbrowser

songs_dict = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "calm down": "https://www.youtube.com/watch?v=WcIcVapfqXw"
}

def play_song(song_name, speak):
    for key in songs_dict:
        if key in song_name:
            speak(f"Playing {key} from your playlist.")
            webbrowser.open(songs_dict[key])
            return
    
    # Auto-play top YouTube result
    speak(f"Playing {song_name} on YouTube.")
    pywhatkit.playonyt(song_name)
