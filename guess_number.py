import numpy as np

first_number = 1  # Начальное число
last_number = 101  # Конечное число
average_value = int((last_number - first_number) / 2)  # Среднее значение интервала


def binary_search(number: int = 1) -> int:
    """Угадываем число с помощью алгоритма

        Args:
            number (int, optional): Загаданное число. Defaults to 1.

        Returns:
            int: Число попыток
        """
    left_board = first_number
    right_board = last_number
    current_value = average_value
    count = 1
    while current_value != number:
        count += 1
        if number > current_value:
            left_board = current_value
            current_value = int((left_board + right_board) / 2)
        else:
            right_board = current_value
            current_value = int((left_board + right_board) / 2)
    return count


def score_game() -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает алгоритм

        Args:
            binary_search ([type]): функция угадывания

        Returns:
            int: среднее количество попыток
        """
    count_ls = []
    random_array = np.random.randint(first_number, last_number, 1000)  # загадали список чисел
    for number in random_array:
        count_ls.append(binary_search(number))
    return int(np.mean(count_ls))


print(f"Алгоритм угадывает число в среднем за: {score_game()} попыток")
