import turtle;import math
#les docstr sont faites avec l'extension autodocstr de python sur vsc

def trait(xdebut,ydebut,xfin,yfin):
    """_summary_

    Args:
        xdebut (int): coordonnée des abscisses de départ du trait
        ydebut (int): coordonnée des ordonnées de départ du trait
        xfin (int): abscisse de fin du trait
        yfin (int): ordonnée de fin du trait
    """
    crayon = turtle.Turtle()
    crayon.speed(0)
    crayon.shape("classic")
    crayon.shape("blank")
    crayon.penup()
    crayon.goto(xdebut,ydebut)
    crayon.pendown()
    crayon.goto(xfin,yfin)

def carre(cote,xhaut,yhaut):
    """_summary_

    Args:
        cote (int): longueur du coté
        xhaut (_type_): point de départ des abscisses, situé à gauche
        yhaut (_type_): point de départ des ordonnées, situé en haut du carré
    """
    Rectangle(xhaut,yhaut,cote,cote).dessine()


class Rectangle:
    def __init__(self,xdebut,ydebut,largeur,hauteur):
        self.xdebut = xdebut
        self.ydebut =ydebut
        self.largeur = largeur
        self.hauteur = hauteur

    def dessine(self):
        trait(self.xdebut, self.ydebut, self.xdebut +self.largeur, self.ydebut)                
        trait(self.xdebut +self.largeur, self.ydebut, self.xdebut+ self.largeur, self.ydebut -self.hauteur)  
        trait(self.xdebut +self.largeur, self.ydebut- self.hauteur, self.xdebut, self.ydebut- self.hauteur)  
        trait(self.xdebut, self.ydebut - self.hauteur, self.xdebut, self.ydebut)
        return self

    def colorier(self, couleur):
        turtle.penup()
        turtle.goto(self.xdebut, self.ydebut)
        turtle.pendown()
        turtle.fillcolor(couleur)
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.largeur)
            turtle.right(90)
            turtle.forward(self.hauteur)
            turtle.right(90)
        turtle.end_fill()




def nbfenetre(t, t_f, demarcation):
    if t_f <= 0:
        return 0  
    return math.floor((t + demarcation) / (t_f + demarcation))