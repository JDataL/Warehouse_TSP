from isle_class import *

class warehouse:
    def __init__(self, floorplan, isle_codes, isle_objects):
        self.FLOORPLAN = floorplan
        self.isle_codes = isle_codes
        self.isle_objects = isle_objects

    def create_warehouse(cls):

        csv_floorplan =  retrieve_floor_plan()
        isle_codes = []
        isle_objects = []

        new_matrix = []
        row_number = 0

        for each_row in csv_floorplan:
            new_matrix.append([])

            col_number = 0

            for each_col in each_row:
                new_matrix[row_number].append(node.create_node(csv_floorplan, row_number, col_number))

                if each_col != '0':

                    if each_col not in isle_codes:
                        isle_codes.append(each_col)
                        isle_objects.append(isle(each_col))

                    index = isle_codes.index(each_col)
                    isle_objects[index].NODE_POSITIONS.append((row_number,col_number))

                    col_number += 1
            
            row_number += 1

        return cls(new_matrix, isle_codes, isle_objects)

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

