"""Effectue plusieurs opérations liées à la génération et à l'analyse de
combinaisons d'actions financières à partir du fichier CSV
"""

# Import module
import sys
import time

import combinations as cb

# Récupère le troisième argument passé au script.
MAX_BUDGET = float(sys.argv[2])

filename = sys.argv[1]  # Récupère le deuxième argument passé au script.

start = time.time()

actions = cb.get_actions_from_csv(filename)  # Appelle de la fonction du module
nb_actions = len(actions)  # Calcule le nombre d'actions dans la liste obtenue.

# Appelle de la fonction du module pour afficher le nombre total d'actions.
cb.show_combinations_number(nb_actions)

combinations = []  # Crée une liste vide appelée combinaisons
cb.get_all_combinations(actions, combinations)  # Appelle de la fonction du
# module, avec la liste d'actions et la liste vide 'combinaisons' en tant
# qu'arguments pour générer toutes les combinaisons d'actions possibles.

combinations_in_budget = []  # Crée une liste vide pour stocker les
# combinaisons d'actions qui respectent le budget maximal.
cb.get_all_combinations_in_budget(combinations, combinations_in_budget,
                                  MAX_BUDGET)  # Appelle de la fonction du
# module, avec les combinaisons générées, la liste vide et le budget maximal
# en tant que arguments pour filtrer les combinaisons en fonction du budget.

cb.calculate_combinations_profit(combinations_in_budget)  # Appelle de la
# fonction du module, avec les combinaisons filtrées en tant qu'argument pour
# calculer le profit total de chaque combinaison.

combinations_in_budget.sort(key=lambda x: x[-1], reverse=True)  # Trie la
# liste combinaisons_in_budget en fonction du dernier élément de chaque
# combinaison (le profit) de manière décroissante.
cb.show_combination_details(combinations_in_budget[0])  # Affiche les détails
# de la prémière combianison de la liste triée 'combinaisons_in_budget'.

cb.execution_time(start)
