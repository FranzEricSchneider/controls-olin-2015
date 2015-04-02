import matplotlib.pyplot as plt

from plot_tools import *


def main():
    # Sample,Time (s),C1 (mV),C2 (V)
    filename = "part2_q2_"
    voltages = ['6V', '9V', '10V', '11V', '12V']
    colors = ['b', 'g', 'r', 'c', 'm']
    filetype = ".csv"

    # for i in range(len(colors)):
    i = 4
    time, pot_V, voltage = \
        get_double_column_data(filename + voltages[i] + filetype)
    pot_time, pot_V = rm_pot_V_edges(time, pot_V, 0.3)
    angle = get_position_from_potentiometer(pot_V)
    velocity = get_velocity_from_angle(pot_time, angle)
    filtered_velocity = moving_average(velocity, 30)

    ###########################################################################
    Vs = [9.2, 14.3, 16.0, 17.7, 19.5]
    V = Vs[i]
    plot_points_and_lines(pot_time, filtered_velocity)
    plt.plot([0, 10], [0.1*V, 0.1*V])
    plt.plot([0, 10], [0.9*V, 0.9*V])
    plt.plot([0, 10], [-0.1*V, -0.1*V])
    plt.plot([0, 10], [-0.9*V, -0.9*V])
    ###########################################################################

    #     plt.subplot(2, 1, 1)
    #     plt.plot(pot_time, filtered_velocity, color=colors[i], linewidth=1)
    #     plt.plot([pot_time[0], pot_time[1]],
    #              [filtered_velocity[0], filtered_velocity[1]],
    #              color=colors[i], label=voltages[i], linewidth=2)
    #     plt.xlabel('Time (s)')
    #     plt.ylabel('Change in Pot Voltage over Time (V/s)')
    #     plt.title('Velocity as Motor is Driven in Voltage Square Wave')

    #     plt.subplot(2, 1, 2)
    #     plt.plot(time, voltage, color=colors[i], linewidth=1)
    #     plt.plot([time[0], time[1]],
    #              [voltage[0], voltage[1]],
    #              color=colors[i], label=voltages[i], linewidth=2)
    #     plt.xlabel('Time (s)')
    #     plt.ylabel('Current (A)')
    #     plt.title('Current as Motor is Driven in Voltage Square Wave')
    # plt.subplot(2, 1, 1)
    # plt.legend()
    # plt.subplot(2, 1, 2)
    # plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
