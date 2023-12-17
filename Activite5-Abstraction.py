from abc import ABC, abstractmethod

class Composition:
    def __init__(self, produit, quantite):
        self.__produit = produit
        self.__quantite = quantite

    @property
    def produit(self):
        return self.__produit

    @property
    def quantite(self):
        return self.__quantite


class Produit(ABC):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def nom(self):
        return self.__nom

    @property
    def code(self):
        return self.__code

    @abstractmethod
    def getPrixHT(self):
        pass

    def equals(self, other) :
        return self.__code == other.__code

class ProduitElementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    def __str__(self):
        return f"Produit élémentaire {self.nom} (Code: {self.code}), Prix d'achat: {self.__prixAchat}"

    def getPrixHT(self):
        return self.__prixAchat
    
    def equals(self, other) :
        return self.__code == other.__code


class ProduitCompose(Produit):
    tauxTVA = 0.18

    def __init__(self, nom, code, fraisFabrication, listeConstituants):
        super().__init__(nom, code)
        self.__fraisFabrication = fraisFabrication
        self.__listeConstituants = listeConstituants 

    @property
    def fraisFabrication(self):
        return self.__fraisFabrication

    @property
    def listeConstituants(self):
        return self.__listeConstituants

    def __str__(self):
        return f"Produit composé {self.nom} (Code: {self.code}), Frais de fabrication: {self.__fraisFabrication}"
    
    def equals(self, other) :
        return self.__code == other.__code

    def getPrixHT(self):
        prix_ht_total = sum(each.produit.getPrixHT() * each.quantite for each in self.__listeConstituants)
        return prix_ht_total + self.__fraisFabrication


