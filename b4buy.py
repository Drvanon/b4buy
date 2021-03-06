import pygame
import logging
import sys
import yaml

from buildings import Building
from console import Console

WHITE = (240, 240, 240)
BLACK = (10, 10, 10)

class App:
    def __init__(self):
        logging.info('Initializing pygame')
        pygame.init()
        with open('settings.yaml') as f:
            self.settings = yaml.load(f)
        self.get_screen()
        self.clock = pygame.time.Clock()
        self.fps = self.settings['fps']
        self.console = Console()


        self.fonts = {
            'console.font': pygame.font.Font(None, 28)
        }

        self.buildings = [Building(self.settings, 'warehouse', (0,0))]
        self.connections = []

        self.run()

    def get_screen(self):
        logging.info('Getting display')
        modes = pygame.display.list_modes()
        self.screen = pygame.display.set_mode(modes[0])

    def run(self):
        running = True
        pygame.time.set_timer(pygame.USEREVENT, round(1000/self.fps))

        while running:
            self.clock.tick(40)
            self.screen.fill((0,0,0))
            self.show_console()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.cleanAndExit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.console.switch_mode('normal')
                    if self.console.mode == 'normal':
                        if e.key == pygame.K_i:
                            self.console.switch_mode('insert')
                            continue
                    if self.console.mode == 'insert':
                        if e.key == pygame.K_RETURN:
                            self.run_command()
                            self.console.switch_mode('normal')
                        else:
                            self.console.text += chr(e.key)

                if e.type == pygame.USEREVENT:
                    for building in self.buildings:
                        building.produce()

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_BACKSPACE] and self.console.mode == 'insert':
                self.console.text = self.console.text[:-1]

            pygame.display.flip()

    def run_command(self):
        self.console.history.append(self.console.text)
        self.console.output.append(self.console.text)
        self.console.text = ''
        comlist = self.console.text.split()
        if comlist:
            if comlist[0] == 'build':
                if len(comlist) > 2:
                    building_type = comlist[1]

    def show_console(self):
        if self.console.mode == 'insert':
            self.screen.fill(WHITE, [0, 0, 300, 200])
            pygame.draw.line(self.screen, BLACK, (3, 30), (297, 30))
            text_surf = self.fonts['console.font'].render(
                    self.console.text[-24:], True, (0, 0, 0),
                    WHITE
                    )
            self.screen.blit(text_surf, (10, 10))

    def cleanAndExit(self):
        logging.info('Closing\nBye!')
        pygame.quit()
        sys.exit()

if __name__=='__main__':
    logging.basicConfig(filename='b4buy.log', level=logging.INFO)
    app = App()
