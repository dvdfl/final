from game.scripting.action import Action
from constants import *

class MusicPlaybackAction(Action):

    def __init__(self, audio_service):
        self._audio_service = audio_service
        self._is_music_playing = False
        
    def execute(self, cast, script, callback):
        if not self._is_music_playing:
            self._audio_service.start_music_from_assets(BACKGROUND_MUSIC)
        
        self._audio_service.playback_music_buffer()