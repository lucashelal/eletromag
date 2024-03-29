import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load seaborn
sns.set_theme()

# constants definition

d = 0.001 # cable width in meters
R_H = 1e-3 # Hall coefficient in m^3/C

# magnetic field space 
B = np.linspace(0.01, 1, 1000) # 0.01 T to 1 T

# voltages

V_220 = 220
V_127 = 127

# lets assume that V_H is proportional to V - add a factor
k = 0.1
V_H_220 = k * V_220
V_H_127 = k * V_127

# current as function of B for either 220 or 127 V
I_220 = (V_H_220 * d) / (R_H * B)
I_127 = (V_H_127 * d) / (R_H * B)

# create a dataframe

data = np.column_stack((B, I_220, I_127))
data = pd.DataFrame(data, columns=['B', 'I_220', 'I_127'])
data_melted = pd.melt(data, id_vars='B', value_vars=['I_220', 'I_127'], var_name='Voltage', value_name='Current')

# plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='B',y='Current', hue='Voltage', data=data_melted)
plt.title('Current as function of magnetic field for different voltages')
plt.grid(True)
plt.show()