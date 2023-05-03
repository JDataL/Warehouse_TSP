from support_functions import *

class node:
    def __init__(self, position, category, north, south, east, west):
        self.POSITION = position
        self.CATEGORY = category
        self.NORTH = north
        self.SOUTH = south
        self.EAST = east
        self.WEST = west

    @classmethod
    def create_node(cls, warehouse_floor_plan, row_number, col_number):
        position = (row_number,col_number)
        category = 'walk_way'
        north = node.compass_check(warehouse_floor_plan, row_number-1, col_number)
        south = node.compass_check(warehouse_floor_plan, row_number+1, col_number)
        east = node.compass_check(warehouse_floor_plan, row_number, col_number+1)
        west = node.compass_check(warehouse_floor_plan, row_number, col_number-1)
        
        if warehouse_floor_plan[row_number][col_number] != '0':
            category = 'isle'

        return cls(position, category, north, south, east, west)
    
    @staticmethod
    def compass_check(warehouse_floor_plan, row, col):
        try:
            node_position = warehouse_floor_plan[row][col]
            if node_position == '0':
                return 'walk_way'
            else:
                return 'isle'
            
        except IndexError:
            return False