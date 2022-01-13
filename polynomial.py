from math import sqrt
import matplotlib.pyplot as plt  # type:ignore



class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.a = coeffs[0]
        self.b = coeffs[1]
        self.c = coeffs[2]

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        e = self.a + other.a
        f = self.b + other.b
        g = self.c + other.c
        
        return  f"{e}X^2 + {f}X + {g}" 

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        h = self.a - other.a
        k = self.b - other.b
        l = self.c - other.c
        return f"{h}X^2 + {k}X + {l}"

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        return f"{self.a}X^2 + {self.b}X + {self.c}" 

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        delta = self.b**2 - 4*self.a*self.c
        if delta < 0:
            return "L'equation n'admet aucune solution reel"
        elif delta == 0:
            x0 = -self.b/(2*self.a)
            return f"L'equation admt une solution unique x0 = {x0}"
        else:
            x1 = (-self.b - sqrt(delta))/(2*self.a)
            x2 = (-self.b + sqrt(delta))/(2*self.a)
            return f"L'equation admet deux solutions reels x1 = {x1} et x2 = {x2}"

    def __va1(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        y = self.a*(self.x**2) + self.b*self.x + self.c
        return y

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        import numpy as np
        x = np.linspace(0, 18, 20)
        y = self.a*(x**2) + self.b*x + self.c
        fig = plt.figure(figsize = (10, 5))
        plt.plot(x, y, "gx")
        plt.xlabel('Abscisses')
        plt.ylabel('Ordonées')
        plt.title(f"{self.a}X^2 + {self.b}X + {self.c}")
        plt.show()


if __name__ == "__main__":
    bar = (1, 1, 1)
    p1 = Poly2(*bar)

    baz = (1, 1, 1)
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2
   

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png