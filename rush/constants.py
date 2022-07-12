from game.casting.color import Color

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

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONTS_PATH = "rush/assets/fonts" 
FONT_FILE = FONTS_PATH + "/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "rush/assets/sounds/boing.wav"
WELCOME_SOUND = "rush/assets/sounds/start.wav"
OVER_SOUND = "rush/assets/sounds/over.wav"

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
LEVEL_FILE = "rush/assets/data/level-{:03}.txt"
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
CAR_IMAGE = "rush/assets/images/car1.png"
CAR_WIDTH = 23
CAR_HEIGHT = 47
#CAR_RATE = 6 # used with animation
CAR_VELOCITY = 5


ROAD_GROUP = "road_walls"
ROAD_IMAGE = {
    "left":"rush/assets/images/left.png",
    "right":"rush/assets/images/right.png"
    }

TRAFFIC_GROUP = "traffic"
TRAFFIC_VELOCITY = 2
TRAFFIC_CARS = 15
CAR_IMAGES = [
    "rush/assets/images/car2.png",
    "rush/assets/images/car3.png",
    "rush/assets/images/car4.png"
 ]


# BRICK_POINTS = 50 # replace with POINTS FOR ROAD

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"


