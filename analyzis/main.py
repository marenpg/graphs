import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_graphml("graphml_digraph.graphml")

def getMaxScore(res):
  max_score = 0
  for (_, score) in res.items():
    if score > max_score:
      max_score = score
  print("Max score:", max_score)

def getTopK(k, res, name="Top k:"):
  print("\n" + name)
  sorted_keys = sorted(res, key=res.get, reverse=True)
  topK = [(key, res[key]) for key in sorted_keys[:10]]
  for nodeId in sorted_keys[:k]:
    node = G.nodes[nodeId]
    score = res[nodeId]
    print(node, score)

  return topK


def run_graph_algs():
  # Whole graph
  centrality = nx.eigenvector_centrality(G)
  page_rank = nx.pagerank(G, alpha=0.9)
  hits = nx.hits(G)
  closeness_centrality = nx.closeness_centrality(G)
  betweenness_centrality = nx.betweenness_centrality(G)

  getTopK(10, centrality, "Centrality:")
  getTopK(10, page_rank, "Page rank:")
  getTopK(10, hits[0], "HITS: Hubs:")
  getTopK(10, hits[1], "HITS: Authorities:")
  getTopK(10, closeness_centrality, "Closeness centrality:")
  getTopK(10, betweenness_centrality, "Betweenness centrality:")

### SimRank:
def run_similarity_algs():
  def get_similar_nodes(nodeId):
    node = G.nodes[nodeId]
    similar_nodes = nx.simrank_similarity(G, source=node)
    print(node[0]["name"], similar_nodes)
### Similarity of brain regions:
  regions = [nodeId for nodeId, data in G.nodes(data=True) if ":BrainRegion" in data["TYPE"]]
  print(regions)
  for regId in regions:
    get_similar_nodes(regId)
    
  simrank_similarity_numpy = nx.simrank_similarity(G)
  print(simrank_similarity_numpy)
  ### Similarity of analyses


  ### Similarty of adusjted analyses
  # simrank_similarity_numpy = nx.simrank_similarity(G)
  # getTopK(10, simrank_similarity_numpy, "Simrank similarity numpy:")

def run_assortativity_algs():
  # Assortativity:
  degree_pearson_correlation_coefficient = nx.degree_pearson_correlation_coefficient(G)
  attribute_assortativity_coefficient = nx.attribute_assortativity_coefficient(G, "TYPE")

  print(degree_pearson_correlation_coefficient)  #-0.15024634421536287
  print(attribute_assortativity_coefficient) #0.004532346525456586 on TYPE

# Figure out why it is too slow to finish
# Try out https://igraph.org/python/doc/igraph.GraphBase-class.html and https://networkit.github.io/dev-docs/search.html?q=similarity for similarities


run_graph_algs()