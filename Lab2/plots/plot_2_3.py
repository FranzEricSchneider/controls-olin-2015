import matplotlib.pyplot as plt

from plot_tools import *


def main():
    # Time (s),C1 (V),C2 (V)
    filename = "part2_q3_"
    currents = ['250mA', '280mA', '300mA', '330mA']
    colors = ['b', 'g', 'r', 'c']
    filetype = ".csv"

    for i in range(len(colors)):
        time, current_mV, pot_V = \
            get_double_column_data(filename + currents[i] + filetype)
        pot_time, pot_V = rm_pot_V_edges(time, pot_V)
        angle = get_position_from_potentiometer(pot_V)
        velocity = get_velocity_from_angle(pot_time, angle)
        filtered_velocity = moving_average(velocity, 15)

        current_V = current_mV
        current = calculate_current_from_voltage(current_V)
        filtered_current = moving_average(current, 25)

        plt.subplot(2, 1, 1)
        plt.plot(pot_time, filtered_velocity, color=colors[i], linewidth=1)
        plt.plot([pot_time[0], pot_time[1]],
                 [filtered_velocity[0], filtered_velocity[1]],
                 color=colors[i], label=currents[i], linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Change in Pot Voltage over Time (V/s)')
        plt.title('Velocity as Motor is Driven at Steady Currents')

        plt.subplot(2, 1, 2)
        plt.plot(time, filtered_current, color=colors[i], linewidth=1)
        plt.plot([time[0], time[1]],
                 [filtered_current[0], filtered_current[1]],
                 color=colors[i], label=currents[i], linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Current (A)')
        plt.title('Current as Motor is Driven at Steady Currents')
        # print("Delta V is 5 volts".upper())
    plt.subplot(2, 1, 1)
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
