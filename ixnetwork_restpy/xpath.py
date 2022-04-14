"""
This class is used by the config assistant, its sole purpose is to store the json and mode of operation
which helps in the operation of caching and mode recognition
"""


class Xpath(object):
    def __init__(self):
        self._config = []
        self._children = []
        self._mode = "normal"

    @property
    def config(self):
        return self._config
