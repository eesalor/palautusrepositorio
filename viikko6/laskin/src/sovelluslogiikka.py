class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._previous_values = []
    
    def _save_to_previous(self):
        self._previous_values.append(self._arvo)

    def miinus(self, operandi):
        self._save_to_previous()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._save_to_previous()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._save_to_previous()
        self._arvo = 0
    
    def kumoa(self):
        if not self._previous_values:
            return
        self._arvo = self._previous_values.pop()

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
