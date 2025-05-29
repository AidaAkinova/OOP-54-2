def find_two_sum(nums, target):
    """
    Находит индексы двух чисел в массиве, дающих в сумме целевое значение.

    Args:
        nums: Список целых чисел
        target: Целевая сумма

    Returns:
        Список из двух индексов или None, если такая пара не найдена
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None



if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = find_two_sum(nums, target)
    print(f"Для массива {nums} и target={target} результат: {result}")