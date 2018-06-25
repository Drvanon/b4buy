import pygame
import logging
import sys
import yaml

from buildings import Building

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

        self.fonts = {
            'console_font': pygame.font.Font(None, 28)
        }

        self.buildings = [Building(self.settings, 'warehouse', (0,0))]
        self.connections = []

        self.set_up_commands()

        self.run()

    def get_screen(self):
        logging.info('Getting display')
        modes = pygame.display.list_modes()
        self.screen = pygame.display.set_mode(modes[0])

    def run(self):
        running = True
        pygame.time.set_timer(pygame.USEREVENT, round(1000/self.fps))
        self.console_mode = 'normal'
        self.console_text = ''
        self.console_history = []

        while running:
            self.clock.tick(40)
            self.screen.fill((0,0,0))
            self.show_console()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.cleanAndExit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.console_mode = 'normal'

                    if self.console_mode == 'normal':
                        if e.key == pygame.K_i:
                            self.console_mode = 'insert'
                            continue
                    if self.console_mode == 'insert':
                        if e.key == pygame.K_RETURN:
                            self.run_command()
                            self.console_text = ''
                            command_mode = 'normal'
                        else:
                            self.console_text += chr(e.key)

                if e.type == pygame.USEREVENT:
                    for building in self.buildings:
                        building.produce()

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_BACKSPACE] and self.console_mode == 'insert':
                self.console_text = self.console_text[:-1]
            if self.console_mode == 'view' and not pressed_keys[pygame.K_v]:
                self.console_mode = 'normal'
            if pygame.key.get_pressed()[pygame.K_v] and self.console_mode == 'normal':
                self.console_mode = 'view'

            pygame.display.flip()

    def run_command(self):
        comlist = self.console_text.split()
        if comlist:
            if comlist[0] == 'build':
                if len(comlist) > 2:
                    building_type = comlist[1]

    def show_console(self):
        if self.console_mode in  ['insert', 'view']:
            self.screen.fill(WHITE, [0, 0, 300, 200])
            pygame.draw.line(self.screen, BLACK, (3, 30), (297, 30))
            text_surf = self.fonts['console_font'].render(
                    self.console_text[-24:], True, (0, 0, 0),
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
