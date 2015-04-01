import csv
import matplotlib.pyplot as plt
import numpy as np


def get_all_lines(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def plot_points_and_lines(time, data, color='b', label=None):
    plt.plot(time, data, color, linewidth=0.5)
    plt.plot(time, data, color+'.', markersize=5)
    if label is not None:
        plt.plot([time[0], time[1]], [data[0], data[1]],
                 color=color, label=label, linewidth=2)


def get_single_column_data(filename, folder='data/'):
    with open(folder+filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = [row for row in reader]
    time_offset = -float(data[0][1])
    time = [float(row[1]) + time_offset for row in data]
    measured_val = [float(row[2]) for row in data]
    last_valid_data = measured_val.index(0)
    return (time[:last_valid_data], measured_val[:last_valid_data])


def get_double_column_data(filename, folder='data/'):
    with open(folder+filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = [row for row in reader]

    if len(data[0]) == 4:
        time_offset = -float(data[1][1])
        time = [float(row[1]) + time_offset for row in data[1:]]
        C1 = [float(row[2]) for row in data[1:]]
        C2 = [float(row[3]) for row in data[1:]]
        last_valid_data = C1.index(0)
    elif len(data[0]) == 3:
        time_offset = -float(data[1][0])
        time = [float(row[0]) + time_offset for row in data[1:]]
        C1 = [float(row[1]) for row in data[1:]]
        C2 = [float(row[2]) for row in data[1:]]
        try:
            last_valid_data = C1.index(0)
        except:
            last_valid_data = len(C1)+1

    return (time[:last_valid_data], C1[:last_valid_data], C2[:last_valid_data])


def get_position_from_potentiometer(data):
    offset = 0;
    position = []
    for i in range(len(data) - 1):
        if i > 0:
            if abs(data[i] - data[i - 1]) > 0.25 and \
               abs(data[i + 1] - data[i]) > 0.25:
                data[i] = data[i - 1]
    for i in range(len(data) - 1):
        position.append(data[i] + offset)
        if (data[i + 1] - data[i]) < -3:
            offset += 5
        elif (data[i + 1] - data[i]) > 3:
            offset -= 5
    position.append(position[-1])  # Keeps length same as before
    return position


def get_velocity_from_angle(time, data):
    velocity = []
    for i in range(len(data) - 1):
        velocity.append( (data[i + 1] - data[i]) / (time[i + 1] - time[i]) )
    velocity.append(velocity[-1])  # Maintains vector length
    return velocity


def rm_pot_V_edges(time, data):
    min_v = 0.0
    max_v = 5.0
    offset = 0.20
    pot_time = [point for point in time]
    for i in reversed(range(len(data))):
        if data[i] > max_v - offset or data[i] < min_v + offset:
            pot_time.pop(i)
            data.pop(i)
    return pot_time, data


def convert_mV_to_V(data):
    return [point / 1000.0 for point in data]


def calculate_current_from_voltage(data):
    R = 0.845
    scalar = 1.568  # Scales current data to match the power supply
    return [(point / R) * scalar for point in data]


def moving_average(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')
