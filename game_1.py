import math
import random


def calculate_lcm(a, b, c):
    # Функция для вычисления НОК трех чисел
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    lcm_ab = lcm(a, b)
    return lcm(lcm_ab, c)


def generate_numbers():
    return sorted([random.randint(2, 20) for _ in range(3)])


def play_game():
    print("Welcome to the Brain Games!")
    print("May I have your name?")
    name = input()
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")
    count = 0
    while True:
        a, b, c = generate_numbers()
        correct_answer = calculate_lcm(a, b, c)

        print(f"\nQuestion: {a}, {b}, {c}")
        user_input = input("Your answer: ")

        try:
            answer = int(user_input)
            if answer == correct_answer:
                print("Correct!")
                count += 1
                if count == 3:
                    print(f"Congratulations, {name}!")
                    break

            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was: {correct_answer}.")
                print(f"Let's try again, {name}!")
        except ValueError:
            print("Please, enter the number")


if __name__ == "__main__":
    play_game()