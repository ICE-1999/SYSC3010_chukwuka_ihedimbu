"""
my_pi_emulator_1.py

This module defines function that simulates the behaviour of
a temperature module and a display module

On availability of a display module and temperature module
the functions in these classes can be substituted for the
modules library functions 
"""

import random

#temperature module class 
class tempMod:
    def readC(self):
        return random.randint(10,22)

#display module class
class dispMod:
    def Print(self,s):    
        print(f'| {s}\r', end="")

    def init(self):
        print("\n\n|---------------|")

        
