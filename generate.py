import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

x = 0
y = 0
z = 0.5

length = 1
width = 1
height = 1

X = x
Y = y
Z = z
W = width
L = length
H = height

for k in range (8):
    for j in range (8): 
        for i in range (8):
            pyrosim.Send_Cube(name="Box", pos=[i,j,Z+k] , size=[W*0.9**k,L*0.9**k,H*0.9**k])
            

pyrosim.End()
