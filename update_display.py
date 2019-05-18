#!/usr/bin/env python
from win32api import (
    EnumDisplaySettings,
    ChangeDisplaySettings,
    GetSystemMetrics
)
import sys

class DisplaySettings():
    def __init__(self) -> None:
        # Retrieve Display Device settings.
        self.settings = EnumDisplaySettings()
        # Manually set resolution since it's hard-coded to 640x480.
        self.settings.PelsWidth = GetSystemMetrics(0)
        self.settings.PelsHeight = GetSystemMetrics(1)

    def __update(self) -> None:
        ChangeDisplaySettings(self.settings, 0)
    
    def __set_refresh(self, freq: int) -> None:
        self.settings.DisplayFrequency = freq
        self.__update()

    def __get_resolution(self) -> tuple:
        # Return current resolution - horizontal by vertical (in pixels)
        return (self.settings.PelsWidth, self.settings.PelsHeight)

    def __get_refresh(self) -> int:
        # Return current refresh rate (in Hz)
        return (self.settings.DisplayFrequency)

    def toggle(self, mode: str) -> None:
        # Switch between 'normal' (144Hz) and 'gaming' (60Hz)
        _success = True
        if mode == 'normal':
            self.__set_refresh(144)
        elif mode == 'gaming':
            self.__set_refresh(60)
        else:
            print('Mode not recognized: \'%s\'' % mode)
            _success = False
        return _success

    def print_settings(self) -> None:
        print('Resolution: %dx%d' % self.__get_resolution())
        print('Refresh rate: %dHz' % self.__get_refresh())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        display = DisplaySettings()
        if display.toggle(str(sys.argv[1])):
            print('New settings:')
            display.print_settings()
    else:
        print('Error: Must provide a mode (normal or gaming)')
