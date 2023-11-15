print('Bonjour !')

print('Bonjour', input('Quel est votre nom ?'), '!')


def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)


print(factorielle(3))


def moyenne():
    a = int(input('Note 1 ?'))
    b = int(input('Note 2 ?'))
    c = int(input('Note 3 ?'))
    return (a+b+c)/3


print(moyenne())


def aire(b, h):
    return 'Aire du triangle : '+str((b*h)/2)


print(aire(int(input('Base ?')), int(input('Hauteur ?'))))


def exercice8():
    a = int(input('Nombre A ?'))
    b = int(input('Nombre B ?'))
    if a > b:
        print('VRAI')
        return True
    else:
        print('FAUX')
        return False


exercice8()
exercice8()


def is_triangle_rectangle(a, b, c):
    if (pow(a, 2) + pow(b, 2)) == pow(c, 2):
        print('TRIANGLE RECTANGLE')
        return True
    else:
        print('TRIANGLE PAS RECTANGLE')
        return False


def exercice9(a, b, c):
    if max(a, b, c) == c:
        return is_triangle_rectangle(a, b, c)
    elif max(a, b, c) == b:
        return is_triangle_rectangle(a, c, b)
    else:
        return is_triangle_rectangle(b, c, a)


exercice9(int(input('Côté A ?')), int(input('Côté B ?')), int(input('Côté C ?')))


def calcul(a, b):
    operation = input('Opération ? Parmi + - * / :')
    match operation:
        case '+':
            print(a+b)
            return a + b
        case '-':
            print(a - b)
            return a - b
        case '*':
            print(a * b)
            return a * b
        case '/':
            print(a / b)
            return a / b


calcul(int(input('Nombre 1 ?')), int(input('Nombre 2 ?')))
