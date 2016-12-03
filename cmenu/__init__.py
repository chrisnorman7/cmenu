"""
Command line menus.

Put this file into your site-packages directory.

Then you can do:

from cmenu import Menu

m = Menu('header')

c.add_item('label', func)

When an entry is selected from the menu, the attached function will be called.
"""

from __future__ import absolute_import, division, print_function
from builtins import *

class Menu(object):
 def __init__(self, title, format = '[{pos}] {label}', prompt = 'Type a number: '):
  """
  Initialise the menu with a title.
  
  If format is included, it will be used for printing entries and will be formatted with the following formatters:
  pos - The position in the menu.
  label - The labe of the entry in the menu.
  func - The function which is assigned to this label.
  
  If prompt is included, it will be printed before entry is required.
  """
  self.title = title
  self.format = format
  self.prompt = prompt
  self.entries = []
 
 def add_entry(self, label, func):
  """Add an entry. Takes a label and a function to be called."""
  self.entries.append([label, func])
  return len(self.entries) - 1
 
 def get_selection(self):
  """Show the menu and get a response."""
  print(self.title)
  for x, y in enumerate(self.entries):
   label, func = y
   print(self.format.format(pos = x + 1, label = label, func = func))
  try:
   return self.entries[int(input(self.prompt)) - 1][1]
  except ValueError:
   pass
