"""résout le problème d'optimisation pour maximiser le profit d'un
investissement dans des actions financières tout en respectant une contrainte
budgétaire.
"""

# Import module
import csv
import sys
import time
import tracemalloc
import combinations as cb

tracemalloc.start()

MAX_BUDGET = float(sys.argv[2])

filename = sys.argv[1]

start = time.time()


with open(filename, newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)

    actions = [[row[0], abs(float(row[1])), float(row[2])] for row in reader
               if (float(row[1]) != 0.0 and float(row[1]) > 0)]

nb_actions = len(actions)

print(f"Getting actions from file is completed in : \
      {cb.psdo_execution_time(start)}")


for action in actions:
    action.append(round(action[1]*action[2]/100, 2))


print(f"Appending to each action completed in : \
      {cb.psdo_execution_time(start)} ms")

# Trier par le profit
actions.sort(key=lambda x: x[2], reverse=True)

print(f"Sorting actions by profit completed in : \
      {cb.psdo_execution_time(start)} ms")

i = 0
total_cost = 0
total_profit = 0
selected_actions = []

while total_cost <= MAX_BUDGET and i <= nb_actions-1:
    if total_cost + actions[i][1] <= MAX_BUDGET:
        total_cost += actions[i][1]
        total_profit += actions[i][3]
        selected_actions.append(actions[i])
    i += 1
print(f"Getting all actions in budget completed in : \
      {cb.psdo_execution_time(start)} ms")

print(f"Nombre d'actions au total : {nb_actions}")
print(f"Nombre d'actions sélectionnées au total : {len(selected_actions)}")


for selected_action in selected_actions:
    print(f"{selected_action[0]:<15} {selected_action[1]:>7} \
          {selected_action[2]:>7} {selected_action[3]:>7}")

print(f"Out putting actions completed in : {cb.psdo_execution_time(start)} ms")

print(f"Coût total : {total_cost:.2f}")

print(f"Profit total : {total_profit:.2f}")

print(f"Completing full exécution in : {cb.psdo_execution_time(start)} ms")

second_size, second_peak = tracemalloc.get_traced_memory()

print(f"Total mmemory size used :{second_size/1024} KiB")

tracemalloc.stop()
