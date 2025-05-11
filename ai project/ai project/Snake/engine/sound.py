import pygame

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.music = "assets/sounds/back_ground.mp3"
        self.chew = pygame.mixer.Sound("assets/sounds/chew.wav")
        self.death = pygame.mixer.Sound("assets/sounds/death.wav")
        self.death.set_volume(0.8)
        self.chew.set_volume(0.5)

    def play_background(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)  # loop

    def stop_background(self):
        pygame.mixer.music.stop()

    def play_chew(self):
        self.chew.stop()
        self.chew.play()

    def play_death(self):
        self.death.stop()
        self.death.play()
