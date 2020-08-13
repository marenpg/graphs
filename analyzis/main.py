import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


G = nx.read_graphml("graphml_bg.xsd")

# not supported
# centrality = nx.eigenvector_centrality(G)
# top10 = sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())[:5]

pr = nx.pagerank(G, alpha=0.9)

print(G.number_of_nodes())
