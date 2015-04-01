import matplotlib.pyplot as plt

from plot_tools import *


def main():
    # Sample,Time (s),C1 (mV),C2 (V)
    filename = "part1_q2_"
    voltages = ['5V', '6V', '7V', '8V', '9V', '10V', '11V', '12V']
    filetype = ".csv"

    time, current_mV, pot_V = \
        get_double_column_data(filename + voltages[7] + filetype)
    # plot_points_and_lines(time, C1)
    angle = get_position_from_potentiometer(pot_V)
    plot_points_and_lines(time, angle, color='g')
    velocity = get_velocity_from_angle(time, angle)
    plot_points_and_lines(time, velocity, color='r')

    current_V = convert_mV_to_V(current_mV)
    current = calculate_current_from_voltage(current_V)
    # plt.xlabel('Time (s)')
    # plt.ylabel('Measured Potentiometer Voltage (V)')
    # plt.title('Potentiometer as Motor is Driven at 5.45V')
    # print("Delta V is 5 volts".upper())
    plt.show()


if __name__ == '__main__':
    main()
