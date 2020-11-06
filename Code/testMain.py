"""Ce fichier sert à tester des fonctions individuelles du code 
    """
from threading import Timer


class CustomTimer(Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._original_function = function
        super(CustomTimer, self).__init__(
            interval, self._do_execute, args, kwargs)

    def _do_execute(self, *a, **kw):
        self.result = self._original_function(*a, **kw)

    def join(self):
        super(CustomTimer, self).join()
        return self.result


def add_together(a, b):
    return a + b


if __name__ == "__main__":
    while True : # Boucle infinie
        c = CustomTimer(10, add_together, (2, 4))
        c.start()
        print(c.join())
