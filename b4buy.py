import pygame
import logging
import sys
import yaml

from buildings import Building

class App:
    def __init__(self):
        logging.info('Initializing pygame')
        pygame.init()
        with open('settings.yaml') as f:
            self.settings = yaml.load(f)
        self.get_screen()
        self.clock = pygame.time.Clock()
        self.fps = self.settings['fps']

        self.buildings = [Building(self.settings, 'warehouse', (0,0))]

        self.run()

    def get_screen(self):
        logging.info('Getting display')
        modes = pygame.display.list_modes()
        self.screen = pygame.display.set_mode(modes[0])

    def run(self):
        running = True
        pygame.time.set_timer(pygame.USEREVENT, round(1000/self.fps))

        while running:
            self.clock.tick(60)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.cleanAndExit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.cleanAndExit()

                if e.type == pygame.USEREVENT:
                    print('Check')
                    for building in self.buildings:
                        building.produce()


    def cleanAndExit(self):
        logging.info('Closing\nBye!')
        pygame.quit()
        sys.exit()

if __name__=='__main__':
    logging.basicConfig(filename='b4buy.log', level=logging.INFO)
    app = App()
