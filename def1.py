from pyquaternion import Quaternion
import numpy as np
import matplotlib.pyplot as plt


def quaternion_rotation(angular_vel, dt):
    angle = np.linalg.norm(angular_vel) * dt
    if angle < 1e-9:
        return Quaternion(1, 0, 0, 0)

    axis = angular_vel / np.linalg.norm(angular_vel)
    q_rot = Quaternion(axis=axis, angle=angle)
    return q_rot


def compute_translation_local(acc, dt, local_velocity):

    #integrated velocity
    int_velocity = local_velocity + acc * dt
    print(int_velocity,acc)
    #displacement
    dp = int_velocity * dt #+ 0.5 * acc * (dt ** 2)

    return dp, int_velocity

def cumulative_sum_vector(cum_vector, vector ):
    return_vector = np.zeros(3)
    for i in range(len(vector)):
        return_vector[i]=cum_vector[i]+vector[i]
    return return_vector

def dt(t, t_plus_dt):
    return (t_plus_dt-t)/1000#
