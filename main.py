# Victor Kahl Petersen - SOP Machine Learning - 3.D Rybners Teknisk Gymnasium
from Descent import GradientDescent


def main():
    xValues = [0, 4, 7, 9, 15, 17, 21, 25, 31, 34, 36, 31]
    yValues = [4, 2, 8, 12, 13, 16, 21, 19, 25, 20, 30, 35]
    GD1 = GradientDescent(0.0015, 100000, xValues, yValues)
    GD1.gradient_descent_regression()


if __name__ == '__main__':
    main()
