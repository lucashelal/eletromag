fig = plt.figure(figsize=(10, 10))
# No parâmetro figsize definimos o tamanho da figura
ax = fig.add_subplot(111, projection='3d')
# (É importante que coloquemos o projection = '3d' para indicar que nosso gráfico será em 3 dimensões)

for xp in xp_list:
    for yp in yp_list:
        for zp in zp_list:
            # Resultado da integração
            result = sint.quad(integrand, 0, L, args=(xp, yp, zp))

            # Valores de cada componente do campo
            bx = 0
            by = -sconst.mu_0*I/(4*np.pi)*zp*result[0]
            bz = sconst.mu_0*I/(4*np.pi)*yp*result[0]

            # Normalizando as componentes do campo
            modb = np.sqrt(bx**2 + by**2 + bz**2)
            bxnorm = bx/modb
            bynorm = by/modb
            bznorm = bz/modb

            # Definindo um vetor no gráfico (normalizado)
            ax.quiver(xp, yp, zp, bxnorm, bynorm, bznorm, length=0.2)

# Definindo os parâmetros do gráfico e plotando
ax.plot3D([0,1],[0,0],[0,0], color="black", linewidth = 5) # Plotando o fio retilínio
ax.set_xlim([-1,2])
ax.set_ylim([-1,2])
ax.set_zlim([-1,2])
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')
plt.show()