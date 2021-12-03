import pandas as pd
import numpy as np


class CsvHandler:

    def __init__(self, path):
        self.path = path

    def get_x_from_csv(self):
        data = pd.read_csv(self.path)
        data_list = np.array(data['Price'].values.tolist())
        return data_list

    def get_y_from_csv(self):
        data = pd.read_csv(self.path)
        data_list = np.array(data['SqM'].values.tolist())
        return data_list






