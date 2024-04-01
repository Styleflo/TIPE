class antennes:
    """definition d'une antenne du reseau"""
    def __init__(self, nom, type, x, y, voisins, capacite):
        self.n = nom
        self.t = type
        self.x = x
        self.y = y
        self.v = voisins
        self.c = capacite

    "donne la position de l'antenne"
    def pos(self):
        return (self.x, self.y)

    "donne le type de l'antenne"
    def type(self):
        return self.t

    def name(self):
        return self.n

    def voisins(self):
        return self.v

    def couleurs(self):
        if self.t == '3g':
            return 'black'
        if self.t == '4g':
            return 'red'
        if self.t == '5g':
            return 'yellow'

    "capactité en fonction des types d'antennes"
    def capacite_max(self):
        if self.t == '3g':
            return 100
        if self.t == '4g':
            return 1000
        if self.t == '5g':
            return 10000



