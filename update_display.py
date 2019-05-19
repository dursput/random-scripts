#!/usr/bin/env python
from win32api import (
    EnumDisplaySettings,
    ChangeDisplaySettings,
    GetSystemMetrics
)
import sys

class DisplaySettings():
    def __init__(self):
        # Retrieve Display Device settings.
        self.settings = EnumDisplaySettings()
        # Manually set resolution since it's hard-coded to 640x480.
        self.settings.PelsWidth = GetSystemMetrics(0)
        self.settings.PelsHeight = GetSystemMetrics(1)

    def __update(self):
        ChangeDisplaySettings(self.settings, 0)
    
    def __set_refresh(self, freq: int):
        self.settings.DisplayFrequency = freq
        self.__update()

    def __get_resolution(self) -> tuple:
        # Return current resolution - horizontal by vertical (in pixels)
        return (self.settings.PelsWidth, self.settings.PelsHeight)

    def __get_refresh(self) -> int:
        # Return current refresh rate (in Hz)
        return self.settings.DisplayFrequency

    def toggle(self, mode: str):
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

    def print_settings(self):
        print('Resolution: %dx%d' % self.__get_resolution())
        print('Refresh rate: %dHz' % self.__get_refresh())

def run():
    if len(sys.argv) > 1:
        display = DisplaySettings()
        if display.toggle(str(sys.argv[1])):
            print('New settings:')
            display.print_settings()
    else:
        print('Error: Must provide a mode (normal | gaming)')

"""
# https://stackoverflow.com/questions/8705814/get-display-count-and-resolution-for-each-display-in-python-without-xrandr
from Xlib import X, display
from Xlib.ext import randr

d = display.Display()
s = d.screen()
window = s.root.create_window(0, 0, 1, 1, 1, s.root_depth)
res = randr.get_screen_resources(window)
for mode in res.modes:
    w, h = mode.width, mode.height
    print(w, h)

# https://stackoverflow.com/questions/21074788/how-do-i-get-a-list-of-all-valid-screen-resolutions-in-python
import ctypes

sdl_dll = ctypes.CDLL('sdl.dll')
modes = sdl_dll.SDL_ListModes(None, None)
print(modes)
"""