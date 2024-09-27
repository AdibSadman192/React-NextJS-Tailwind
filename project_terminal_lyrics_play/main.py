import lyricsgenius
import time

# Replace 'your_genius_api_token' with your actual Genius API token
genius = lyricsgenius.Genius("gEfpu5kISsTt_lCx6gfXWRvyXYfR2qPKn4H1X4XUIq9DjpEefqc9laDdqkTSdqrf")

def get_lyrics(song_title, artist_name):
    song = genius.search_song(song_title, artist_name)
    if song:
        return song.lyrics
    else:
        return "Lyrics not found."

def display_lyrics(lyrics):
    for line in lyrics.split('\n'):
        print(line)
        time.sleep(2)  # Adjust the delay as needed

if __name__ == "__main__":
    song_title = input("Enter the song title: ")
    artist_name = input("Enter the artist name: ")
    
    lyrics = get_lyrics(song_title, artist_name)
    display_lyrics(lyrics)