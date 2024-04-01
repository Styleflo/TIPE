import networkx as nx
import matplotlib.pyplot as plt

# Dictionnaire des sommets du graphe orienté et pondéré
dico = {'A': {'B': 1, 'D': 2},
        'B': {'C': 3, 'E': 4},
        'C': {'E': 5, 'I': 34},
        'D': {'E': 6, 'B': 5},
        'E': {'D': 34, 'G': 23},
        'F': {'A': 2, 'D': 4},
        'G': {'C': 4, 'F': 3},
        'H': {'G': 3, 'A': 1, 'C': 12},
        'I': {'H': 3, 'D': 24}}


def Representation_graphique(dico):
    # Création du graphe orienté et pondéré à partir du dictionnaire
    G1 = nx.DiGraph()
    G2 = nx.DiGraph()
    G3 = nx.DiGraph()
    # G4 = nx.complete_graph(10)
    for sommet, voisins in dico.items():
        for voisin, poids in voisins.items():
            G1.add_edge(sommet, voisin, weight=poids)
            G2.add_edge(voisin, sommet, weight=poids)
            G3.add_edge(sommet, voisin, weight=poids)
            G3.add_edge(voisin, sommet, weight=poids)

    # Positionnement des sommets avec l'algorithme de Fruchterman-Reingold
    pos = nx.spring_layout(G1)
    #pos2 = nx.spring_layout(G4)

    # Affichage du graphe orienté et pondéré avec les étiquettes des sommets
    plt.figure(1)
    nx.draw_networkx(G1, pos, with_labels=True)

    # Affichage des poids des arêtes
    labels = nx.get_edge_attributes(G1, 'weight')
    labels2 = nx.get_edge_attributes(G2, 'weight')
    nx.draw_networkx_edge_labels(G1, pos, edge_labels=labels)

    plt.figure(2)
    nx.draw_networkx(G2, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G2, pos, edge_labels=labels2)

    plt.show()

    plt.figure(3)

    nx.draw_networkx(G3, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G3, pos, edge_labels=labels2)

    plt.figure(4)

    nx.draw(G3)

    plt.show()

    # plt.figure(5)
    # nx.draw_networkx(G4, pos2)
    # nx.draw_networkx(G4, pos2)
    # plt.show()


print(Representation_graphique(dico))



