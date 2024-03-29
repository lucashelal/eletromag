import matplotlib.pyplot as plt
import scipy.constants as sconst
import scipy.integrate as sint
import numpy as np

I = 1
L = 1

def integrand(x, xp, yp, zp):
    return 1/(((xp - x)**2 + yp**2 + zp**2)**(3/2))

zp_list2 = np.linspace(0.01, 1, 100)
modb_list = []
modbinf_list = []

for zp in zp_list2:
    # Resultado da integração
    xp = 0.5
    yp = 0
    result = sint.quad(integrand, 0, L, args=(xp, yp, zp))

    # Valores de cada componente do campo
    bx = 0
    by = -sconst.mu_0*I/(4*np.pi)*zp*result[0]
    bz = sconst.mu_0*I/(4*np.pi)*yp*result[0]

    # Cálculo do módulo do campo numérico
    modb = np.sqrt(bx**2 + by**2 + bz**2)
    modb_list.append(modb)

    # Cálculo do campo no fio infinito
    modbinf = sconst.mu_0*I/(2*np.pi*zp)
    modbinf_list.append(modbinf)
    
# Plotando o gráfico
plt.plot(zp_list2, modb_list, "o", label="Fio finito utilizando o método numérico", markersize = 2)
plt.plot(zp_list2, modbinf_list, label="Fio infinito utilizando a expressão conhecida")
plt.legend()
plt.xlabel(r'$z_p$ (m)')
plt.ylabel(r'$|\vec{B}|$ (T)')
plt.title(r'Gráfico de $|\vec{B}|$ vs $z_p$')
plt.show()