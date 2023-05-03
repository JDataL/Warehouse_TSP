import numpy as np

def retrieve_floor_plan():
        CSVData = open('Warehouse_Layout.csv')
        warehouse_floor_plan = np.loadtxt(CSVData, delimiter=',', dtype=str)
        return warehouse_floor_plan