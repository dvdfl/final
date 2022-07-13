import pyray
import os
import pathlib

class RaylibAudioService:
    """ A Raylib implementation of AudioService."""

    def initialize(self):
        pyray.init_audio_device()
        self._sounds = {}
        self._current_music = None

    def load_sounds(self, directory, load_as_music):
        filepaths = self._get_filepaths(directory, [".ogg", ".wav"])
        for filepath in filepaths:
            if filepath not in self._sounds.keys():
                if(not load_as_music):
                    sound = pyray.load_sound(filepath)
                else:
                    sound = pyray.load_music_stream(filepath)
                
                self._sounds[str(pathlib.Path(filepath))] = (sound, load_as_music)

    def play_sound_from_assets(self, filename):
        sound = self._sounds[str(pathlib.Path(filename))]

        if not sound[1]:
            pyray.play_sound(sound[0])
        else:
            raise TypeError()

    def start_music_from_assets(self, filename):
        sound = self._sounds[str(pathlib.Path(filename))]

        if sound[1]:
            self._current_music = sound[0]
            pyray.play_music_stream(sound[0])
        else:
            raise TypeError()
        
    def stop_current_music(self):
        if self._current_music is not None:
            pyray.stop_music_stream(self._current_music)

    def playback_music_buffer(self):
        pyray.update_music_stream(self._current_music)

    def release(self):
        pyray.close_audio_device()

    def _get_filepaths(self, directory, filter):
        filepaths = []
        for file in os.listdir(directory):
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
        return filepaths
