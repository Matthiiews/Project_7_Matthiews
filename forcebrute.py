"""Effectue plusieurs opérations liées à la génération et à l'analyse de
combinaisons d'actions financières à partir du fichier CSV
"""

# Import module
import sys
import time

import combinations as cb

MAX_BUDGET = float(sys.argv[2])

filename = sys.argv[1]

start = time.time()

actions = cb.get_actions_from_csv(filename)
nb_actions = len(actions)

cb.show_combinations_number(nb_actions)

combinations = []
cb.get_all_combinations(actions, combinations)

combinations_in_budget = []
cb.get_all_combinations_in_budget(combinations, combinations_in_budget,
                                  MAX_BUDGET)

cb.calculate_combinations_profit(combinations_in_budget)

combinations_in_budget.sort(key=lambda x: x[-1], reverse=True)
cb.show_combination_details(combinations_in_budget[0])

cb.execution_time(start)
