from isle_class import *

class warehouse:
    def __init__(self):
        self.FLOORPLAN = retrieve_floor_plan()
        self.isle_codes = []
        self.isle_objects = []

    def x(self):
        new_matrix = []
        row_number = 0

        for each_row in self.FLOORPLAN:
            new_matrix.append([])

            col_number = 0

            for each_col in each_row:
                new_matrix[row_number].append(node.create_node(self.FLOORPLAN, row_number, col_number))

                if each_col != '0':

                    if each_col not in self.isle_codes:
                        self.isle_codes.append(each_col)
                        self.isle_objects.append(isle(each_col))

                    index = self.isle_codes.index(each_col)
                    self.isle_objects[index].NODE_POSITIONS.append((row_number,col_number))

                    col_number += 1
            
            row_number += 1

        self.FLOORPLAN = new_matrix

    def display_isle_values(self):
        
        for i in self.isle_objects:
            print(f'Isle: {i.CODE}')
            print('')
            for j in i.NODE_POSITIONS:
                self.display_node_values(j)
            print('')

    def display_node_values(self, position):
        print(f'Position: {self.FLOORPLAN[position[0]][position[1]].POSITION}')
        print(f'Category: {self.FLOORPLAN[position[0]][position[1]].CATEGORY}')
        print(f'North: {self.FLOORPLAN[position[0]][position[1]].NORTH}')
        print(f'South: {self.FLOORPLAN[position[0]][position[1]].SOUTH}')
        print(f'East: {self.FLOORPLAN[position[0]][position[1]].EAST}')
        print(f'West: {self.FLOORPLAN[position[0]][position[1]].WEST}')
        print('')

