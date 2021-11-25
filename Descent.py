import numpy as np


class GradientDescent:

    def __init__(self, learning_rate, iterations, x_data, y_data):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.x = np.array(x_data)
        self.y = np.array(y_data)

    def gradient_descent_regression(self):
        a_current = 0
        b_current = 0
        n = len(self.x)
        current_iteration = 0;
        previous_cost = 0;

        while current_iteration < self.iterations:
            current_iteration += 1

            y_prediction = a_current * self.x + b_current

            cost = (1 / n) * sum([val ** 2 for val in (self.y - y_prediction)])

            derivativeA = (2 / n) * sum(-self.x * (self.y - y_prediction))
            derivativeB = (2 / n) * sum(-(self.y - y_prediction))

            a_current = a_current - self.learning_rate * derivativeA
            b_current = b_current - self.learning_rate * derivativeB

            print(f"a: {a_current}, b: {b_current}, Cost: {cost}, Iteration: {current_iteration}")

            if abs(cost - previous_cost) >= 5e-33:
                previous_cost = cost
            else:
                break
