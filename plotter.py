import matplotlib.pyplot as plt
import numpy as np



class Plotter:
    def __init__(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data

    def plotScatterPoints(self):
        plt.subplot(1, 2, 1)
        plt.xlabel("Price pr. 100000 in Dkk")
        plt.ylabel("Area in square meters")
        plt.title("Scatter")
        plt.scatter(self.x_data, self.y_data)

    def plotBestFitLine(self, a, b):
        y = a * self.x_data + b
        plt.subplot(1, 2, 2)
        plt.xlabel("Price pr. 100000 in Dkk")
        plt.ylabel("Area in square meters")
        plt.title("Trend Line")
        plt.plot(self.x_data, y, linestyle = 'dotted', color = 'g')
        plt.scatter(self.x_data, self.y_data)



    def showPlot(self):
        plt.show()


