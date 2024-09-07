# https://stackoverflow.com/questions/72361026/how-can-i-get-attrdict-module-working-in-python
from collections import UserDict

class AttrDict(UserDict):
    def __getattr__(self, key):
        return self.__getitem__(key)
    def __setattr__(self, key, value):
        if key == "data":
            return super().__setattr__(key, value)
        return self.__setitem__(key, value)
