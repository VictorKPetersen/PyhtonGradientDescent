import matplotlib.pyplot as plt
#Import matplotlib.pyplot under the name plt


#Class plotter is responislbe for creating the diagrams that show up upen the end of the program
class Plotter:
    def __init__(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data
#plotScatterPoints(self): this method creates a subplot at a position, the proceeds to name the x and y axis and giving the plot a titel. Finally the data i plotted
    def plotScatterPoints(self):
        plt.subplot(1, 2, 1)
        plt.xlabel("Price pr. 100000 in Dkk")
        plt.ylabel("Area in square meters")
        plt.title("Scatter")
        plt.scatter(self.x_data, self.y_data)
#plotBestFitLine(self): THis does practicly the same as the above, just in a diffrent location. And it adds and a trendline using the final estiamte of Descent.py
    def plotBestFitLine(self, a, b):
        y = a * self.x_data + b
        plt.subplot(1, 2, 2)
        plt.xlabel("Price pr. 100000 in Dkk")
        plt.ylabel("Area in square meters")
        plt.title("Trend Line")
        plt.plot(self.x_data, y, linestyle = 'dotted', color = 'g')
        plt.scatter(self.x_data, self.y_data)


#Method to draw functions to screen
    def showPlot(self):
        plt.show()


