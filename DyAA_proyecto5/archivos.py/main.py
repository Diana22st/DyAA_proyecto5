from grafo import guardar_grafo
from grafo import Grafo

# Generamos grafo de mallas con 30 nodos
grafo_malla_30 = Grafo(dirigido=False)
grafo_malla_30.grafo_malla(5, 6)
grafo_malla_30.layout()

# Generamos grafo de mallas con 500 nodos
grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10)
grafo_malla_500.layout()

# Generamos grafo Erdös y Rényi con 30 nodos y 200 aristas
grafo_erdos_30_200 = Grafo(dirigido=False)
grafo_erdos_30_200.grafo_erdos_renyi(30, 200)
grafo_erdos_30_200.layout()


# generamos grafo con modelo de Gilbert 30 nodos y probabilidad 0.5
grafo_gilbert_30_05 = Grafo(dirigido=False)
grafo_gilbert_30_05.grafo_gilbert(30, 0.5)
grafo_gilbert_30_05.layout()


# generamos grafo con modelo geográfico simple con 30 nodos y r=0.5
grafo_geografico_30_05 = Grafo(dirigido=False)
grafo_geografico_30_05.grafo_geografico(30, 0.5)
grafo_geografico_30_05.layout()

# generamos grafo con modelo Barabási-Albert con 30 nodos y grado 10
grafo_babarasi_30_10 = Grafo(dirigido=False)
grafo_babarasi_30_10.grafo_barabasi_albert(30, 10, False, False)
grafo_babarasi_30_10.layout()


# generamos grafo con modelo Dorogovtsev-Mendes con 30 nodos
grafo_dorogovtsev_mendes_30 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_30.dorogovtsev_mendes(30)
grafo_dorogovtsev_mendes_30.layout()
