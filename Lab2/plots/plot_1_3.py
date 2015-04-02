import matplotlib.pyplot as plt

from plot_tools import *


def main():
    # Sample,Time (s),C1 (mV),C2 (V)
    filename = "part1_q3_"
    voltages = ['400mA', '450mA', '500mA', '550mA', '600mA']
    colors = ['b', 'g', 'r', 'c', 'm']
    filetype = ".csv"

    # for i in range(len(colors)):
    for i in [0, 4]:
        time, current_mV, pot_V = \
            get_double_column_data(filename + voltages[i] + filetype)
        pot_time, pot_V = rm_pot_V_edges(time, pot_V)
        angle = get_position_from_potentiometer(pot_V)
        velocity = get_velocity_from_angle(pot_time, angle)
        filtered_velocity = moving_average(velocity, 15)

        if i in [0, 2]:
            current_V = convert_mV_to_V(current_mV)
        else:
            current_V = current_mV
        current = calculate_current_from_voltage(current_V)
        filtered_current = moving_average(current, 30)

        if i == 0:
            plt.subplot(2, 2, 1)
            plt.title('Velocity as Motor is Driven at 400 mA')
        else:
            plt.subplot(2, 2, 3)
            plt.title('Velocity as Motor is Driven at 600 mA')
        plt.plot(pot_time, filtered_velocity, color=colors[i], linewidth=1)
        plt.plot([pot_time[0], pot_time[1]],
                 [filtered_velocity[0], filtered_velocity[1]],
                 color=colors[i], label=voltages[i], linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Change in Pot V over Time (V/s)')

        if i == 0:
            plt.subplot(2, 2, 2)
            plt.title('Current as Motor is Driven at 400 mA')
        else:
            plt.subplot(2, 2, 4)
            plt.title('Current as Motor is Driven at 600 mA')
        plt.plot(time, filtered_current, color=colors[i], linewidth=1)
        plt.plot([time[0], time[1]],
                 [filtered_current[0], filtered_current[1]],
                 color=colors[i], label=voltages[i], linewidth=2)
        plt.xlabel('Time (s)')
        plt.ylabel('Current (A)')
    plt.show()


if __name__ == '__main__':
    main()
