import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def _creaGrafo(self, anno, salario):
        self._nodes = DAO.getAllNodes(anno, salario)
        self._grafo.add_nodes_from(self._nodes)
        nodi = self._nodes
        for u in nodi:
            for v in nodi:
                if u != v:
                    arco = DAO.getEdge(u.playerID, v.playerID, anno)
                    if arco != []:
                        self._grafo.add_edge(u, v)
        for n in nodi:
            teams = DAO.getTeams(n.playerID, anno)
            n.setTeams(teams)


    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getGradoMax(self):
        gradi = []
        for n in self._nodes:
            grado = self._grafo.degree(n)
            gradi.append((n, grado))
        gradi.sort(key=lambda x: x[1], reverse=True)
        return gradi[0]

    def getNumConnesse(self):
        nConnesse = nx.number_connected_components(self._grafo)
        return nConnesse

    def handleDreamTeam(self):
        self._dreamTeam = []
        self._dreamSalary = 0
        self._setNodi = set()
        for n in self._nodes:
            self._setNodi.add(n)
        for n in self._nodes:
            self._ricorsione(n, [])
        return self._dreamTeam, self._dreamSalary

    def _ricorsione(self, nodo, parziale):
        salarioParziale = self.salarioParziale(parziale)
        if len(parziale) > 0:
            if len(parziale) > len(self._dreamTeam) and salarioParziale > self._dreamSalary:
                self._dreamSalary = salarioParziale
                self._dreamTeam = copy.deepcopy(parziale)
        vicini = self._grafo.neighbors(nodo)
        setVicini = set()
        for v in vicini:
            setVicini.add(v)
        non_vicini = self._setNodi - setVicini
        for nv in non_vicini:
            if self.filtroP(nv, parziale):
                parziale.append(nv)
                self._ricorsione(nv, parziale)


    def filtroNodi(self, v, parziale):  # no percorso semplice, non serve
        pass

    def filtroArchi(self, n, v, parziale):
        pass

    def salarioParziale(self, parziale):
        totS = 0
        for p in parziale:
            totS += p.salary
        return totS

    def filtroP(self, nv, parziale):
        for p in parziale:
            if nv == p:
                return False
        return True
