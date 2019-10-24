import networkx as nx
import matplotlib.pyplot as plt

from common.tasks import getTasks
from common.modules import brain_modules

def printGraph(graph):
    nx.draw(graph, with_labels=True)
    plt.show()
    
def buildGraph(brain_modules, tasks):
    G = nx.Graph()
    for module in brain_modules:
        G.add_node(module, name=module.name)

    for task in tasks:
        G.add_node(task, task=task.name)
        for mod in task.brain_modules:
            G.add_edge(task, mod, weight='100')

    return G

if(__name__ == "__main__"):
    print("Main called")
    tasks = getTasks()
    graph = buildGraph(brain_modules, tasks)
    printGraph(graph)

# G = nx.Graph()
# G.add_node(1)
# G.add_nodes_from([22, 55])

# H = nx.path_graph(5)
# G.add_node(H)

# G.add_edges_from([(22, 55)])
# G.add_edges_from(H.edges)
# G.add_edge(55, H)
# G.add_edge(1, 55)
# G[1][2]['color'] = "blue"

# print(G.degree([2, 3]))

# printGraph(G)

# H = nx.DiGraph(G) # directed graph
# edgelist = [(0, 1), (1, 2), (2, 3)]
# H = nx.DiGraph(edgelist)

# printGraph(H)

# # Ignore all edges: 
# G.clear()



