import pygame
import os
pygame.mixer.init()
# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Dino/duck2.png"))

JUMP_SOUND =  pygame.mixer.Sound(os.path.join(IMG_DIR, 'Other/score_sound.wav'))
JUMP_SOUND.set_volume(1)

DEATH_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Other/death_sound.wav'))
DEATH_SOUND.set_volume(1)

SCORE_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Other/score_sound.wav'))
SCORE_SOUND.set_volume(1)

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/runShilder1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/runShilder2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/runShilder3.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run2.png")),
    
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/jumpshilder.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/jump.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/duckshilder.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/duckshilder.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/duck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/duck.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
FUNDO = pygame.image.load(os.path.join(IMG_DIR, 'Other/7.png'))
FUNDO = pygame.transform.scale(FUNDO,(SCREEN_WIDTH, SCREEN_HEIGHT -200))
FUNDO_INIT =  pygame.image.load(os.path.join(IMG_DIR, 'Other/7.png'))
FUNDO_INIT = pygame.transform.scale(FUNDO,(SCREEN_WIDTH, SCREEN_HEIGHT ))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
