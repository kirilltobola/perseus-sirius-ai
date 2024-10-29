from __future__ import print_function
import os, sys
import logging
from .. import views

class DoSomething(SomeCommand) :

    def __init__(self):
        for i in range(1,11):
            if self.number == i:
                print("matched")
            else:
                print('not matched')

    def check_user(self):
        if self.user: return True
        else  : return False