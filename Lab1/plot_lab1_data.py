import csv

import matplotlib.pyplot as plt
import numpy as np


def get_csv_data(filename):
    with open('data/' + filename + '.csv', 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        csv_data = [row for row in datareader]
    csv_data = [[float(pt) for pt in row] for row in csv_data[5:]]
    return csv_data


def plot_channel(data, t_offset, label, channel=1, color_shape='bo'):
    for i in range(len(data)):
        plt.plot(data[i][0] + t_offset, data[i][channel], color_shape)
    return plt.plot(data[0][0] + t_offset, data[0][channel], color_shape, label=label)


def plot_dataset(data, title):
    t_offset = -data[0][0]
    plt.figure()
    thermistor, = plot_channel(data, t_offset, 'Thermistor Voltage', 2, 'b.')
    response, = plot_channel(data, t_offset, 'Output Voltage of Controller', 1, 'g.')
    plt.axis([0, data[-1][0] + t_offset, -3.0, 1.5])
    plt.plot([-50, 150], [0, 0], 'r', label='Goal Voltage on Thermistor (0V)')
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.legend(loc=0)


def main():
    tests = { #'med_proportional_small_integrator_touch':'Recovery after brief touch',
    #          'med_proportional_small_integrator_touch_and_hold':'Reaction to pinching and holding system',
    #          'med_proportional_small_integrator_wind_single_puff':'Recovery after brief wind',
    #          'med_proportional_small_integrator_ice':'Ice briefly applied, temp. step'} #,
             'med_proportional_small_integrator_heat_step':'Heat gun briefly applied, temp. step'}
             # 'med_proportional_small_integrator_stable':'Stable system, no disturbances', # SAVED

    for dataset in tests.keys():
        data = get_csv_data(dataset)
        plot_dataset(data, tests[dataset])
    plt.show()


if __name__ == '__main__':
    main()
