import re


def nb_chiffres_du_carre(n):
    return len(str(pow(n, 2)))


print(nb_chiffres_du_carre(100))


def est_premier(n):
    for i in range(2, n - 1):
        if (n % i) == 0:
            return False
    return True


print(est_premier(7))
print(est_premier(8))


def nombres_premiers(n, nombres):
    if n == 2:
        nombres.insert(0, n)
        return nombres
    elif est_premier(n):
        nombres.insert(0, n)
        return nombres_premiers(n - 1, nombres)
    else:
        return nombres_premiers(n - 1, nombres)


print(nombres_premiers(10, []))


class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __eq__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return self.jour == other.jour and self.mois == other.mois and self.annee == other.annee

    def __lt__(self, other):
        if self.annee > other.annee:
            return True
        elif self.annee == other.annee:
            if self.mois > other.mois:
                return True
            elif self.mois == other.mois:
                return self.jour > other.jour
        return False

    def set_jour(self, jour):
        self.jour = jour

    def set_mois(self, mois):
        self.mois = mois

    def set_annee(self, annee):
        self.annee = annee

    def afficher_date(self):
        return str(self.jour) + '/' + str(self.mois) + '/' + str(self.annee)


def creation_date():
    d = Date()
    annee = int(input('Saisissez une année : '))
    while annee < 0:
        annee = int(input('Saisissez une année, celle-ci ne peut être négative : '))
    d.set_annee(annee)
    mois = int(input('Saisissez un mois, compris entre 1 et 12 : '))
    while mois < 1 or mois > 12:
        mois = int(input('Saisissez un mois, compris entre 1 et 12 : '))
    d.set_mois(mois)
    jour = int(input('Saisissez un jour, compris entre 1 et 31 : '))
    while jour < 1 or jour > 31:
        jour = int(input('Saisissez un mois, compris entre 1 et 31 : '))
    d.set_jour(jour)
    return d


# date = creation_date()
# print(date.afficher_date())


class Personne:
    def __init__(self, nom, prenom, date_naissance, date_embauche):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.date_embauche = date_embauche

    def afficher_personne(self):
        return self.prenom + " " + self.nom + " est née le " + self.date_naissance.afficher_date() + " et embauché le " + self.date_embauche.afficher_date()


def creation_personne():
    regex = "^([a-zA-Z]|[à-ü]|[À-Ü])+$"
    nom = input("Entrez un nom : ")
    while not re.match(regex, nom):
        nom = input("Entrez un nom : ")
    prenom = input("Entrez un prenom : ")
    while not re.match(regex, prenom):
        prenom = input("Entrez un prenom : ")
    print("Choisissez une année de naissance : ")
    date_naissance = creation_date()
    print("Choisissez une année d'embauche : ")
    date_embauche = creation_date()
    return Personne(nom, prenom, date_naissance, date_embauche)


# personne = creation_personne()
# print(personne.afficher_personne())


def est_plus_recente_que(date1, date2):
    if date1.__eq__(date2):
        return False
    return date1.__lt__(date2)


# print('est_plus_recente_que(date1, date2) = ')
# date1 = Date()
# date1.set_jour(2)
# date1.set_mois(1)
# date1.set_annee(1970)
# date2 = Date()
# date2.set_jour(1)
# date2.set_mois(1)
# date2.set_annee(1970)
# print(est_plus_recente_que(date1, date2))

def anciennete(personne1, personne2):
    bool = est_plus_recente_que(personne1.date_embauche, personne2.date_embauche)
    if bool:
        return personne1.afficher_personne() + " n'a pas plus d'expérience que " + personne2.afficher_personne()
    else:
        return personne2.afficher_personne() + " n'a pas plus d'expérience que " + personne1.afficher_personne()


personne1 = Personne("Benzema", "Karim", Date(19, 12, 1987), Date(18, 11, 2020))
personne2 = Personne("Belaili", "Youcef", Date(14, 3, 1992), Date(26, 10, 2017))
print(anciennete(personne1, personne2))
