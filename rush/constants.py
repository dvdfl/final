from game.casting.color import Color
import pathlib

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Road Rush"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 800 #1040
SCREEN_HEIGHT = 600 #680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# DIRECTORIES
ASSETS_DIR = f'{pathlib.Path(__file__).parent.resolve()}/assets'
IMAGES_PATH = f"{ASSETS_DIR}/images"

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONTS_PATH = f"{ASSETS_DIR}/fonts" 
FONT_FILE = FONTS_PATH + "/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
SOUNDS_PATH = f"{ASSETS_DIR}/sounds"
EFFECTS_PATH = f"{ASSETS_DIR}/sounds/effects"
MUSIC_PATH = f"{ASSETS_DIR}/sounds/music"
CRASH = f"{EFFECTS_PATH}/crash.ogg"
BACKGROUND_MUSIC = f"{MUSIC_PATH}/music.ogg"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = f"{ASSETS_DIR}/data/level-{{:03}}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6
CUSTOM = 7

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# CAR
CAR_GROUP = "cars"
CAR_IMAGE = f"{ASSETS_DIR}/images/car1.png"
CAR_WIDTH = 23
CAR_HEIGHT = 47
#CAR_RATE = 6 # used with animation
CAR_VELOCITY = 5


ROAD_GROUP = "road_walls"
ROAD_IMAGES = {
    "left":{
            "path" : f"{ASSETS_DIR}/images/left.png",
            "width" : 126,
            "height" : 599
        },
    "right": {
            "path" : f"{ASSETS_DIR}/images/right.png",
            "width": 303,
            "height" : 598
        }
    }

TRAFFIC_GROUP = "traffic"
TRAFFIC_VELOCITY = 2
TRAFFIC_LEVEL_THRESHOLD = 350
TRAFFIC_CARS = 15
TRAFFIC_POINTS = 10
CAR_IMAGES = [
    f"{ASSETS_DIR}/images/car2.png",
    f"{ASSETS_DIR}/images/car3.png",
    f"{ASSETS_DIR}/images/car4.png"
 ]


# BRICK_POINTS = 50 # replace with POINTS FOR ROAD

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"


