import random


def generate_geometric_sequence():
    # Генерируем случайные параметры прогрессии
    start = random.randint(1, 5)
    ratio = random.choice([x for x in range(2, 5)] + [1 / 2, 1 / 3, 2 / 3])

    length = random.randint(5, 10)

    # Создаем прогрессию
    sequence = [round(start * (ratio ** i), 4) for i in range(length)]

    if all(num.is_integer() for num in sequence):
        sequence = [int(num) for num in sequence]

    return sequence, ratio


def play_game():
    print("Welcome to the brain games!")
    print("May I have your name?")
    name = input()
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    count = 0

    while True:
        sequence, ratio = generate_geometric_sequence()

        hidden_pos = random.randint(0, len(sequence) - 1)
        hidden_value = sequence[hidden_pos]

        displayed_sequence = sequence.copy()
        displayed_sequence[hidden_pos] = ".."

        # Выводим последовательность
        print("Question:", " ".join(map(str, displayed_sequence)))

        # Получаем ответ пользователя
        user_input = input("Your answer: ")

        try:
            answer = float(user_input)
            if abs(answer - hidden_value) < 0.0001:  # Учитываем возможные ошибки округления
                print("Correct!")
                count += 1

                if count == 3:
                    print(f"Congratulations, {name}!")
                    break
            else:
                print(f"'{user_input}' is wrong answer ;( correct answer was '{hidden_value}'.")
                print(f"Lets try again, {name}!")
        except ValueError:
            print("Please, enter the number")


if __name__ == "__main__":
    play_game()