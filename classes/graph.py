import pandas as pd
import networkx as nx
import dbUtils.get_assets_prices as pcs 
import dbUtils.get_returns as ret
import dbUtils.get_assets as assets

class Graph:

    def __init__(self,app):

        self.prices =  pcs.get_prices(app)
        self.returns = ret.get_returns(app)
        self._app = app
        self.corr_matrix = self.returns.corr()
    
    def create_graph(self):
        self.graph = nx.Graph()
        for ativo in self.corr_matrix.columns:
            self.graph.add_node(ativo)

        for i, ativo1 in enumerate(self.corr_matrix.columns):
            for j, ativo2 in enumerate(self.corr_matrix.columns):
                if i < j:
                    correlation = self.corr_matrix.iloc[i, j]
                    self.graph.add_edge(ativo1, ativo2, weight=correlation)


    def mst(self):
        self.MST = nx.minimum_spanning_tree(self.graph)
        return self.MST
    



