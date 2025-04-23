import math
import random

class lcmgame:
    @staticmethod
    def calculate_lcm(a, b, c):
        def lcm(x, y):
            return x * y // math.gcd(x, y)

        lcm_ab = lcm(a, b)
        return lcm(lcm_ab, c)

    @staticmethod
    def generate_numbers():
        return sorted([random.randint(2, 20) for _ in range(3)])

    @staticmethod
    def play_game(name):
        print("Find the smallest common multiple of given numbers.")
        count = 0
        while True:
            a, b, c = lcmgame().generate_numbers()
            correct_answer = lcmgame().calculate_lcm(a, b, c)

            print(f"\nQuestion: {a}, {b}, {c}")
            user_input = input("Your answer: ")

            if user_input.lower() == "quit":
                print("Return to the games menu..")
                break

            try:
                answer = int(user_input)
                if answer == correct_answer:
                    print("Correct!")
                    count += 1
                    if count == 3:
                        print(f"Congratulations, {name}!\n")
                        break

                else:
                    print(f"'{answer}' is wrong answer ;(. Correct answer was: {correct_answer}.")
                    print(f"Let's try again, {name}!")
            except ValueError:
                print("Please, enter the number")
