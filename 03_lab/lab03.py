def falling(n, k):
    """Рассчитать убывающий факториал от n глубины k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """


    result = 1
    for i in range(n, n - k, -1):
        result *= i
    return result


def sum_digits(y):
    """Сложить все цифры числа y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123)
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"


    # Инициализируем сумму
    sum = 0
    # Извлекаем цифры из числа, пока оно не станет равным 0
    while y != 0:
        # Извлекаем последнюю цифру числа
        digit = y % 10
        # Добавляем ее к сумме
        sum += digit
        # Удаляем последнюю цифру из числа
        y = y // 10
    return sum


def double_eights(n):
    """Возвращает True если в n есть две цифры 8 подряд.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    s = str(n)
    return "88" in s