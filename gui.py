"""
  Text-based GUI lib
"""

import os
from typing import Optional, Union
from enum import Enum

class Direction(Enum):
  LEFTTORIGHT = 0
  TOPTOBOTTOM = 1

class BorderStyle(Enum):
   NONE = 0
   SPACE = 1
   PIPES = 2
   LINES = 3

class FormatText:
  def __init__(
    self,
    text:str,
    bold:bool=False,
    underline:bool=False,
    color:int=0,
    halign:int=0,
    valign:int=0
  ):
    self.text = text
    self.bold = bold
    self.underline = underline
    self.color = color
    self.halign = halign
    self.valign = valign

class Container:
    """ Containers have a list of children """
    def __init__(self, children:Optional[list]=None, direction:Direction=Direction.LEFTTORIGHT):
      """
        Creates a container

        Parameters:
        children = A list of objects with a draw method
      """
      self.children = children
      self.direction = direction
    
    def draw(self, setw:Optional[int]=None, seth:Optional[int]=None):
      """
        Draws children in this container
      """

class Panel(Container):
    """ Panels have title bars, borders, and content """
    def __init__(
      self,
      w:float=1,
      h:float=1,
      border:BorderStyle=BorderStyle.LINES,
      content:Optional[FormatText]=None
    ):
        """
          Creates a panel inside of the terminal

          Parameters:
          -----------
          w = Width, 1 being 100% of the parent, 0 being 0%
          h = Height, 1 being 100% of the parent, 0 being 0%
          border = The border style
          content = Text content, the position and alignment is controlled by textprops
        """
        self.w = w
        self.h = h
        self.content = content
        self.border = border