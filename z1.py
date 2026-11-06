import numpy as np


def MakeIntMatr(n, low, high):
    """Создает целочисленную матрицу NxN в диапазоне [low, high]"""
    # randint не включает верхнюю границу, поэтому +1
    return np.random.randint(low, high + 1, size=(n, n))


def SumPositiveCols(Matr):
    """1. Сумма элементов в столбцах без отрицательных чисел"""
    n = Matr.shape[0]
    total_sum = 0

    for j in range(n):  # Проход по столбцам
        # all() вернет True, если ВСЕ элементы столбца >= 0
        if all(Matr[i][j] >= 0 for i in range(n)):
            col_sum = sum(Matr[i][j] for i in range(n))
            total_sum += col_sum
            print(f"Столбец {j + 1} подходит. Сумма: {col_sum}")

    return total_sum


def MinAntiDiagSum(Matr):
    """2. Минимум среди сумм модулей диагоналей, параллельных побочной"""
    n = Matr.shape[0]
    min_val = float('inf')  # Бесконечность для поиска минимума

    # k - смещение относительно побочной диагонали (от -(n-1) до n-1)
    for k in range(-(n - 1), n):
        diag_sum = 0
        for i in range(n):
            j = n - 1 - i + k  # Формула индекса колонки для побочной диагонали + смещение
            if 0 <= j < n:  # Проверка выхода за границы массива
                diag_sum += abs(Matr[i][j])

        # Обновляем минимум (исключаем пустые диагонали, если вдруг)
        if diag_sum > 0 and diag_sum < min_val:
            min_val = diag_sum

    return min_val


def PrintMatr(Matr, title=""):
    """Вывод матрицы на экран"""
    print(title)
    for row in Matr:
        # Выводим всю строку сразу, форматируя каждый элемент
        print(" ".join(f"{x:4d}" for x in row))
    print()


def main():
    print("Лабораторная работа №5. Вариант 5.")
    try:
        n = int(input("Введите размер матрицы N: "))

        # Генерация целых чисел от -9 до 9
        A = MakeIntMatr(n, -9, 9)
        PrintMatr(A, "Исходная матрица:")

        # Задание 1
        s1 = SumPositiveCols(A)
        print(f"\n1. Сумма в 'положительных' столбцах: {s1}")

        # Задание 2
        s2 = MinAntiDiagSum(A)
        print(f"2. Мин. сумма модулей параллельных диагоналей: {s2}")

    except ValueError:
        print("Ошибка ввода.")


if __name__ == "__main__":
    main()