import matplotlib.pyplot as plt

from plot_tools import *


def main():
    # Sample,Time (s),C1 (mV),C2 (V)
    filename = "part1_q3_"
    voltages = ['400mA', '450mA', '500mA', '550mA', '600mA']
    colors = ['b', 'g', 'r', 'c', 'm']
    filetype = ".csv"

    for i in range(len(colors)):
        time, current_mV, pot_V = \
            get_double_column_data(filename + voltages[i] + filetype)
        pot_time, pot_V = rm_pot_V_edges(time, pot_V)
        angle = get_position_from_potentiometer(pot_V)
        velocity = get_velocity_from_angle(pot_time, angle)
        filtered_velocity = moving_average(velocity, 15)

        current_V = convert_mV_to_V(current_mV)
        current = calculate_current_from_voltage(current_V)
        filtered_current = moving_average(current, 30)

        plt.subplot(2, 1, 1)
        plot_points_and_lines(pot_time, filtered_velocity,
                              color=colors[i], label=voltages[i])
        plt.xlabel('Time (s)')
        plt.ylabel('Change in Pot Voltage over Time (V/s)')
        plt.title('Velocity as Motor is Driven at DC Voltages')

        plt.subplot(2, 1, 2)
        plt.plot(time, filtered_current, color=colors[i], linewidth=0.25)
        plt.plot([time[0], time[1]],
                 [filtered_current[0], filtered_current[1]],
                 color=colors[i], label=voltages[i], linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Current (A)')
        plt.title('Current as Motor is Driven at DC Voltages')
        # print("Delta V is 5 volts".upper())
    plt.subplot(2, 1, 1)
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
