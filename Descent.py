from plotter import Plotter

#Class that does all gradient descent along with calculation r2
class GradientDescent:

    def __init__(self, learning_rate, iterations, x_data, y_data):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.x = x_data
        self.y = y_data

#method to calculate r squared of a given line.
    def r_squared(self, y_prediction):
        y_average = sum(self.y) / len(self.y) # findes the average y value in data set
        unexplained_varians = sum([val ** 2 for val in (y_prediction - self.y)]); #runs once for each value in self.y. self.y is subtracted from y_prediction. Here after they are squared
        total_varians = sum([val ** 2 for val in (self.y - y_average)]) # Simmilar to above, only the diffrence has changed to each y value minus the average y value
        r2 = 1 - (unexplained_varians / total_varians) # Formula fo calculation r2
        return r2
#Method for executing gradient descent
    def gradient_descent_regression(self):
        a_current = 0 # set a, b to 0
        b_current = 0
        n = len(self.x) # get length of x array
        current_iteration = 0; # current iteration and previus cost is 0 as we are yet to perform an iteration
        previous_cost = 0;

        while current_iteration < self.iterations: # while loop that runs aslong as the current iteration does not go above the max amount specified.
            current_iteration += 1 # increments the iteration by 1

            y_prediction = a_current * self.x + b_current # regular formula for linear model y = a * x + b, generatas an array of y values based on current line

            cost = (1 / n) * sum([val ** 2 for val in (self.y - y_prediction)]) # Cost function for comparing how well it is progressing

            derivativeA = (2 / n) * sum(-self.x * (self.y - y_prediction)) # Partial derivitate a
            derivativeB = (2 / n) * sum(-(self.y - y_prediction)) # partial derivitate b

            a_current = a_current - self.learning_rate * derivativeA # updates the a value to a new one
            b_current = b_current - self.learning_rate * derivativeB # updates the v value
            r2 = self.r_squared(y_prediction) # r_squared method call to calculate r2
            print(f"a: {a_current}, b: {b_current}, Cost: {cost}, R2: {r2}, Iteration: {current_iteration}") #formatted string printing information

            if abs(cost - previous_cost) >= 5e-33: # checks if the positive diffrence of current cost - previus iterations cost is greated than 5e-33
                previous_cost = cost # updates previous cost
            else:
                break
        #Upon breaking the while loop final info is printen to console, and plots are made.
        print(f"The best fitting line i determined as \ny = {a_current}x + {b_current} \n with an R squarred value of {r2}")
        PlotterD = Plotter(self.x, self.y)
        PlotterD.plotScatterPoints()
        PlotterD.plotBestFitLine(a_current, b_current)
        PlotterD.showPlot()






