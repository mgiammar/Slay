# -*- coding: utf-8 -*-

from pygame import Color
from typing import List


__author__ = "Matthew Giammar"
__email__ = "giammar.7@osu.edu"


class Tile:

    r : int = 0 # row
    c : int = 0 # column
    color : str = ""  # Color and Player owner of this tile TODO make pygame.Color object
    # sprite : Sprite  # Sprite living on this tile (capitol, spearman, tree, etc.)

    def __init__(self, *args, **kwargs):
        """Initilize in axial coordinates"""
        if "r" in kwargs and "c" in kwargs and "color" in kwargs:
            self.r = kwargs["r"]
            self.c = kwargs["c"]
            self.color = kwargs["color"]


    def __str__(self):
        """Returns verbose string representing object"""
        pass

    def compact_tup(self):
        """Compact tuple representation for ASCII print"""
        hex_num = f"{self.to_int(as_hex=True)}".center(4, " ")
        coords = f"{self.r}, {self.c}".center(6, " ")
        color = self.color.center(6, " ")
        return (hex_num, coords, color)

    def parse_int(self, int):
        """Expands int from compacted storage to Tile object"""
        pass

    def to_int(self, as_hex=False):
        """Stores all info about tile to an integer

        Args:
            as_hex: if true, return int as 4 digit hex 
        """
        if as_hex:
            return "    "


class Board:
    # See (https://www.redblobgames.com/grids/hexagons/) for more info on data storage
    board : List[List[Tile]]  # odd-q storage

    def __init__(self, *args, **kwargs):
        """"""  # TODO: Write docstring
        # Should parse json file to complete board object
        # file will use even-q storage schema
        pass

    # Algoritms should convert even-q storage into axial/cube
    # If too computationally intensive, can convert storage types into axial 

    def ascii_print(self):
        """Prints ascii board state to terminal"""
        # Main loop for printing
        # NOTE: Only even number of columns will work currently
        # TODO: Add logic for odd number of columns

        num_rows = 5
        num_cols = 10  # use only even cols for now

        temp_board = [[Tile(r=j, c=i, color="color") for i in range(num_cols)] for j in range(num_rows)]

        top_row = print("        ____" * (num_cols // 2))  # Print tops of hexagons

        tile1 = temp_board[0][0].compact_tup()
        tile2 = temp_board[0][1].compact_tup()

        # Print first row
        temp1 = f"       /{tile2[0]}"
        temp2 = f"  ____/{tile2[1]}"
        temp3 = f" /{tile1[0]}\{tile2[2]}"
        temp4 = f"/{tile1[1]}\____"
        for j in range(3, num_cols, 2):
            tile1 = temp_board[0][j-1].compact_tup()
            tile2 = temp_board[0][j].compact_tup()
            temp1 += f"\      /{tile2[0]}"
            temp2 += f"\____/{tile2[1]}"
            temp3 += f"/{tile1[0]}\{tile2[2]}"
            temp4 += f"/{tile1[1]}\____"
        print(temp1 + "\\")
        print(temp2 + "\\")
        print(temp3 + "/")
        print(temp4 + "/")

        # Print main section
        for i in range(1, num_rows):
            tile0 = temp_board[i-1][0].compact_tup()
            tile1 = temp_board[i][0].compact_tup()
            tile2 = temp_board[i][1].compact_tup()
            temp1 = f"\{tile0[2]}/{tile2[0]}"
            temp2 = f" \____/{tile2[1]}"
            temp3 = f" /{tile1[0]}\{tile2[2]}"
            temp4 = f"/{tile1[1]}\____"
            for j in range(3, num_cols, 2):
                tile0 = temp_board[i-1][j-1].compact_tup()
                tile1 = temp_board[i][j-1].compact_tup()
                tile2 = temp_board[i][j].compact_tup()
                temp1 += f"\{tile0[2]}/{tile2[0]}"
                temp2 += f"\____/{tile2[1]}"
                temp3 += f"/{tile1[0]}\{tile2[2]}"
                temp4 += f"/{tile1[1]}\____"
            print(temp1 + "\\")
            print(temp2 + "\\")
            print(temp3 + "/")
            print(temp4 + "/")

        # Print bottom half of last row
        tile1 = temp_board[num_rows-1][0].compact_tup()
        temp1 = f"\{tile1[2]}/    "
        for j in range(2, num_cols, 2):
            tile1 = temp_board[num_rows-1][0].compact_tup()
            temp1 += f"\{tile1[2]}/    "
        print(temp1)
        print(" \\____/     " * (num_cols // 2))  # Print bottoms of hexagons



