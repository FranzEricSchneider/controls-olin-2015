import matplotlib.pyplot as plt

from plot_tools import *


def main():
    filename = "part1_q1_5-45V.csv"  # Sample,Time (s),C1 (V)
    time, pot_voltage = get_single_column_data(filename)
    plot_points_and_lines(time, pot_voltage)
    plt.xlabel('Time (s)')
    plt.ylabel('Measured Potentiometer Voltage (V)')
    plt.title('Potentiometer as Motor is Driven at 5.45V')
    print("Delta V is 5 volts".upper())
    plt.show()


if __name__ == '__main__':
    main()
