import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from pyvis.network import Network

def read_json(filename):
    with open(filename, 'r') as f:
        full_list = json.load(f)
    return full_list

file = read_json("resources/normal.json")


# #                    To graph with NetworkX

# Nodesf
nodes = [i for i in file if file[i]["neededFor"] and file[i]["producedFrom"]]
print (nodes)


# Edges
edges = []
for i in file:
    try:
        for j in file[i]["neededFor"]:
            edges.append((i,j))
    except:
        pass
print(edges)

# Create graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

print(G.degree)
print(G.adj)

nx.draw_circular(G, node_size=30)
# nx.draw_shell(G, node_size=30)

net = Network(notebook=True)
net.from_nx(G)

net.show("example.html")

