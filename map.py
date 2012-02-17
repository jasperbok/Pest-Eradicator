import math
import os
import sys

from tile import Tile
import settings

class Map():
    def __init__(self, file_name, window_surface_reference):
        self.map_ = self._generate_map_from_file(file_name)
        self.window_surface_reference = window_surface_reference

    def draw_tiles(self):
        for line in self.map_:
            for tile in line:
                try:
                    self.window_surface_reference.blit(tile.image, tile.rect)
                except:
                    pass

    def get_tile_index_at_point(self, point):
        """Gets the x and y offsets to lookup the tile in the internal map_
        list.

        Keyword arguments:
        point -- A tuple containing an x-y co-ordinate (x, y).

        """
        x_offset = int(math.floor(point[0] / settings.TILE_SIZE))
        y_offset = int(math.floor(point[1] / settings.TILE_SIZE))
        return (x_offset, y_offset)

    def get_available_directions(self, point):
        """Finds out what adjecent tiles are passable.

        Keyword arguments:
        point -- A tuple containing an x-y co-ordinate (x, y).

        """
        print "GETTING DIRECTIONS"
        tile_x_offset, tile_y_offset = self.get_tile_index_at_point(point)
        choices = []
        if self.map_[tile_y_offset - 1][tile_x_offset].passable:
            choices.append('north')
        if self.map_[tile_y_offset][tile_x_offset + 1].passable:
            choices.append('east')
        if self.map_[tile_y_offset + 1][tile_x_offset].passable:
            choices.append('south')
        if self.map_[tile_y_offset][tile_x_offset - 1].passable:
            choices.append('west')
        return choices

    def get_tile_at_index(self, location):
        """Returns a reference to a tile at a certain location in the
        internal map_ list.

        Keyword arguments:
        location -- A tuple containing a 2 dimensional array index, eg: (2, 4)
        """
        try:
            return self.map_[location[1]][location[0]]
        except IndexError:
            print "Index error!"

    def get_tile_at_point(self, point):
        """Returns the tile that contains a given point.

        Keyword arguments:
        point -- A tuple containing an x-y co-ordinate (x, y).

        """
        x_offset = int(math.floor(point[0] / settings.TILE_SIZE))
        y_offset = int(math.floor(point[1] / settings.TILE_SIZE))
        return self.map_[y_offset][x_offset]

    def _generate_map_from_file(self, file_name):
        map_ = []
        with open(os.path.join('maps', file_name), 'r') as map_file:
            y_pos = 0
            for line in map_file:
                if not line.startswith('#'):
                    row = []
                    x_pos = 0
                    for char in line:
                        if char in "abcdefghijklmnopqrstuvwxyz-":
                            row.append(self._character_to_tile(char, (x_pos, y_pos)))
                            x_pos += settings.TILE_SIZE
                    y_pos += settings.TILE_SIZE
                    map_.append(row)
                else:
                    # The line is a creature entry in the following format:
                    # # x_pos, y_pos, facing_direction, gender
                    pass
        return map_

    def _character_to_tile(self, character, start_position):
        """Used during map loading to translate a character from the text
        file to a specific type of tile.

        Keyword arguments:
        character -- The ASCII character to translate to a tile.
        start_position -- A tuple with the tile's starting x and y positions

        """
        if character == '-':
            tile = Tile('grass.png', False)
        elif character == 'a':
            tile = Tile('dirt_road.png', True)
        tile.rect.topleft = start_position
        return tile
