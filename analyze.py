#Importsimport numpy as npimport matplotlib.pyplot as plt#Load saved sensor valuesbackLegSensorValues = np.load("data/backLegSensorValues.npy")frontLegSensorValues = np.load("data/frontLegSensorValues.npy")#Plottingplt.plot(backLegSensorValues, label = "Back Leg",linewidth = 3)plt.plot(frontLegSensorValues, label = "Front Leg")plt.title("Front and Back Leg Sensor Values")plt.xlabel("Step")plt.ylabel("Sensor Value")plt.legend()plt.show()