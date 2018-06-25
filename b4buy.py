import pygame
import logging
import sys

class App:
    def __init__(self):
        pygame.init()
        self.get_screen()
        self.run()

    def get_screen(self):
        logging.info('Getting display...')
        modes = pygame.display.list_modes()
        self.screen = pygame.display.set_mode(modes[0])

    def run(self):
        running = True

        while running:
            self.tick()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.cleanAndExit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.cleanAndExit()


    def tick(self):
        pass

    def cleanAndExit(self):
        logging.info('Closing\nBye!')
        pygame.quit()
        sys.exit()

if __name__=='__main__':
    logging.basicConfig(filename='b4buy.log', level=logging.INFO)
    app = App()
