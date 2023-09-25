class CommandLineEventLoop:
    def __init__(self, command_line_app):
        self.command_line_app = command_line_app

    def start(self, tick):
        while True:
            tick()
