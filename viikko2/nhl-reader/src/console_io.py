class ConsoleIO:
    def read(self, text):
        return str(input(text))

    def write(self, message: str = ""):
        print(message)
