"""résout le problème d'optimisation lié à l'investissement dans des actions.
Le programme cherche à trouver la combinaison la plus rentable d'actions à
acheter en fonction d'un budget maximal.
"""

# Import Module
from tqdm import tqdm
from itertools import combinations
import csv
import time
import sys

# Constants
MAX_INVEST_DEFAULT = 500
CSV_FILENAME = "data/test_shares.csv"


def main():
    start_time = time.time()
    MAX_INVEST = get_max_investment()
    shares_list = read_csv(CSV_FILENAME)
    print(f"\nProcessing {len(shares_list)} shares for {MAX_INVEST}€ :")
    best_combo = find_best_combo(shares_list, MAX_INVEST)
    display_results(best_combo, start_time)


def get_max_investment():
    """Obtenir l'investissement en numéraire personnalisé à partir des
    arguments de la ligne de commande,
    Valeur par défaut de MAX_INVEST_DEFAULT si elle n'est pas fournie.
    """
    try:
        return float(sys.argv[1])
    except (IndexError, ValueError):
        return MAX_INVEST_DEFAULT


def read_csv(filename):
    """Importer des données sur les actions à partir d'un fichier CSV."""
    shares_list = []
    with open(filename) as csvfile:
        shares_file = csv.reader(csvfile, delimiter=',')
        for row in shares_file:
            shares_list.append((row[0], float(row[1]), float(row[2])))
    return shares_list


def find_best_combo(shares_list, max_investment):
    """Trouver la combinaison d'actions la plus rentable."""
    profit = 0
    best_combo = []
    for i in tqdm(range(len(shares_list))):
        combos = combinations(shares_list, i + 1)
        for combo in combos:
            total_cost = sum(share[1] for share in combo)
            if total_cost <= max_investment:
                total_profit = sum(share[1] * share[2] / 100 for share in
                                   combo)
                if total_profit > profit:
                    profit = total_profit
                    best_combo = combo
    return best_combo


def display_results(best_combo, start_time):
    """Afficher les résultats de la meilleure combinaison."""
    print(f"\nInvestissement le plus rentable ({len(best_combo)} Actions) :\n")
    for item in best_combo:
        print(f"{item[0]} | {item[1]} € | +{item[2]} %")
    total_cost = sum(share[1] for share in best_combo)
    total_profit = sum(share[1] * share[2] / 100 for share in best_combo)
    print("\nTotal cost : ", total_cost, "€")
    print("Profit after 2 years : +", total_profit, "€")
    print("\nTime elapsed : ", time.time() - start_time, "seconds")


if __name__ == "__main__":
    main()
