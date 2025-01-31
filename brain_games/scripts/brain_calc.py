# file: scripts/brain_calc.py

# import module to start the game
from brain_games.games import logic_calc

# import function from my_functions.py
from brain_games.games.my_functions import game
# ----------------------------------------------


def main():
    game(logic_calc)


if __name__ == "__main__":
    main()
