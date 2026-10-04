import pygame
from .constants import TIME_SCALE, SCREEN_SIZE, FPS

class Simulation:
    def __init__(self, space, is_scale_down=False):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.fps = FPS
        self.space = space
        self.is_scale_down = is_scale_down
        self.dt = (1/self.fps) * TIME_SCALE if self.is_scale_down else (1/self.fps)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                self.running = False

            self.screen.fill('black')

            self.space.render(self.screen, self.is_scale_down)
            self.space.update(self.dt)

            pygame.display.flip()
            self.clock.tick(self.fps)
