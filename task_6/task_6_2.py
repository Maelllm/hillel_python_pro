class bcolors:
    COLORS = {'black': '\033[90m', 'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m', 'blue': '\033[94m',
              'pink': '\033[95m', 'turquoise': '\033[96m', 'default': '\033[0m'}


class colorizer(bcolors):
    def __init__(self, text='defalut'):
        self.text = text

    def __enter__(self):
        try:
            print(colorizer.COLORS[self.text.lower()])
        finally:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(colorizer.COLORS['default'])


with colorizer('yellow'):
    print('printed in red')
print('printed in default color')
