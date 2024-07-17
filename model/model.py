from database.DAO import DAO
import networkx as nx
from geopy.distance import geodesic
class Model:
    def __init__(self):
        self.shapes = []
        self.myGraph = nx.Graph()
        self.stati = DAO.stati()

    def add_shapes(self,anno):
        self.shapes = DAO.get_shape(anno)
        return self.shapes

    def buildGraph(self, anno, forma):
        #creo nodi
        self.myGraph.add_nodes_from(self.stati)
        for state in self.stati:
            vicini = DAO.neighborns(state)
            nState = DAO.peso_stati(state, forma, anno)
            for neighbor in vicini:
                if self.myGraph.has_edge(state,neighbor):
                    print()
                else:
                    count = DAO.peso_stati(neighbor, forma, anno)
                    self.myGraph.add_edge(state,neighbor, weight = count[0] + nState[0])

        print(self.myGraph)

    def pesoarchi(self, stato, stato2 ):
        peso = DAO.peso_stati(stato, stato2)
        return peso


    def ricorsione(self, parziale,parziale_archi, count):
        bool,edge = self.archi_liberi(parziale)
        neighbors = self.archi_ammissibili(parziale[-1], )
        if bool == 0:
            print(parziale)

        else:
            conta_arco = 0
            """for edge in self.myGraph.edges:
                    print(edge)
                    parziale.append(edge)
                    self.ricorsione(parziale, count+1)
                    parziale.pop()"""
            for node in neighbors:
                print(f"nodo aggiunto al parziale: {node}")
                parziale.append(node)
                self.ricorsione(parziale, count+1)
                parziale.pop()
    def archi_liberi(self, parziale):
        if parziale != []:
            for neighbor in self.myGraph.neighbors(parziale[-1]):
                if neighbor not in parziale:
                    return 1, (parziale[-1], neighbor)
                else:
                    bool = 0
            return 0
        else:
            return 1, ("","")
    def archi_liberi(self, parziale):
        if parziale != []:
            ultimo = parziale[-1][1]
            print(ultimo)
            for neighbor in self.myGraph.neighbors(ultimo):
                tupla = (neighbor, ultimo)
                print(tupla)
                if tupla in parziale:
                    bool = 0
                else:
                    bool = 1
                    return bool
        else:
            bool = 1
            return bool





