from numpy import pi
import numpy as np


# Calculating ACTUAL \dot{\theta}
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
print('K_{tach} (V/rad)')
print(K_tach)
print('-------------------------------')
