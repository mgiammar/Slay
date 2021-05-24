# -*- coding: utf-8 -*-

from typing import List
from pygame import Color


__author__ = "Matthew Giammar"
__email__ = "giammar.7@osu.edu"


class Player:
    """Player class"""

    player_type : str
    color : Color
    territories = List[territory]

    def __init__(self, player_type="computer", color=(0,0,0)):
        self.player_type = player_type
        self.color = color

