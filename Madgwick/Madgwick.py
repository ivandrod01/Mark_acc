import numpy as np
import ahrs
from ahrs.filters import Madgwick
import numpy as np
from ahrs.filters import Madgwick
import matplotlib.pyplot as plt
from squaternion import Quaternion
import integrations
import calculate
import math



data = np.loadtxt(f'acc1.csv', delimiter=',', skiprows=1)
gyro = np.loadtxt(f'gyr1.csv', delimiter=',', skiprows=1)

timestamps = data[6:,0]
acc = data[6:,1:4]
gyro = gyro[:,1:4]


# deg/s to rad/s
gyro *= 0.017453


# Sampling rate
deltat = 0.01 # 100Hz

# Start Madgwick estimation
madgwick = Madgwick(acc=acc, gyr=gyro, frequency=100) # Returns Quaternions

# Saving madgwick estimations to array
estimation = []

# Array with integrated distances
dist_data = []

# For every row of data
for t in range(1, len(acc)):
    # Integrate distance from X-axis acceleration
    positX, distanceX = calculate.distance(acc[t][0], acc[t][1], acc[t][2], deltat)
    dist_data.append(distanceX)
    q = Quaternion(madgwick.Q[t][0],madgwick.Q[t][1],madgwick.Q[t][2],madgwick.Q[t][3])
    # Convert estimated quaternion AHRS to euler angles
    estimation.append(q.to_euler(degrees=True))

# Convert estimation to numpy array
estimation = np.array(estimation)

positions = []

for index, distance in enumerate(dist_data,start=-1) :
    # Calculate X, Y, Z positions - Distance * heading angle. Update the coordinate with each function
    coordinateX, coordinateY, coordinateZ = integrations.getCoordinate()
    positionX = distance * math.cos(math.radians(estimation[index][2])) + coordinateX
    positionY = distance * math.sin(math.radians(estimation[index][2])) + coordinateY
    positionZ = distance * math.sin(math.radians(estimation[index][0])) + coordinateZ
    positions.append([positionX,positionY,positionZ])
    integrations.updateCoordinates(positionX, positionY, positionZ)


x, y, z = [], [], []

for position in positions:
    x.append(position[0])
    y.append(position[1])
    z.append(position[2])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z)

plt.savefig(f"plot_mag_1_acc.png")












#
#
# # Create an instance of the Madgwick filter
# madgwick_filter = Madgwick()
#
# # Optional: Set the initial quaternion
# quaternions = Q = np.tile([1., 0., 0., 0.], (len(gyro), 1))
# madgwick_filter.quaternion = quaternions[0]
#
#
#
# for i in range(1, len(timestamps)):
#     dt = timestamps[i] - timestamps[i - 1]
#     madgwick_filter.Dt = dt/1000#use madgwick_filter.smaple_period
#     q = madgwick_filter.updateIMU(quaternions[i-1],gyro[i], acc[i])
#     quaternions[i] = q
#
# quaternions = np.array(quaternions)
# for quaternion in quaternions:
#     print(quaternion)