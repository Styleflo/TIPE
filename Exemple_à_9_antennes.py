import Classes as cl
import matplotlib.pyplot as plt

#Donnée des antennes, depend du nombres posées dans une zone
a = cl.antennes(0, '3g', 0, 0, {1: 100, 2: 100, 3: 100, 4: 100},0)
b = cl.antennes(1, '4g', 1, 1, {0: 100, 5: 100, 8: 1000},0)
c = cl.antennes(2, '5g', 1, -1, {0: 100, 5: 100, 6: 10000},0)
d = cl.antennes(3, '3g', -1, -1, {0: 100, 6: 100, 7: 100},0)
e = cl.antennes(4, '4g', -1, 1, {0: 100, 7: 1000, 8: 1000},0)
f = cl.antennes(5, '3g', 2, 0, {1: 100, 2: 100},0)
g = cl.antennes(6, '5g', 0, -2, {2: 10000, 3: 100},0)
h = cl.antennes(7, '4g', -2, 0, {3: 100, 4: 1000},0)
i = cl.antennes(8, '4g', 0, 2, {4: 1000, 1: 1000},0)

# donnée du dictionnaire d'adjascence construit avec les antennes
dico = {0: {1: 100, 2: 100, 3: 100, 4: 100}, 1: {0: 100, 5: 100, 8: 1000},
        2: {0: 100, 5: 100, 6: 10000}, 3: {0: 100, 6: 100, 7: 100},
        4: {0: 100, 7: 1000, 8: 1000}, 5: {1: 100, 2: 100},
        6: {2: 10000, 3: 100}, 7: {3: 100, 4: 1000}, 8: {4: 1000, 1: 1000}}

#Donne la représentation des antennes selon cette distribution avec reliée entres elles de proche en proche.
def representation_antennes(l):
    fig, ax = plt.subplots()
    cercle = plt.Circle((0, 0), 2, color=(0.8, 0.8, 0.8))
    plt.xlim(- 2 - 0.3, 2 + 0.3)
    plt.ylim(- 2 - 0.3, 2 + 0.3)
    ax.set_aspect(1)
    ax.add_artist(cercle)
    for val in l:
        a = val.pos()
        b = val.name()
        plt.plot(a[0], a[1], c=val.couleurs(), marker='+', markersize=10)
        plt.text(a[0]-0.2, a[1]-0.2, b)
    plt.plot([], [], label='3g' + '=' + 'noir', c='black', marker='+', markersize=10)
    plt.plot([], [], label='4g' + '=' + 'rouge', c='red', marker='+', markersize=10)
    plt.plot([], [], label='5g' + '=' + 'jaune', c='yellow', marker='+', markersize=10)
    plt.legend()
    plt.title("Exemple à 9 antennes")
    plt.savefig('Image à 9 antennes', dpi=600)

representation_antennes([a, b, c, d, e, f, g, h, i])

#donne la représentation avec ici des connections entre les sommets

def representation_antennes_2(l):
    fig, ax = plt.subplots()
    cercle = plt.Circle((0, 0), 2, color=(0.8, 0.8, 0.8))
    plt.xlim(- 2 - 0.3, 2 + 0.3)
    plt.ylim(- 2 - 0.3, 2 + 0.3)
    ax.set_aspect(1)
    ax.add_artist(cercle)
    for val in l:
        a = val.pos()
        c = val.name()
        plt.plot(a[0], a[1], c=val.couleurs(), marker='+', markersize=10)
        plt.text(a[0] - 0.1, a[1] - 0.3, c)
    for val in l:
        a = val.pos()
        voisin = val.voisins()
        for val2 in voisin:
            for val3 in l:
                if val3.name() == val2:
                    b = val3.pos()
                    plt.plot([a[0], b[0]], [a[1], b[1]], c='black')
    plt.plot([], [], label='3g' + '=' + 'noir', c='black', marker='+', markersize=10)
    plt.plot([], [], label='4g' + '=' + 'rouge', c='red', marker='+', markersize=10)
    plt.plot([], [], label='5g' + '=' + 'jaune', c='yellow', marker='+', markersize=10)
    plt.legend()
    plt.title("Exemple à 9 antennes")
    plt.savefig('Image à 9 antennes reliées', dpi=600)

representation_antennes_2([a, b, c, d, e, f, g, h, i])



