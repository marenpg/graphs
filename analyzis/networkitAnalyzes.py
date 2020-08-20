import matplotlib.pyplot as plt
import networkit as nk

# FROM https://github.com/networkit/networkit/blob/Dev/notebooks/User-Guide.ipynb

#g = networkit.graphio.GraphMLReader("graphml_bg.graphml")
G = nk.readGraph("graphml_bg.graphml", nk.Format.GraphML)

nk.overview(G)

# communities = community.detectCommunities(G)
# print(communities)


cc = nk.components.StronglyConnectedComponents(G)
cc.run()
print("number of components ", cc.numberOfComponents())
v = 0
print("component of node ", v , ": " , cc.componentOfNode(0))
#print("map of component sizes: ", cc.getComponentSizes())


dd = sorted(nk.centrality.DegreeCentrality(G).run().scores(), reverse=True)
plt.xscale("log")
plt.xlabel("degree")
plt.yscale("log")
plt.ylabel("number of nodes")
plt.plot(dd)
#plt.show()

bc = nk.centrality.Betweenness(G)
bc.run()

print(bc.ranking()[:10]) # the 10 most central nodes