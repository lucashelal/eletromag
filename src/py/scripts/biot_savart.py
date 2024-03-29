
# associaar um vetor para o campo e plotar o gráfico em R3
## calcular a integral, os valores de campo, associar um vetor para o campo e plotar o gráfico em R3
### asssumindo que o condutor é retilineo 

#### parametros da funcao - funcao, intervalo de integracao, parametros da funcao a ser integrada
import matplotlib.pyplot as plt
import scipy.constants as sconst
import scipy.integrate as sint
import numpy as np

I = 1
L = 1

def integrand(x, xp, yp, zp):
    return 1/(((xp - x)**2 + yp**2 + zp**2)**(3/2))

xp_list = np.linspace(-1, 2, 4)
yp_list = np.linspace(-1, 2, 15)
zp_list = np.linspace(-1, 2, 15)
  
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d') # implica dizer que sao 3 dimensoes e sera 3D

for xp in xp_list:
  for yp in yp_list:
    for zp in zp_list:
      # resultado da integral
      result = sint.quad(integrand, 0, L, args=(xp, yp, zp))
      
      # campo magnetico - valores de campo
      bx = 0
      by = -sconst.mu_0 * I / (4*np.pi) * zp * result[0]
      bz = sconst.mu_0 * I / (4*np.pi) * yp * result[0]
      
      # vetor do campo
      
      ax.quiver(xp, yp, zp, bx, by, bz, length=1e6)

# plotar o condutor, vetores, campo, etc

ax.plot3D([0, 1], [0, 0], [0, 0], color='black', linewidth=5) # condutor
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')
plt.show()

