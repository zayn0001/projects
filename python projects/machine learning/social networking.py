import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(['u','v'])
G.nodes()

G.add_edge(1,2)
G.add_edge(2,'v')

G.add_edges_from([(1,3),(1,4),(1,5),(1,6)])
G.add_edge('u','w')
G.edges

G.remove_node(2)
G.remove_nodes_from([4,5])
G.remove_edge(1,3)
G.remove_edges_from([(1,4),(1,5)])
G.number_of_edges()
G.number_of_nodes()

G = nx.karate_club_graph()

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
#nx.draw(G, with_labels=True,node_color='lightblue',edge_color='gray')

G.degree()
G.degree()[33]
G.degree(33)

#Erdos-Renyi graph

from scipy.stats import bernoulli
#bernoulli.rvs(p=0.2)


p = 0.2
N = 20
def er_graph(N,p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1<node2 and bernoulli.rvs(p=p):
                G.add_edge(node1,node2)
    return G

#nx.draw(er_graph(N,p), node_size=40)


def plot_degree_distribution(G):
    degree_sequence = [d for n,d in G.degree()]
    plt.hist(degree_sequence, histtype='step')
    plt.xlabel('Degree $k$')
    plt.ylabel('$P(k)$')
    plt.title('Degree distribution')

plt.figure()
G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
G4 = er_graph(500, 0.08)
plot_degree_distribution(G4)
plt.show()

G5 = nx.erdos_renyi_graph(100, 0.03)
G6 = nx.erdos_renyi_graph(100, 0.30)
plot_degree_distribution(G5)
plot_degree_distribution(G6)
plt.show()



import numpy as np
A1 = np.loadtxt('C:\\Users\\mishal\\Desktop\\pdfs\\adj_allVillageRelationships_vilno_1.csv', delimiter=',')
A2 = np.loadtxt('C:\\Users\\mishal\\Desktop\\pdfs\\adj_allVillageRelationships_vilno_2.csv',delimiter=',')

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    degree_sequence = [d for n,d in G.degree()]
    print("Average degreee: %.2f" % np.mean(degree_sequence))

basic_net_stats(G1)
basic_net_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.show()

G1_CCS = (G1.subgraph(c) for c in nx.connected_components(G1))
G2_CCS = (G2.subgraph(c) for c in nx.connected_components(G2))
#g = gen.__next__()

G1_LCC = max(G1_CCS,key=len)
G2_LCC = max(G2_CCS,key=len)

G1_LCC.number_of_nodes()/G1.number_of_nodes()   #fraction of nodes contained in the lcc
G2_LCC.number_of_nodes()/G2.number_of_nodes()

plt.figure(figsize=(20,20))
plt.subplot(221)
nx.draw(G1_LCC, node_color='red', edge_color='gray', node_size=10)
plt.subplot(223)
nx.draw(G2_LCC, node_color='green', edge_color='gray', node_size=10)
plt.savefig('C:\\Users\\mishal\\Desktop\\pdfs\\village_relationships.pdf')
