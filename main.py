from games.game_1 import lcmgame
from games.game_2 import geometric


def show_menu():
    print("Menu:")
    print("1. LCM Game (Least Common Multiple)")
    print("2. Geometric Progression Game")
    print("3. Exit")


def main():
    print("Welcome to the Math Games Collection!")
    print("May I have your name?")
    name = input()
    print(f"Hello, {name}!")

    while True:
        show_menu()
        choice = input("\nSelect a game (1-3): ")

        if choice == '1':
            lcmgame.play_game(name)
        elif choice == '2':
            geometric.play_game(name)
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()