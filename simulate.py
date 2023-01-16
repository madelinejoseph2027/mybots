#Imports
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

#Set up world
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

#Launch world
pyrosim.Prepare_To_Simulate(robotId)

#Simulate robots
iterations = 1000

backLegSensorValues = np.zeros(iterations)
frontLegSensorValues = np.zeros(iterations)

for i in range(iterations):
    p.stepSimulation()
    
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    time.sleep(1/60)
    #print(i)

#Save sensor values
np.save("data/backLegSensorValues", backLegSensorValues)
np.save("data/frontLegSensorValues", frontLegSensorValues)

#Shut down GUI
p.disconnect()

#print(backLegSensorValues)
#print(frontLegSensorValues)

