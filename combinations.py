"""Effectue des opérations liées à l'analyse de données
financières à partir du fichier CSV.
"""

# Import module
import csv
import math
import time


def execution_time(start_time):
    end_time = time.time()
    print(f"Temps: {end_time - start_time}")


def get_actions_from_csv(filename):
    """
    Récupérer les actions dans une liste depuis le fichier csv
    """
    actions = []
    with open(filename, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)

        for row in reader:
            row[1] = float(row[1])
            if row[1] != 0:
                if row[1] < 0:
                    row[1] = -row[1]
                row[2] = float(row[2])
                actions.append(row)
    return actions


def show_combinations_number(nb_actions):
    """
    Calculer le nombre de combinaisons possibles à partir d'un nombre d'actions
    """
    somme = 0
    for k in range(0, nb_actions):
        somme += math.factorial(nb_actions)/(math.factorial(k) *
                                             math.factorial(nb_actions-k))
    print(f"Nombre d'actions : {nb_actions}")
    print(f"Nombre total de combinaisons possibles : {int(somme)}")


def get_combinations_of_k_elements(elements, k, combinations, start=0,
                                   combination=[]):
    """
    Récupérer toutes les combinaisons de k actions parmi la liste des actions
    """
    if len(combination) == k:
        combinations.append(list(combination))
        return
    for i in range(start, len(elements)):
        combination.append(elements[i])
        get_combinations_of_k_elements(elements, k, combinations, i + 1,
                                       combination)
        combination.pop()


def get_all_combinations(actions, combinations):
    """
    Récupérer toutes les combinaisons possibles de k actions
    avec 1 <= k <= n, n étant le nombre total d'actions
    """
    for k in range(1, len(actions)+1):
        get_combinations_of_k_elements(actions, k, combinations)
    print(f"Nombre total trouvé: {len(combinations)}")


def get_all_combinations_in_budget(combinations, combinations_in_budget,
                                   max_budget):
    """
    Récupérer parmi une liste de combinaisons
    les combinaisons où la somme totale des coûts des actions
    ne dépasse pas le budget max.
    """
    for combination in combinations:
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
    for action in combination[:-1]:
        print(f"{action[0]}, coût : {action[1]}")
        total_cost += action[1]
    print(f"Coût total : {total_cost}")
    print(f"Profit : {combination[-1]}")
