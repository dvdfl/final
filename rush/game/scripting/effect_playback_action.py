from game.scripting.action import Action
from constants import *

class EffectPlaybackAction(Action):

    def __init__(self, audio_service, effect_filename):
        self._audio_service = audio_service
        self._effect_filename = effect_filename
        self._already_played = False
        
    def execute(self, cast, script, callback):
        if not self._already_played:
            self._audio_service.play_sound_from_assets(self._effect_filename)
            self._already_played = True