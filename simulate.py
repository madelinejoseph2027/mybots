#Imports
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random


#Set up world
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")


#Launch world
pyrosim.Prepare_To_Simulate(robotId)


#Variables for simulating robots
iterations = 1000

backLegAmplitude = np.pi/4.0
backLegFrequency = 6
backLegPhaseOffset = 0
frontLegAmplitude = np.pi/4.0
frontLegFrequency = 6
frontLegPhaseOffset = np.pi/3.0

angleRange = np.linspace(0, 2*np.pi, iterations+1)
backTargetAngles = backLegAmplitude*np.sin(backLegFrequency*angleRange+backLegPhaseOffset)
frontTargetAngles = frontLegAmplitude*np.sin(frontLegFrequency*angleRange+frontLegPhaseOffset)

maxForce = 100

backLegSensorValues = np.zeros(iterations)
frontLegSensorValues = np.zeros(iterations)


#Simulate robots
for i in range(iterations):
    #Step simulation
    p.stepSimulation()
    
    #Track sensor values in each link
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    #Put motors in each joint
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = 'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = backTargetAngles[i],
        maxForce = maxForce)
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = 'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = frontTargetAngles[i],
        maxForce = maxForce)
    
    #Slow down the stepping so we can see things happening the world
    time.sleep(1/240)


#Save sensor values
np.save("data/backLegSensorValues", backLegSensorValues)
np.save("data/frontLegSensorValues", frontLegSensorValues)


#Shut down GUI
p.disconnect()



#print(backLegSensorValues)
#print(frontLegSensorValues)
