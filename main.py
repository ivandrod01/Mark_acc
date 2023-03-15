from pyquaternion import Quaternion
import numpy as np
import matplotlib.pyplot as plt
from def1 import quaternion_rotation, compute_translation_local, dt, cumulative_sum_vector

# Load the CSV file into a numpy array
data = np.loadtxt('lacc.csv', delimiter=',', skiprows=1)

new_row = np.array([data[0][0] - 10, 0, 0, 0])
data = np.vstack((new_row, data))
# Extract the second, third, and fourth columns into a new array


velocity_local = [0, 0, 0]
orientation = Quaternion(1, 0, 0, 0)

position = np.zeros((1, 3))
position[0] = np.array([0, 0, 0])

sum_accel = np.array([0,0,0])
sum_time = 0

average_set = 10

for i in range(data.shape[0]-1):
    delta_t = dt(data[i][0], data[i + 1][0])

    if i % average_set != 0 and i != 0:
        sum_accel = cumulative_sum_vector(sum_accel, data[i][1:4])
        sum_time += delta_t

    else:
        displacement, velocity_local = compute_translation_local(sum_accel/average_set, sum_time,
                                                                 velocity_local)
        new_position = [position[-1][j] + displacement[j] for j in range(3)]

        position = np.vstack([position,new_position])
        sum_accel = data[i][1:4]
        sum_time = delta_t

    # Store position for plotting or further analysis
x1, y1, z1 = [], [], []
for posit in position:
    x1.append(posit[0])
    y1.append(posit[1])
    z1.append(posit[2])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x1, y1, z1)
plt.show()#
