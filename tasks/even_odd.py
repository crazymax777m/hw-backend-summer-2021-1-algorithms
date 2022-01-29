__all__ = (
    'even_odd',
)


def even_odd(arr:list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even = sum(i for i in arr if not abs(i) % 2)
    odd = sum(i for i in arr if abs(i) % 2)
    return 0 if even == 0 or odd == 0 else even / odd



