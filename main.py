# Victor Kahl Petersen - SOP Machine Learning - 3.D Rybners Teknisk Gymnasium
from Descent import GradientDescent
from csvHandler import CsvHandler


def main():

    CSVHandler1 = CsvHandler('housePriceDataTest.csv')
    x_values = CSVHandler1.get_x_from_csv()
    y_values = CSVHandler1.get_y_from_csv()

    GD1 = GradientDescent(0.025, 10000000, x_values, y_values)
    GD1.gradient_descent_regression()




if __name__ == '__main__':
    main()
