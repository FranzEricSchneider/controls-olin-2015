import matplotlib.pyplot as plt
from numpy import pi
import numpy as np


# Calculating ACTUAL \dot{\theta} (from plot_1_2)
voltages    = [5,       6,      7,      8,      9,      10]#11,     12]
revs        = [7,       7,      9,      14,     15,     16]
start_time  = [0.4312,  0.4862, 0.375,  0.2837, 0.1775, 0.2188]
end_time    = [4.7959,  4.4475, 4.6812, 6.0875, 5.6525, 5.4237]
dot_theta = []
for i in range(len(voltages)):
    dot_theta.append( revs[i] * 2 * pi / (end_time[i] - start_time[i]) )
print('-------------------------------')
print('\dot{\\theta} rad/s')
print(dot_theta)
print('-------------------------------')


# Calculating MEASURED \dot{\theta}_m in Volts / Second
# dot_theta_m = [-7.628034, -9.308132, -11.006211, -12.703801, -14.413247, -16.176099]#, -17.834590]
dot_theta_m = [7.628034, 9.308132, 11.006211, 12.703801, 14.413247, 16.176099]#, 17.834590]  # Converted to positive
print('-------------------------------')
print('\dot{\\theta}_m (V/s)')
print(dot_theta_m)
print('-------------------------------')


# Calculating K_{tach} in Volts / Radian
Dot_Theta = np.transpose( np.array([dot_theta]) )
Dot_Theta_M = np.transpose( np.array([dot_theta_m]) )
K_tach = np.dot( np.transpose(Dot_Theta), Dot_Theta_M )[0][0] / \
         np.dot( np.transpose(Dot_Theta), Dot_Theta )[0][0]
print('-------------------------------')
print('*** K_{tach} (V/rad) ***')
print(K_tach)
print('-------------------------------')


# Calculating V_m and I_m (from plot_2_1)
voltages        = [6,       9,      10,     11,     12]
#   Current spikes
delta_i_array   = [[3.45,   3.4,    3.305,  3.32,   3.29],
                   [5.13,   4.93,   4.93,   4.9,    5.03],
                   [5.165,  4.955,  5.028,  4.985,  5.168],
                   [5.11,   5.018,  5.1,    5.034,  5.13],
                   [5.12,   5.016,   5.14,   5.03,   5.13]]
currents = [np.mean(row) for row in delta_i_array]
print('-------------------------------')
print('Current spikes (A)')
print(currents)
print('-------------------------------')


# Calculating R_m (from plot_2_1)
Voltages = np.transpose( np.array([voltages]) )
Currents = np.transpose( np.array([currents]) )
R_m = np.dot( np.transpose(Currents), Voltages )[0][0] / \
      np.dot( np.transpose(Currents), Currents )[0][0]
print('-------------------------------')
print('*** R_m (\Omega) ***')
print(R_m)
print('-------------------------------')


# Calculating \tau_e (from plot_2_1)
ten_per_array = [[1.187,    2.5542,     4.0237,     5.4462],
                 [1.2278,   2.4402,     3.5441,     4.6897],
                 [1.1674,   2.2758,     3.3607,     4.5389],
                 [1.8237,   3.0238,     4.1064,     5.2802],
                 [1.216,    2.3565,     3.4276,     4.4817]]
ninety_per_array = [[1.1933,   2.5599,      4.0298,     5.452],
                    [1.2338,   2.4465,      3.5506,     4.7017],
                    [1.1736,   2.2819,      3.3668,     4.5455],
                    [1.8299,   3.03,        4.1125,     5.2865],
                    [1.2219,    2.3629,     3.4337,     4.4883]]
dt_array = []
for i in range(len(ten_per_array)):
    for j in range(len(ten_per_array[i])):
        dt_array.append(ninety_per_array[i][j] - ten_per_array[i][j])
dt_avg = np.mean(dt_array)
tau_e = dt_avg / 2.2
print('-------------------------------')
print('\\tau_e (s)')
print(tau_e)
print('-------------------------------')


# Calculating L_m
L_m = tau_e * R_m
print('-------------------------------')
print('*** L_m (H) ***')
print(L_m)
print('-------------------------------')


