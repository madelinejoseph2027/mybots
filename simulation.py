#Imports
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
#import numpy as np
#import random
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
            #Set up world
            self.physicsClient = p.connect(p.GUI)
            p.setAdditionalSearchPath(pybullet_data.getDataPath())

            p.setGravity(0,0,-9.8)
            
            self.world = WORLD()
            self.robot = ROBOT()

    def Run(self):
        for i in range(c.iterations):
            p.stepSimulation()
            time.sleep(c.sleep)
                        
    def __del__(self):
        p.disconnect()