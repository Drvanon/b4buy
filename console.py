import logging

class Console:
    def __init__(self):
        self.modes = ['normal', 'insert']
        self.mode = 'normal'
        self.text = ''
        self.history = []
        self.output = []

    def switch_mode(self, mode):
        assert mode in self.modes

        self.mode = mode
        logging.info('Switched modes to: {}'.format(mode))
