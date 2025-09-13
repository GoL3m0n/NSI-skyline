import formes;import esthetique;import random;import turtle

class building:
    def __init__(self,largeur,hauteur,couleur,x,y,typeb):  #couleur est un dict 
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.x = x #coin supérieur gauche
        self.y = y
        self.typeb = typeb
     
    
    def dessine_mur_porteurs(self):
        formes.Rectangle(self.x,self.y,self.largeur,self.hauteur).dessine().colorier(self.couleur[self.typeb])
        return self

    def creation_fenetre(self):
        esthetique.Fenetres(self.largeur,self.hauteur,self.x,self.y,self.couleur["fenetres"]).dessinef()
        return self

    def ajout_toit(self):
        typetoit = random.randint(1,3)
        if typetoit == 1:
            esthetique.toit1(self.largeur,self.x,self.y,self.couleur["toits"]).dessine().colorie()
        elif typetoit==2:
            esthetique.toit2(self.x,self.y,self.largeur,self.couleur["toits"]).dessine()
        elif typetoit==3:
            esthetique.toit3(self.x,self.y,self.hauteur,self.largeur,self.couleur["toits"]).dessine().colorie()
        return self

def main():
    countlen = 0
    x= -500
    n= random.randint(6,9)
    na = n //2
    nb = n-na
    coef = 1
    couleurs = esthetique.choix_couleur()
    largeur = random.randint(100,125)
    hauteur = random.randint(200,225)
    y = hauteur - 200
    building(largeur,hauteur,couleurs,x,y,"building").dessine_mur_porteurs().creation_fenetre().ajout_toit()
    x +=largeur
    coef += 0.1
    for i in range(na): #on crée les tours de derriere, il faudra voir combien on en met
        couleurs = esthetique.choix_couleur()
        largeur = random.randint(100,125)
        hauteur = hauteur * coef
        y = hauteur - 200
        building(largeur,hauteur,couleurs,x,y,"building").dessine_mur_porteurs().creation_fenetre().ajout_toit()
        x+=largeur
        countlen+=largeur
        coef += 0.01

    for i in range(nb+2): #on crée les tours de derriere, il faudra voir combien on en met
        couleurs = esthetique.choix_couleur()
        largeur = random.randint(100,125)
        hauteur = hauteur * coef
        y = hauteur - 200
        building(largeur,hauteur,couleurs,x,y,"building").dessine_mur_porteurs().creation_fenetre().ajout_toit()
        x+=largeur
        countlen+=largeur
        coef -= 0.1



    
    n2 = random.randint(9,11)
    x = -400
    for i in range(n2):
        couleurs = esthetique.choix_couleur()
        largeur = random.randint(60,75)
        hauteur = random.randint(125,150) #changer les valeurs
        y= hauteur - 200
        building(largeur,hauteur,couleurs,x,y,"bureaux").dessine_mur_porteurs().creation_fenetre().ajout_toit()
        x+=largeur
 



    n3 = random.randint(12,16)
    x = -350
    for i in range(n3):
        couleurs = esthetique.choix_couleur()
        largeur = random.randint(40,50)
        hauteur = random.randint(75,90) #changer les valeurs
        y = hauteur -200
        building(largeur,hauteur,couleurs,x,y,"habitation").dessine_mur_porteurs().creation_fenetre().ajout_toit()
        x+=largeur
        
    formes.Rectangle(-600,0,countlen,50).dessine().colorier("white")
    turtle.done()
