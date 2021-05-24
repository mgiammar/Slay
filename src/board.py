# -*- coding: utf-8 -*-

from pygame import Color
from typing import List


__author__ = "Matthew Giammar"
__email__ = "giammar.7@osu.edu"


class Board:
    # See (https://www.redblobgames.com/grids/hexagons/) for more info on data storage
    board : List[List[Tile]]  # Axial hex grid

    def __init__(self, *args, **kwargs):
        """"""  # TODO: Write docstring
        # Should parse json file to complete board object
        pass

    def ascii_print(self):
        """Prints ascii board state to terminal"""
        # NOTE: Currently under development

        # Main loop for printing
        for row in self.board:
            for tile in row:
                print(str(tile))


class Tile:

    q : int  # q position (-up   +down)
    r : int  # r position (-left&up   +right&down)
    color : Color  # Color and Player owner of this tile
    # sprite : Sprite  # Sprite living on this tile (capitol, spearman, tree, etc.)

    def __init__(self, *args, **kwargs):
        """Initilize in axial coordinates"""

    def __str__(self):
        """Returns str representing object"""

    def parse_int(self, int):
        """Expands int from compacted storage to Tile object"""
        pass

    def to_int(self):
        """Stores all info about tile to an integer """
        pass

