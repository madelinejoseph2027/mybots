# #Imports
# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy as np
# import random
# import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()

# #Variables for simulating robots
# angleRange = np.linspace(0, 2*np.pi, c.iterations+1)
# backTargetAngles = c.backLegAmplitude*np.sin(c.backLegFrequency*angleRange+c.backLegPhaseOffset)
# frontTargetAngles = c.frontLegAmplitude*np.sin(c.frontLegFrequency*angleRange+c.frontLegPhaseOffset)

# backLegSensorValues = np.zeros(c.iterations)
# frontLegSensorValues = np.zeros(c.iterations)


# #Simulate robots
# for i in range(c.iterations):
#     #Step simulation
#     p.stepSimulation()
    
#     #Track sensor values in each link
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
#     #Put motors in each joint
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = 'Torso_BackLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = backTargetAngles[i],
#         maxForce = c.maxForce)
    
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = 'Torso_FrontLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = frontTargetAngles[i],
#         maxForce = c.maxForce)
    
#     #Slow down the stepping so we can see things happening the world
#     time.sleep(c.sleep)


# #Save sensor values
# np.save("data/backLegSensorValues", backLegSensorValues)
# np.save("data/frontLegSensorValues", frontLegSensorValues)


# #Shut down GUI
# p.disconnect()
