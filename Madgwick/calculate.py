import integrations


def distance(acceleration_linX, acceleration_linY, acceleration_linZ, deltat):
    """
    Returns the X, Y and Z position
    """
    acceleration_linX = abs(acceleration_linX)
    acceleration_linY = abs(acceleration_linY)
    if -0.05 <= acceleration_linX <= 0.05:
        acceleration_linX = 0.0
        velocityX = integrations.getVelocityX(acceleration_linX, deltat)
    else:
        velocityX = integrations.getVelocityX(acceleration_linX, deltat)

    if -0.05 <= acceleration_linY <= 0.05:
        acceleration_linY = 0.0
        velocityY = integrations.getVelocityY(acceleration_linY, deltat)
    else:
        velocityY = integrations.getVelocityY(acceleration_linY, deltat)

    if -0.05 <= acceleration_linZ <= 0.05:
        acceleration_linZ = 0.0
        velocityZ = integrations.getVelocityZ(acceleration_linZ, deltat)
    else:
        velocityZ = integrations.getVelocityZ(acceleration_linZ, deltat)
        
    positionX, distanceX = integrations.getPositionX(velocityX, acceleration_linX, deltat)
    # positionY = integrations.getPositionY(velocityY, acceleration_linY, deltat)
    # positionZ = integrations.getPositionZ(velocityZ, acceleration_linZ, deltat)
    # displacement = integrations.getDisplacement(velocity, position)
    return positionX, distanceX#, positionY, positionZ
