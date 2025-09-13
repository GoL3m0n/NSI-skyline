import random;import formes;import turtle



def choix_couleur():
    return{
    "fenetres" : ["#80C4FF","#4A90E2","#A7C7E7"],
    "toits" : ["#2C2C2C","#1B263B","#0D1B2A","#3E4C59","#C45435","#D0FFFF","#BD6A4C"],
    "building" : random.choice(["#D5CBB7","#E5E5E5","#FAE2FF","#FFF0B3"]),
    "bureaux" : random.choice(["#D8D2C2","#DFF1C7","#5DA9C5","#CAA9B0"]),
    "habitation" : random.choice(["#8B3A3A","#F5E6D3","#A0522D","#A3B18A"])}

  

class Fenetres:
    def __init__(self,largeurbd,hauteurbd,x,y,couleurs):
        self.hauteurbd=hauteurbd
        self.largeurbd=largeurbd
        self.x=x
        self.y=y
        self.typefenetres= random.randint(1,3)
        self.couleurs = couleurs #c'est juste la case du dictionnaire "fenetre"

    def dessinef(self):
        couleur = random.choice(self.couleurs)
        if self.typefenetres == 1:
            couleur1 = "#FFD166"
            couleur2 = random.choice(self.couleurs) 
            if couleur1 == couleur2:
                couleur1 = random.choice(self.couleurs) 
            self.fenetre_barres(couleur1,couleur2)
            print("barres")
        elif self.typefenetres==2:
            self.baies_vitrees(couleur)
            print("baies vitrees")
        elif self.typefenetres == 3:
            self.myriade_fenetres(couleur)
            print("myriade fenetres")
        return self

    def fenetre_barres(self,couleur_barres,couleur_fenetres):
        ecart_barres = self.largeurbd/3
        largeur_barre = self.largeurbd/5
        largeur_f = self.largeurbd/5
        hauteur_f = largeur_f *1.5
        demarcation = hauteur_f/5
        formes.Rectangle(self.x+ecart_barres-(largeur_barre)/2,self.y,largeur_barre,self.hauteurbd).dessine().colorier(couleur_barres)
        formes.Rectangle(self.x+2*ecart_barres-(largeur_barre)/2,self.y,largeur_barre,self.hauteurbd).dessine().colorier(couleur_barres)
        nbfens = formes.nbfenetre(self.hauteurbd,hauteur_f,demarcation)
        x_f = self.x+self.largeurbd/2-largeur_f/2
        y_f = self.y-demarcation
        for i in range(nbfens):
            formes.Rectangle(x_f,y_f,largeur_f,hauteur_f).dessine().colorier(couleur_fenetres)
            y_f -= hauteur_f + demarcation

    def baies_vitrees(self,couleur_baie):
        h = self.hauteurbd/7
        l = self.largeurbd * 2/3
        demarc = 0.1 * h
        nbfen = formes.nbfenetre(self.hauteurbd,h,demarc)
        y= self.y-demarc 
        for i in range(nbfen):
            formes.Rectangle(self.x+(self.largeurbd-l)/2,y,l,h).dessine().colorier(couleur_baie)
            y-= h+demarc

    def myriade_fenetres(self,couleur_fenetres):
        div = random.choice([8,10])
        print("nb div:",div)
        l = self.largeurbd/div
        demarc_hor = l*0.25
        h = l * 1.4
        demarc_vert = h * 0.15
        nbcol = formes.nbfenetre(self.hauteurbd,h,demarc_vert)
        nblig = formes.nbfenetre(self.largeurbd,l,demarc_hor)
        y = self.y-demarc_vert
        for i in range(nbcol):
            x = self.x + demarc_hor
            for j in range(nblig):
                formes.Rectangle(x,y,l,h).dessine().colorier(couleur_fenetres)
                x+= l + demarc_hor
            y-=h+demarc_vert


    

class toit1:
    def __init__(self, largeur, x, y, couleurs):
        self.largeur = largeur
        self.x, self.y = x, y
        self.couleurs = couleurs  # liste de couleurs
        choix_h = [self.largeur/4, self.largeur/3, self.largeur/6, self.largeur/2]
        self.hauteur = random.choice(choix_h)

    def dessine(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.goto(self.x + self.largeur, self.y)
        turtle.goto(self.x + self.largeur/2, self.y + self.hauteur)
        turtle.goto(self.x, self.y)
        return self

    def colorie(self):
        couleur = random.choice(self.couleurs)
        turtle.fillcolor(couleur)

        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

        turtle.begin_fill()
        turtle.goto(self.x + self.largeur, self.y)
        turtle.goto(self.x + self.largeur/2, self.y + self.hauteur)
        turtle.goto(self.x, self.y)
        turtle.end_fill()
        return self

class toit2:
    def __init__(self,x,y,largeur,couleur):
        self.x,self.y = x,y
        self.largeur = largeur
        self.couleur = couleur

    def dessine(self):
        couleur = random.choice(self.couleur)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.fillcolor(couleur)
        turtle.begin_fill()
        turtle.setheading(90)
        turtle.circle(-self.largeur/2, 180)  # demi-cercle vers le bas
        turtle.setheading(0)
        turtle.end_fill()
        return self

class toit3:
    def __init__(self, x, y, hauteurbd, largeur, couleurs):
        self.x, self.y = x, y
        self.hauteurbd = hauteurbd
        self.hauteur = hauteurbd / 4  # proportion du toit
        self.largeur = largeur
        self.couleurs = couleurs

    def dessine(self):
        nombre_marches = 4
        largeur_marche = self.largeur / (nombre_marches * 2)
        hauteur_marche = self.hauteur / nombre_marches
        x, y = self.x, self.y

        # on monte à gauche
        for i in range(nombre_marches):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.goto(x + largeur_marche, y)
            x += largeur_marche
            turtle.goto(x, y + hauteur_marche)
            y += hauteur_marche

        # on descend à droite
        for i in range(nombre_marches):
            turtle.goto(x, y - hauteur_marche)
            y -= hauteur_marche
            turtle.goto(x + largeur_marche, y)
            x += largeur_marche

        # fermer le contour
        turtle.goto(self.x, self.y)
        return self

    def colorie(self):
        couleur = random.choice(self.couleurs)
        turtle.fillcolor(couleur)
        turtle.begin_fill()
        self.dessine() 
        turtle.end_fill()
        return self
