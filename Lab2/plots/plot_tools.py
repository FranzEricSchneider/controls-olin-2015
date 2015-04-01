import csv
import matplotlib.pyplot as plt


def get_all_lines(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def plot_points_and_lines(time, data, color='b'):
    plt.plot(time, data, color, linewidth=0.5)
    plt.plot(time, data, color+'.', markersize=5)


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
    time_offset = -float(data[1][1])
    time = [float(row[1]) + time_offset for row in data[1:]]
    C1 = [float(row[2]) for row in data[1:]]
    C2 = [float(row[3]) for row in data[1:]]
    last_valid_data = C1.index(0)
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
        new_data = (data[i + 1] - data[i]) / (time[i + 1] - time[i])
        if i > 0:
            if abs(new_data - velocity[-1]) > 20:
                new_data = velocity[-1]
        velocity.append(new_data)
    velocity.append(velocity[-1])  # Maintains vector length
    return velocity


def convert_mV_to_V(data):
    return [point / 1000.0 for point in data]


def calculate_current_from_voltage(data):
    R = 0.845
    scalar = 1.568  # Scales current data to match the power supply
    return [(point / R) * scalar for point in data]
