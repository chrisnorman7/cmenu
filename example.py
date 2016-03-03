from __future__ import absolute_import, division, print_function
from builtins import *
from cmenu import Menu

m = Menu('Example Menu')
m.add_entry('Print 4', lambda value = 4: print(value))
m.add_entry('Quit', lambda: None)

print(m.get_selection())
