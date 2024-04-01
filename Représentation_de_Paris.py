import random as rd
import Classes as c
import matplotlib.pyplot as plt

classes = ['3g', '3g', '4g', '4g', '4g', '5g']
epsilon = [-1, 1]

def pos_alea(r):
    x = epsilon[rd.randrange(0, 2)] * r * rd.random()
    y = epsilon[rd.randrange(0, 2)] * r * rd.random()
    d = r**2
    while x**2 + y**2 > d:
        x = epsilon[rd.randrange(0, 2)] * r * rd.random()
        y = epsilon[rd.randrange(0, 2)] * r * rd.random()
    return x, y

def construction_antennes(n,r):
    l = []
    for i in range(n-1):
        a = classes[rd.randrange(0, 6)]
        b = pos_alea(r)
        l.append(c.antennes(i, a, b[0], b[1], [], 0))
    return l

def Paris(r,n):
    fig, ax = plt.subplots()
    cercle = plt.Circle((0, 0), r, color=(0.2, 0.5, 0.7))
    plt.xlim(- r - r/10, r + r/10)
    plt.ylim(- r - r/10, r + r/10)
    ax.set_aspect(1)
    ax.add_artist(cercle)
    plt.title("Représentation de Paris")
    antennes = construction_antennes(n+1, r)
    for car in antennes:
        position = car.pos()
        plt.plot([position[0]], [position[1]], c=car.couleurs(), marker='+', markersize=10)
    plt.plot([], [], label='3g' + '=' + 'noir', c='black', marker='+', markersize=10)
    plt.plot([], [], label='4g' + '=' + 'rouge', c='red', marker='+', markersize=10)
    plt.plot([], [], label='5g' + '=' + 'jaune', c='yellow', marker='+', markersize=10)
    plt.legend()
    plt.savefig('Image antennes de Paris', dpi=600)

print(Paris(10, 500))

