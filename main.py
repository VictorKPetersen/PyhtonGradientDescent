# Victor Kahl Petersen - SOP Machine Learning - 3.D Rybners Teknisk Gymnasium
from Descent import GradientDescent


def main():
    xValues = [0, 1, 2]
    yValues = [1, 2, 3]

    GD1 = GradientDescent(0.0015, 100000, xValues, yValues)
    GD1.gradient_descent_regression()



if __name__ == '__main__':
    main()
