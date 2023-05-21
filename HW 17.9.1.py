def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid - 1
        else:
            return mid

    return left

def sort_sequence(sequence):
    numbers = sequence.split()
    numbers = [int(num) for num in numbers]
    numbers.sort()
    return numbers

# Ввод последовательности чисел
sequence = input("Введите последовательность чисел через пробел: ")
target_number = int(input("Введите число: "))

# Проверка на корректность ввода
try:
    numbers = sort_sequence(sequence)
except ValueError:
    print("Ошибка: некорректный ввод чисел.")
    exit()

# Поиск позиции элемента в отсортированном списке
position = binary_search(numbers, target_number)

# Проверка на соответствие числа в последовательности
if position == len(numbers):
    print("Введенное число не соответствует условию.")
else:
    print("Позиция числа в последовательности:", position)
