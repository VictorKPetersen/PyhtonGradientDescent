import pandas as pd
import numpy as np


class CsvHandler:

    def __init__(self, path, first_collum_name, second_collum_name):
        self.path = path
        self.first_collum_name = first_collum_name
        self.second_collum_name = second_collum_name

    def get_x_from_csv(self):
        data = pd.read_csv(self.path)
        data_list = np.array(data[self.first_collum_name].values.tolist())
        return data_list

    def get_y_from_csv(self):
        data = pd.read_csv(self.path)
        data_list = np.array(data[self.second_collum_name].values.tolist())
        return data_list






