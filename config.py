import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4.1-mini"
)

OPENAI_IMAGE_MODEL = os.getenv(
    "OPENAI_IMAGE_MODEL",
    "gpt-image-1"
)

WIDTH = 1080
HEIGHT = 1920
FPS = 24

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

ASSETS_DIR = os.path.join(
    BASE_DIR,
    "assets"
)

IMAGES_DIR = os.path.join(
    ASSETS_DIR,
    "images"
)

AUDIO_DIR = os.path.join(
    ASSETS_DIR,
    "audio"
)

OUTPUT_DIR = os.path.join(
    ASSETS_DIR,
    "output"
)

INPUT_DIR = os.path.join(
    BASE_DIR,
    "input"
)

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
