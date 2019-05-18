#!/usr/bin/env python
from win32api import (
    EnumDisplaySettings,
    ChangeDisplaySettings,
    GetSystemMetrics
)
import sys

class DisplaySettings():
    def __init__(self):
        self.settings = EnumDisplaySettings()
        self.settings.PelsWidth = GetSystemMetrics(0)
        self.settings.PelsHeight = GetSystemMetrics(1)

    def __update(self):
        ChangeDisplaySettings(self.settings, 0)
    
    def __set_refresh(self, freq):
        self.settings.DisplayFrequency = freq
        self.__update()

    def toggle(self, mode):
        if mode == 'normal':
            self.__set_refresh(144)
        elif mode == 'gaming':
            self.__set_refresh(60)
        else:
            print('Mode not recognized: \'%s\'' % mode)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        DisplaySettings().toggle(str(sys.argv[1]))
    else:
        print('Error: Must provide a mode.')
