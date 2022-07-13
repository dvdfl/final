from constants import *
from game.casting.cast import Cast
from game.scripting.script import Script
from game.directing.scene_manager import SceneManager

class Director():
    def __init__(self, video_service, audio_service):

        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._audio_service = audio_service
        self._cast = Cast()
        self._script = Script()
        self._scene_manager = SceneManager()
        
    def on_next(self, scene):
        """Overriden ActionCallback method transitions to next scene.
        
        Args:
            A number representing the next scene to transition to.
        """
        self._scene_manager.prepare_scene(scene, self._cast, self._script)
        
    def start_game(self):
        #initializing windows

        """Starts the game. Runs the main game loop."""
        self.on_next(NEW_GAME)
        self._execute_actions(INITIALIZE)
        self._execute_actions(LOAD)
        while self._video_service.is_window_open():
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)
            self._execute_actions(CUSTOM)
        self._execute_actions(UNLOAD)
        #self._execute_actions(RELEASE)
        self._audio_service.release()
        self._video_service.release()

    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script, self)          