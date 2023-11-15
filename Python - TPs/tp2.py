list = [1990, 1996, 1994, 1997, 1993, 2001, 1999, 2000]
list.remove(min(list))
print(min(list))

maroc = {"president": "Mohammed VI", "capitale": "Rabat", "superficie": 710850}
algerie = {"president": "Abdelaziz Bouteflika", "capitale": "Alger", "superficie": 2382000}
tunisie = {"president": "Kaïs Saïed", "capitale": "Tunis", "superficie": 163610}

algerie["president"] = "Abdelmadjid Tebboune"
pays = {"maroc": maroc, "algerie": algerie, "tunisie": tunisie}
for p in pays:
    print(p+' = '+str(pays[p]))
print(pays)

etudiants = {
    "etudiant_1": 13,
    "etudiant_2": 17,
    "etudiant_3": 9,
    "etudiant_4": 15,
    "etudiant_5": 8,
    "etudiant_6": 14,
    "etudiant_7": 14,
    "etudiant_8": 12,
    "etudiant_9": 13,
    "etudiant_10": 15,
    "etudiant_11": 14,
    "etudiant_12": 9,
    "etudiant_13": 12,
    "etudiant_14": 12,
    "etudiant_15": 13,
    "etudiant_16": 7,
    "etudiant_17": 12,
    "etudiant_18": 15,
    "etudiant_19": 9,
    "etudiant_20": 17
}


def exercice3(etudiants):
    etudiants['etudiant_21'] = 18
    etudiantAdmis = {}
    etudiantNonAdmis = {}
    for nom in etudiants:
        print(etudiants[nom])
        if etudiants[nom] >= 10:
            etudiantAdmis[nom] = etudiants[nom]
        else:
            etudiantNonAdmis[nom] = etudiants[nom]
    etudiants = {}
    etudiants['Admis'] = etudiantAdmis
    etudiants['non admis'] = etudiantNonAdmis
    return etudiants


print(exercice3(etudiants))

d = {
    "Adam": [12, 15, 17],
    "Karim": [15, 12, 16],
    "Joshua": [13, 15, 7]
}


def moyenne3(a, b, c):
    return (a+b+c)/3


for name in d:
    d[name] = round(moyenne3(d[name][0], d[name][1], d[name][2]), 2)

print(d)


def factorielle(n):
    if n == 1:
        return 1
    else:
        return n * factorielle(n-1)


print(factorielle(4))


def moyenne():
    notes = []
    sum = 0
    x = int(input('Nombre de notes ?'))
    for i in range(x):
        notes.append(int(input('Note #'+str(i+1)+' ?')))
    for note in notes:
        sum += note
    return sum / x


# print(moyenne())

def exercice7():
    n = int(input('n ? '))
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()


exercice7()
