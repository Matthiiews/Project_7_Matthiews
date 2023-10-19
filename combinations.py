"""Effectue des opérations liées à l'analyse de données
financières à partir du fichier CSV.
"""

# Import module
import csv
import math
import time


def execution_time(start):
    end = time.time()
    print(f"Temps: {end - start}")


def psdo_execution_time(start):
    end = time.time()
    return (end - start)


def get_actions_from_csv(filename):
    """
    Récupérer les actions dans une liste depuis le fichier csv
    lit le fichier CSV, extrait les actions (premier élément de chaque ligne),
    les coûts (deuxième élément de chaque ligne, en valeur absolue), et les
    bénéfices (troisième élément de chaque ligne) depuis le fichier CSV et les
    stocke dans une liste. Les actions ayant un coût égal à zéro sont ignorées.
    """
    actions = []
    with open(filename, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)

        actions = [[row[0], abs(float(row[1])), float(row[2])]
                   for row in reader if float(row[1]) != 0.0]
    return actions


def show_combinations_number(nb_actions):
    """
    Calculer le nombre de combinaisons possibles à partir d'un nombre
    donné d'actions en utilisant la formule mathématique des combinaiosons.
    """
    somme = 0
    for k in range(0, nb_actions):  # Itère sur tous les nombres de 0 a nb_act
        somme += math.factorial(nb_actions)/(math.factorial(k) *
                                             math.factorial(nb_actions-k))  #
    # Cette ligne effectue le calcul des combinaisons pour chaque valeur de k
    # et ajoute le résultat à la variable somme.
    print(f"Nombre d'actions : {nb_actions}")
    print(f"Nombre total de combinaisons possibles : {int(somme)}")


def get_combinations_of_k_elements(elements, k, combinations, start=0,
                                   combination=[]):
    """
    Récupérer toutes les combinaisons de k actions parmi la liste des actions
    """
    if len(combination) == k:  # vérifie si la longueur de la liste
        # combination est égale à k, Si oui, cela signifie que combination a
        # atteint la taille k désirée
        combinations.append(list(combination))  # en créant une copie de
        # combinaison afin d'éviter que les modifications ultérieures de
        # combination n'affectent la combinaison déjà ajoutée à combinations.
        return
    for i in range(start, len(elements)):  # Itère sur les indices i à partir
        # de la valeur actuelle de start jusqu'à la fin de la liste elements.
        combination.append(elements[i])
        get_combinations_of_k_elements(elements, k, combinations, i + 1,
                                       combination)
        combination.pop()  # Après l'appel récursif, l'élément ajouté à la
        # liste combination est retiré (pop()) pour explorer d'autres
        # combinaisons possibles. Ceci est essentiel pour maintenir l'état
        # correct de combination lors du retour des appels récursifs.


def get_all_combinations(actions, combinations):
    """
    Récupérer toutes les combinaisons possibles de k actions
    avec 1 <= k <= n, n étant le nombre total d'actions
    """
    for k in range(1, len(actions)+1):  # Itère sur les nombres de 1 à n, où n
        # est la longueur de la liste actions. À chaque itération,
        # k représente le nombre d'éléments dans chaque combinaison,
        # allant de 1 à la longueur totale de actions.
        get_combinations_of_k_elements(actions, k, combinations)  # génère
        # toutes les combinaisons de k éléments à partir de la liste actions
        # et ajoute ces combinaisons à la liste combinations.
    print(f"Nombre total trouvé: {len(combinations)}")  # imprime le nombre
    # total de combinaisons trouvées en utilisant la fonction
    # len(combinations). Cela donne le nombre total de combinaisons possibles
    # à partir des actions données.


def get_all_combinations_in_budget(combinations, combinations_in_budget,
                                   max_budget):
    """
    Récupérer parmi une liste de combinaisons
    les combinaisons où la somme totale des coûts des actions
    ne dépassant pas le budget max.
    """
    for combination in combinations:
        # print(f"combinaison: {combination}")
        cost = 0
        for action in combination:
            cost += action[1]
        if cost <= max_budget:
            combinations_in_budget.append(combination)

    print(f"Nombre total dans le budget : {len(combinations_in_budget)}")


def calculate_combinations_profit(combinations_in_budget):
    """
    Calculer le profit total de chaque combinaison.
    """
    for combination in combinations_in_budget:
        profit = 0
        for action in combination:
            profit += action[1] * action[2]/100
        combination.append(profit)


def show_combination_details(combination):
    """
    Afficher pour une combinaison:
    - la liste des actions
    - le coût total
    - le profit
    """
    total_cost = 0
    for action in combination[:-1]:  # itération sur chaque élément de la
        # combinaison, sauf le dernier élément
        print(f"{action[0]}, coût : {action[1]}")
        total_cost += action[1]  # a chaque itération, le coût de l'action
        # (action[1]) est ajouté à la variable total_cost
    print(f"Coût total : {total_cost}")
    print(f"Profit : {combination[-1]}")