# Calculating v_emf (from plot_1_2)
voltages        = [5,           6,          7,          8,          9,          10]#11,     12]
steady_currents = [0.229466,    0.237100,   0.245455,   0.253681,   0.254916,   0.263335]
v_emf = [V - I * R_m for V, I in zip(voltages, steady_currents)]
print('-------------------------------')
print('V_{emf} (V)')
print(v_emf)
print('-------------------------------')


# Calculating K_e
V_Emf = np.transpose( np.array([v_emf]) )
K_e = np.dot( np.transpose(Dot_Theta), V_Emf )[0][0] / \
      np.dot( np.transpose(Dot_Theta), Dot_Theta )[0][0]
print('-------------------------------')
print('*** K_e (V-s/rad) ***')
print(K_e)
print('-------------------------------')


# Calculating n (or not)
print('-------------------------------')
print('*** Gear ratio n (unitless) ***')
print('Meaningless. 100+, because friction?')
print('-------------------------------')


# Calculating K_p
print('-------------------------------')
print('*** K_p - Scale factor for potentiometer - (V/rad) ***')
print(5.0 / (2 * pi))
print('-------------------------------')


# Calculateing J_F
print('-------------------------------')
print('*** J_F (Kg-m^2) ***')
J_F = 0.0010065  # kg-m^2
print(J_F)
print('-------------------------------')


# Calculating K_t and J_m from plot_2_3 and plot_1_3
currents_1_3 = [400,    450,    500,    550,    600]  # in mA
alpha_m_1_3  = [23.0,   28.75,  30.25,  42.0,   51.0]  # V/s, not velocity
alpha_1_3 = [point / K_tach for point in alpha_m_1_3]

Currents_1_3 = np.transpose( np.array([currents_1_3]) )
Alpha_1_3 = np.transpose( np.array([alpha_1_3]) )
K_t_J_m = np.dot( np.transpose(Currents_1_3), Alpha_1_3 )[0][0] / \
          np.dot( np.transpose(Currents_1_3), Currents_1_3 )[0][0]
print('-------------------------------')
print('K_t / J_m')
print(K_t_J_m)  # phi
print('-------------------------------')


# Calculating K_t, J_m, and J_F together from plot_2_3
currents_2_3 = [250,    280,    300,    330]  # in mA
alpha_m_2_3  = [13.75,  17.85,  26.6,   27.3]  # V/s, not velocity
alpha_2_3 = [point / K_tach for point in alpha_m_2_3]

Currents_2_3 = np.transpose( np.array([currents_2_3]) )
Alpha_2_3 = np.transpose( np.array([alpha_2_3]) )
K_t_J_m_J_F = np.dot( np.transpose(Currents_2_3), Alpha_2_3 )[0][0] / \
              np.dot( np.transpose(Currents_2_3), Currents_2_3 )[0][0]
print('-------------------------------')
print('K_t / (J_m + J_F)')
print(K_t_J_m_J_F)  # psi
print('-------------------------------')


# Calculating J_m and K_t
J_m = K_t_J_m_J_F * J_F / (K_t_J_m - K_t_J_m_J_F)
K_t = J_m * K_t_J_m_J_F
print('-------------------------------')
print('*** J_m ***')
print(J_m)
print('-------------------------------')
print('-------------------------------')
print('*** K_t ***')
print(K_t)
print('-------------------------------')



# Calculating \tau_m (from plot_2_2)
ten_per_array = [[1.33,    2.71],
                 [0.791,   1.778],
                 [3.067,   4.2165],
                 [0.7875,  1.7025],
                 [2.916,    2.049]]
ninety_per_array = [[1.368,   2.753],
                    [0.835,   1.823],
                    [3.158,   4.232],
                    [0.830,   1.752],
                    [2.961,   2.087]]
dt_array = []
for i in range(len(ten_per_array)):
    for j in range(len(ten_per_array[i])):
        dt_array.append(ninety_per_array[i][j] - ten_per_array[i][j])
dt_avg = np.mean(dt_array)
tau_m = dt_avg / 2.2
print('-------------------------------')
print('*** \\tau_m (s) ***')
print(tau_m)
print('-------------------------------')
