from gmusicapi import Mobileclient
from vlc import EventType, Instance
from threading import Thread
import json
import os.path
import time

enable_display = True
if enable_display:
    import scrollphat
    scrollphat.set_brightness(5)

class Player(object):

    def __init__(self, email, password, device_id):
        self.api = Mobileclient()
        self.vlc = Instance()
        self.loaded_tracks = []
        self.playing = False
        self.thread_running = False
        
        self.api.login(email, password, device_id)
        if os.path.isfile("songs.json"):
            # Load from file
            print("Found songs data.")
            with open('songs.json') as input_file:
                self.song_library = json.load(input_file)
        else:
            self.song_library = self.api.get_all_songs()
            # Save to file
            with open('songs.json', 'w') as output_file:
                json.dump(self.song_library, output_file)    
        
    def load_playlist(self, name):
        name = name.strip().lower()
        print("Looking for...", name)
        if os.path.isfile("playlists.json"):
            # Load from file
            print("Found playlist data.")
            with open('playlists.json') as input_file:
                self.playlists = json.load(input_file)
        else:
            self.playlists = self.api.get_all_user_playlist_contents()
            # Save to file
            with open('playlists.json', 'w') as output_file:
                json.dump(self.playlists, output_file)
            
        self.loaded_tracks = []
        for playlist_dict in self.playlists:
            playlist_name = playlist_dict['name'].strip().lower()
            if (playlist_name == name) or (name in playlist_name):
                print("Found match...", playlist_dict['name'])
                for track_dict in playlist_dict['tracks']:
                    self.loaded_tracks.append(track_dict)
                return playlist_dict['name']
            else:
                print("Found...", playlist_dict['name'])
        return None
 
    def end_callback(self, event, track_index):
        if track_index < len(self.loaded_tracks):
            self.play_song(self.loaded_tracks[track_index])
            event_manager = self.player.event_manager()
            event_manager.event_attach(EventType.MediaPlayerEndReached, self.end_callback, track_index + 1)
            self.playing = True
        else:
            self.playing = False

    def start_playlist(self):
        if len(self.loaded_tracks) > 0:
            self.play_song(self.loaded_tracks[0])
        
            if len(self.loaded_tracks) > 1:
                event_manager = self.player.event_manager()
                event_manager.event_attach(EventType.MediaPlayerEndReached, self.end_callback, 1)
  
    def play_song(self, song_dict):
        stream_url = self.api.get_stream_url(song_dict['trackId'])
        self.player = self.vlc.media_player_new()
        media = self.vlc.media_new(stream_url)
        self.player.set_media(media)
        self.player.play()

        song_string = ""
        if (song_dict['source'] == '2'):
            song_string = self.get_song_details(song_dict)
        else:
            song_string = self.get_local_song_details(song_dict['trackId'])

        print("Playing...",song_string)
        
        if enable_display:
            scrollphat.clear()
            scrollphat.write_string(" "*5+song_string)

            if not self.thread_running:
                thread = Thread(target=self.scroll_string)
                thread.start()

        self.playing = True

    def scroll_string(self):
        self.thread_running = True
        while self.thread_running:
            scrollphat.scroll()
            time.sleep(0.1)

    def stop(self):
        if self.player != None:
            self.player.stop()
        if enable_display:
            scrollphat.clear()
        self.thread_running = False
        self.playing = False

    def get_local_song_details(self, track_id):
        for song_dict in self.song_library:
            if track_id == song_dict['id']:
                return song_dict['albumArtist']+" - "+song_dict['title']

    def get_song_details(self, song_dict):
        return song_dict['track']['albumArtist']+" - "+song_dict['track']['title']

