"""résout le problème d'optimisation pour maximiser le profit d'un
investissement dans des actions financières tout en respectant une contrainte
budgétaire.
"""

# Import module
from tqdm import tqdm
import csv
import time
import sys


def read_csv(filename):
    """Importation de données sur les actions à partir d'un fichier csv
    Filtrer les données corrompues

    @return: données sur les actions (liste)
    """
    try:
        with open(filename) as csvfile:
            shares_file = csv.reader(csvfile, delimiter=',')
            if filename != "data/test_shares.csv":
                next(csvfile)  # skip first row in both datasets
            shares_list = []
            for row in shares_file:
                if float(row[1]) > 0 and float(row[2]) > 0:
                    share = (row[0], int(float(row[1]) * 100),
                             float(float(row[1]) * float(row[2]) / 100))
                    shares_list.append(share)
            return shares_list

    except FileNotFoundError:
        print(f"\nFile '{filename}' does not exist. Please try again.\n")
        time.sleep(1)
        sys.exit()


def knapsack(shares_list):
    """Initialiser la matrice (ks) pour le problème knapsack 0-1
    Obtenir la meilleure combinaison d'actions

    @param shares_list: données relatives aux actions (liste)
    @return: meilleure combinaison possible (liste)
    """
    max_inv = int(MAX_INVEST * 100)     # capacity
    shares_total = len(shares_list)
    cost = [share[1] for share in shares_list]       # weights
    profit = [share[2] for share in shares_list]     # values

    # Trouver le profit optimal
    ks = [[0 for x in range(max_inv + 1)] for _ in range(shares_total + 1)]
    for i in tqdm(range(1, shares_total + 1)):
        for w in range(1, max_inv + 1):
            if cost[i-1] <= w:
                ks[i][w] = max(profit[i-1] + ks[i-1][w-cost[i-1]], ks[i-1][w])
            else:
                ks[i][w] = ks[i-1][w]

    # Recherche d'une combinaison d'actions à partir d'un profit optimal
    best_combo = []

    while max_inv >= 0 and shares_total >= 0:

        if ks[shares_total][max_inv] == \
            ks[shares_total-1][max_inv - cost[shares_total-1]] \
                + profit[shares_total-1]:

            best_combo.append(shares_list[shares_total-1])
            max_inv -= cost[shares_total-1]

        shares_total -= 1
    return best_combo


def display_results(best_combo):
    """Afficher les résultats de la meilleure combinaison

    @param best_combo: combinaison d'actions la plus rentable (liste)
    """
    print(f"\nInvestissement le plus rentable ({len(best_combo)} Actions) :\n")
    cost = []
    profit = []
    for item in best_combo:
        print(f"{item[0]} | {item[1] / 100} € | +{item[2]} €")
        cost.append(item[1] / 100)
        profit.append(item[2])
    print("\nTotal cost : ", sum(cost), "€")
    print("Profit after 2 years : +", sum(profit), "€")
    print("\nTime elapsed : ", time.time() - start_time, "seconds\n")


def main():
    """Vérification de l'entrée du nom de fichier"""
    try:
        filename = "data/" + sys.argv[1] + ".csv"
    except IndexError:
        print("\nNo filename found. Please try again.\n")
        time.sleep(1)
        sys.exit()

    shares_list = read_csv(filename)

    print(f"\nProcessing '{sys.argv[1]}'({len(shares_list)} valid shares) \
            for {MAX_INVEST} € :")

    display_results(knapsack(shares_list))


if __name__ == "__main__":
    start_time = time.time()
    # Vérification de l'investissement personnalisé en numéraire(default = 500)
    try:
        MAX_INVEST = float(sys.argv[2])
    except IndexError:
        MAX_INVEST = 500
    main()
