import csv

import matplotlib.pyplot as plt
import numpy as np


def get_csv_data(filename):
    with open('data/' + filename + '.csv', 'rb') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        csv_data = [row for row in datareader]
    return csv_data[5:]


def plot_channel(data, label, channel=1, color_shape='bo'):
    for i in range(len(data)):
        plt.plot(data[i][0], data[i][channel], color_shape)
    return plt.plot(data[0][0], data[0][channel], color_shape, label=label)


def plot_dataset(data, title):
    plt.figure()
    thermistor, = plot_channel(data, 'Thermistor Voltage', 1, 'b.')
    response, = plot_channel(data, 'Output Voltage of Controller', 2, 'g.')
    plt.plot([-5, 5], [0, 0], 'r', label='Goal Voltage on Thermistor (0V)')
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.legend(loc=0)


def main():
    tests = {'med_proportional_small_integrator_touch':'Recovery after brief touch',
             'med_proportional_small_integrator_wind_single_puff':'Recovery after brief wind',
             'med_proportional_small_integrator_ice':'Ice briefly applied, temp. step',
             'med_proportional_small_integrator_heat_step':'Heat gun briefly applied, temp. step'}
             # 'med_proportional_small_integrator_stable':'Stable system, no disturbances', # SAVED

    for dataset in tests.keys():
        data = get_csv_data(dataset)
        plot_dataset(data, tests[dataset])
    plt.show()


if __name__ == '__main__':
    main()
