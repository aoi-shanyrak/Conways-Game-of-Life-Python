
DENSITY_MODES = {
    "very_sparse": 0.02,    # 2% - почти пустое поле
    "sparse": 0.05,         # 5% - для стабильных конфигураций
    "optimal": 0.1,         # 10% - оптимально для игры Жизнь
    "dense": 0.15,          # 15% - более активная игра
    "chaos": 0.25,          # 25% - хаотичное поведение
    "random": None,         # Случайная плотность от 2% до 25%
}

USE_NUMPY = True

DENSITY_MODE = "chaos"
DENSITY_VALUE = None
FIELD_SIZE = 64
STEPS = 64

ANIMATION = True
INTERVAL_FOR_ANI = 50
SAVE_GIF_ANI = False

VERBOSE = True

TEST_DIR = "fields"
FIELD_NUMBER = None
SAVE_GIF_ANI_PATH = "gifs"
