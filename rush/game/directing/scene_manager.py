from constants import *
from game.casting.car import Car
from game.casting.body import Body
from game.casting.road import Road
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.stats import Stats
from game.casting.text import Text
from game.scripting.change_scene_action import ChangeSceneAction
# from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_traffic_action import CollideTrafficAction
from game.scripting.control_car_action import ControlCarAction
from game.scripting.control_traffic_action import ControlTrafficAction
from game.scripting.draw_car_action import DrawCarAction
from game.scripting.draw_road_action import DrawRoadAction
from game.scripting.draw_traffic_action import DrawTrafficAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.effect_playback_action import EffectPlaybackAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_car_action import MoveCarAction
from game.scripting.move_traffic_action import MoveTrafficAction
# from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
# from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.scripting.music_playback_action import MusicPlaybackAction


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""

    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    # CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE)
    COLLIDE_TRAFFIC_ACTION = CollideTrafficAction(PHYSICS_SERVICE)
    CONTROL_CAR_ACTION = ControlCarAction(KEYBOARD_SERVICE)
    CONTROL_TRAFFIC_ACTION = ControlTrafficAction()

    DRAW_CAR_ACTION = DrawCarAction(VIDEO_SERVICE)
    DRAW_ROAD_ACTION = DrawRoadAction(VIDEO_SERVICE)
    DRAW_TRAFFIC_ACTION = DrawTrafficAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_CAR_ACTION = MoveCarAction()
    MOVE_TRAFFIC_ACTION = MoveTrafficAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:
            self._prepare_game_over(cast, script)

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------

    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_score(cast)
        self._add_car(cast)
        self._add_dialog(cast, ENTER_TO_START)
        self._add_road_walls(cast)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        script.add_action(CUSTOM, MusicPlaybackAction(self.AUDIO_SERVICE))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_next_level(self, cast, script):
        self._add_car(cast)
        script.clear_actions(INPUT)
        #script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        self.prepare_scene(IN_PLAY, cast, script)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_CAR_ACTION)

        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        # script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(CUSTOM)
        script.add_action(CUSTOM, EffectPlaybackAction(self.AUDIO_SERVICE, CRASH))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    def _add_car(self, cast):
        cast.clear_actors(CAR_GROUP)
        x = CENTER_X - CAR_WIDTH / 2
        y = SCREEN_HEIGHT - CAR_HEIGHT - 10
        position = Point(x, y)
        size = Point(CAR_WIDTH, CAR_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(CAR_IMAGE)
        car = Car(body, image)
        cast.add_actor(CAR_GROUP, car)

    def _add_road_walls(self, cast):
        cast.clear_actors(ROAD_GROUP)

        # LEFT WALL
        left_road_image = ROAD_IMAGES['left']
        right_road_image = ROAD_IMAGES['right']

        x = 0
        y = 0

        position = Point(x, y)
        size = Point(left_road_image['width'], left_road_image['height'])
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(left_road_image['path'])
        left_wall = Road(body, image, True)

        cast.add_actor(ROAD_GROUP, left_wall)

        # RIGHT WALL
        x = SCREEN_WIDTH - right_road_image['width']
        y = 0

        position = Point(x, y)
        size = Point(right_road_image['width'], right_road_image['height'])
        velocity = Point(0, 0)
        right_body = Body(position, size, velocity)
        right_image = Image(right_road_image['path'])
        right_wall = Road(right_body, right_image, True)

        cast.add_actor(ROAD_GROUP, right_wall)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)

    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_ROAD_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_CAR_ACTION)
        script.add_action(OUTPUT, self.DRAW_TRAFFIC_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)

    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)

    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.CONTROL_TRAFFIC_ACTION)
        script.add_action(UPDATE, self.MOVE_CAR_ACTION)
        script.add_action(UPDATE, self.MOVE_TRAFFIC_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_TRAFFIC_ACTION)
        # script.add_action(UPDATE, self.CHECK_OVER_ACTION)
